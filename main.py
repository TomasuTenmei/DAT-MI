"""
╔═════════════╦════════════╦═══════════╦═══════════════════════════════════════╗
║ Version 1.0 ║ 31/01/2024 ║ SERE/LE2R ║         Auteur: Thomas ARNAUD         ║
╠═════════════╩════════════╩═══════════╩═══════════════════════════════════════╣
║           Lecteur d'ocsilloscopes & enregistrement en format TDMS            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import sys, os, traceback, pyvisa, time
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QLabel
from PySide6.QtGui import QPainter, QPen, Qt
from PySide6.QtCore import QPointF, QThreadPool, Slot, Signal, QObject, QRunnable
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from nptdms import TdmsWriter, RootObject, GroupObject, ChannelObject, TdmsFile

from ui_mainwindow import Ui_MainWindow

# Threads
class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):

        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):

        try:

            result = self.fn(*self.args, **self.kwargs)

        except:

            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:

            self.signals.result.emit(result)

        finally:

            self.signals.finished.emit()

# Main
class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_Addr.textChanged.connect(self.readAddr)
        self.ui.pushButton_Connect.clicked.connect(self.connectScope)
        self.ui.pushButton_AcqCh.clicked.connect(self.acqChannel)
        self.ui.pushButton_AcqAll.clicked.connect(self.acqAll)
        self.ui.comboBox_Port.currentIndexChanged.connect(self.updateAddr)
        
        self.ui.comboBox_Port.setPlaceholderText("Port")

        self.addr = 'TCPIP::192.168.7.43::INSTR'
        self.rm = pyvisa.ResourceManager()
        self.connected = 0

        self.message = QLabel()
        self.message.setText("En attente de données à acquérir (Stop sur l'instrument)")
        self.ui.gridLayout_Visual.addWidget(self.message, 1, 1, 1, 1)

        # Création du graphique
        self.chart = QChart()

        # Création des Axes
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()
        self.axisX.setLabelFormat("%.1E s")
        self.axisY.setLabelFormat("%.1E V")

        # Ajout des axes au graph
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)

        # Affichage graph
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.ui.gridLayout_Visual.addWidget(self.chartView, 1, 1, 1, 1)

        # Threadpool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    # Gestion Thread
    def progress_fn(self, n):

        pass

    def print_output(self, s):

        pass

    def thread_complete(self):

        print('End thread')

    def exec_thread(self, fn):

        worker = Worker(fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    # Fonctions
    def readAddr(self):

        self.addr = self.ui.lineEdit_Addr.text()

    def updateAddr(self):

        if self.ui.comboBox_Port.currentText() == "IP":

            self.ui.lineEdit_Addr.setText('TCPIP::192.168.X.X::INSTR')
            
        elif self.ui.comboBox_Port.currentText() == "GPIB":

            self.ui.lineEdit_Addr.setText('GPIBX::X::INSTR')
            
        elif self.ui.comboBox_Port.currentText() == "IP/GPIB":

            self.ui.lineEdit_Addr.setText('TCPIP::192.168.X.X::gpibX,X::INSTR')
            
        elif self.ui.comboBox_Port.currentText() == "USB":

            self.ui.lineEdit_Addr.setText('USBX::X::INSTR')
            
        elif self.ui.comboBox_Port.currentText() == "Autre":

            self.ui.lineEdit_Addr.setText('')

    def connectScope(self):

        if self.connected == 0: # Connexion

            if len(self.addr) == 0:

                QMessageBox.critical(self, "Error", "Vous n'avez pas rentré d'adresse.", QMessageBox.Ok)

            else:

                try:

                    self.instr = self.rm.open_resource(self.addr) # Ouverture de la connection
                    self.model = self.instr.query('*idn?') # Lecture du modèle des oscilloscopes

                    # Mise en place du header
                    if self.model.find("Rohde&Schwarz") >= 0:

                        self.instr.write('FORMAT ASCII')

                    elif self.model.find("TEKTRONIX") >= 0:

                        self.instr.write('HEAD OFF')
                        self.instr.write('VERB OFF')
                        self.instr.write('DIS:SHOWRE ON')
                        self.instr.write('DATA:ENC ASCII')

                    elif self.model.find("LECROY") >= 0:

                        self.instr.write('COMM_HEADER OFF') # Désactive le retour de la commande dans la réponse

                    self.connected = 1
                    self.ui.pushButton_Connect.setText("Connecté")
                    self.ui.pushButton_Connect.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0, 0, 0);")
                    print('Connecté')

                    # Acquisition
                    self.exec_thread(self.updateGraph)

                except pyvisa.errors.VisaIOError as e:

                    QMessageBox.critical(self, "Error", str(e), QMessageBox.Ok)

        else: # Deconnexion

            self.instr.close()
            self.connected = 0
            self.ui.pushButton_Connect.setText("Déconnecté")
            self.ui.pushButton_Connect.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")
            self.chartView.hide()
            self.message.hide()
            print('Déconnecté')

    def updateGraph(self, progress_callback):
        
        while self.connected == 1:

            try:

                # Initialisation
                dicoChannels = {}
                dicoChannels['channels'] = {}
                dicoChannels['data'] = {}
                dicoChannels['temps'] = []
                dicoChannels['rangeAxis'] = 0
                self.chart.removeAllSeries()
                
                if self.model.find("RTM3004") >= 0:
                    
                    # Scope 4 voies
                    for i in range(1, 5):
                        
                        if int(self.instr.query(f'CHAN{i}:STAT?')) == 1:
                            
                            # Récupération des points
                            channelData = self.instr.query_ascii_values(f'CHAN{i}:DATA?')
                            dicoChannels['data'][f'ch{i}'] = channelData
                            
                            # Information sur l'acquisition
                            dicoChannels['nbPoints'] = len(channelData)
                            dicoChannels['xorigine'] = float(self.instr.query(f'CHAN{i}:DATA:XOR?'))
                            dicoChannels['xincrement'] = float(self.instr.query(f'CHAN{i}:DATA:XINC?'))

                            if dicoChannels['rangeAxis'] < float(self.instr.query(f'CHAN{i}:RANG?')):

                                dicoChannels['rangeAxis'] = float(self.instr.query(f'CHAN{i}:RANG?'))

                            # Implémentation des données
                            dicoChannels['channels'][f'ch{i}'] = QLineSeries()
                            
                            # Calcule du temps pour chaque points
                            for point in range(dicoChannels['nbPoints']):
                                
                                # Calcule et indexation des x
                                dicoChannels['temps'].append(point * dicoChannels['xincrement'] + dicoChannels['xorigine'])
                                
                                # Implémentation des données
                                dicoChannels['channels'][f'ch{i}'].append(dicoChannels['temps'][point], channelData[point])
                
                # Ajout des données au graph
                for key in dicoChannels['channels']:
                    
                    self.chart.addSeries(dicoChannels['channels'][key])
                    #dicoChannels['channels'][key].setName(key.upper())

                # Configuration des Axes
                self.axisX.setRange(dicoChannels['temps'][0], dicoChannels['temps'][-1])
                self.axisY.setRange(-dicoChannels['rangeAxis'] / 2, dicoChannels['rangeAxis'] / 2)
                
                # Liaison des séries aux axes
                for key in dicoChannels['channels']:

                    dicoChannels['channels'][key].attachAxis(self.axisY)

                # Affichage
                #self.chart.update()
                self.message.hide()
                self.chartView.show()

            except:

                # Affichage
                self.chartView.hide()
                self.message.show()

        time.sleep(1)
        print('Update')

    def acqChannel(self):

        QMessageBox.critical(self, "Error", "Work in progress (en gros attend la prochaine version !)", QMessageBox.Ok)

    def acqAll(self):

        # Choix du lieux de sauvegarde
        savePath = QFileDialog.getSaveFileName(self, "Save data", "C:/", "Fichier de données (*.tdms)")
        fileName = savePath[0].split('/')[-1][:-5]
        
        # Parametre du tableau    
        root_object = RootObject(properties={
            "prop1": "foo",
            "prop2": 3,
        })
        group_object = GroupObject(fileName, properties={
            "prop1": 1.2345,
            "prop2": False,
        })

        # Nom de la feuille + valeur de temps
        channel_object = ChannelObject(fileName, "t", dicoChannels['temps'], properties={})
        
        # Nom du fichier
        with TdmsWriter(savePath[0]) as tdms_writer:
                
            tdms_writer.write_segment([
                root_object,
                group_object,
                channel_object
            ])
                
            # Autres colonnes avec feuille, nom de la data, data
            for key in dicoChannels['data']:

                channel_object = ChannelObject(fileName, key, dicoChannels['data'][key], properties={})
                tdms_writer.write_segment([channel_object])


# Affichage du GUI
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())