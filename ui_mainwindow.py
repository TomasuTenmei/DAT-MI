# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_Main = QGridLayout(self.centralwidget)
        self.gridLayout_Main.setSpacing(2)
        self.gridLayout_Main.setObjectName(u"gridLayout_Main")
        self.gridLayout_Main.setContentsMargins(20, 2, 20, 2)
        self.verticalSpacer = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_Main.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.Title.setFont(font1)
        self.Title.setAlignment(Qt.AlignCenter)
        self.Title.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_Main.addWidget(self.Title, 1, 1, 1, 1)

        self.groupBox_Visual = QGroupBox(self.centralwidget)
        self.groupBox_Visual.setObjectName(u"groupBox_Visual")
        self.gridLayout_Visual = QGridLayout(self.groupBox_Visual)
        self.gridLayout_Visual.setObjectName(u"gridLayout_Visual")

        self.gridLayout_Main.addWidget(self.groupBox_Visual, 5, 0, 1, 3)

        self.groupBox_Save = QGroupBox(self.centralwidget)
        self.groupBox_Save.setObjectName(u"groupBox_Save")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_Save.sizePolicy().hasHeightForWidth())
        self.groupBox_Save.setSizePolicy(sizePolicy1)
        self.gridLayout_Save = QGridLayout(self.groupBox_Save)
        self.gridLayout_Save.setObjectName(u"gridLayout_Save")
        self.label_AcqAll = QLabel(self.groupBox_Save)
        self.label_AcqAll.setObjectName(u"label_AcqAll")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_AcqAll.sizePolicy().hasHeightForWidth())
        self.label_AcqAll.setSizePolicy(sizePolicy2)

        self.gridLayout_Save.addWidget(self.label_AcqAll, 1, 0, 1, 1)

        self.pushButton_AcqAll = QPushButton(self.groupBox_Save)
        self.pushButton_AcqAll.setObjectName(u"pushButton_AcqAll")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_AcqAll.sizePolicy().hasHeightForWidth())
        self.pushButton_AcqAll.setSizePolicy(sizePolicy3)

        self.gridLayout_Save.addWidget(self.pushButton_AcqAll, 1, 1, 1, 2)

        self.label_AcqCh = QLabel(self.groupBox_Save)
        self.label_AcqCh.setObjectName(u"label_AcqCh")
        sizePolicy2.setHeightForWidth(self.label_AcqCh.sizePolicy().hasHeightForWidth())
        self.label_AcqCh.setSizePolicy(sizePolicy2)

        self.gridLayout_Save.addWidget(self.label_AcqCh, 0, 0, 1, 1)

        self.pushButton_AcqCh = QPushButton(self.groupBox_Save)
        self.pushButton_AcqCh.setObjectName(u"pushButton_AcqCh")
        sizePolicy3.setHeightForWidth(self.pushButton_AcqCh.sizePolicy().hasHeightForWidth())
        self.pushButton_AcqCh.setSizePolicy(sizePolicy3)

        self.gridLayout_Save.addWidget(self.pushButton_AcqCh, 0, 2, 1, 1)

        self.spinBox_AcqCh = QSpinBox(self.groupBox_Save)
        self.spinBox_AcqCh.setObjectName(u"spinBox_AcqCh")
        sizePolicy3.setHeightForWidth(self.spinBox_AcqCh.sizePolicy().hasHeightForWidth())
        self.spinBox_AcqCh.setSizePolicy(sizePolicy3)
        self.spinBox_AcqCh.setMaximum(100)

        self.gridLayout_Save.addWidget(self.spinBox_AcqCh, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_Save.addItem(self.horizontalSpacer, 0, 3, 2, 1)


        self.gridLayout_Main.addWidget(self.groupBox_Save, 7, 0, 1, 3)

        self.groupBox_Addr = QGroupBox(self.centralwidget)
        self.groupBox_Addr.setObjectName(u"groupBox_Addr")
        sizePolicy1.setHeightForWidth(self.groupBox_Addr.sizePolicy().hasHeightForWidth())
        self.groupBox_Addr.setSizePolicy(sizePolicy1)
        self.horizontalLayout_Addr = QHBoxLayout(self.groupBox_Addr)
        self.horizontalLayout_Addr.setObjectName(u"horizontalLayout_Addr")
        self.comboBox_Port = QComboBox(self.groupBox_Addr)
        self.comboBox_Port.addItem("")
        self.comboBox_Port.addItem("")
        self.comboBox_Port.addItem("")
        self.comboBox_Port.addItem("")
        self.comboBox_Port.addItem("")
        self.comboBox_Port.setObjectName(u"comboBox_Port")

        self.horizontalLayout_Addr.addWidget(self.comboBox_Port)

        self.lineEdit_Addr = QLineEdit(self.groupBox_Addr)
        self.lineEdit_Addr.setObjectName(u"lineEdit_Addr")
        self.lineEdit_Addr.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_Addr.setClearButtonEnabled(False)

        self.horizontalLayout_Addr.addWidget(self.lineEdit_Addr)

        self.pushButton_Connect = QPushButton(self.groupBox_Addr)
        self.pushButton_Connect.setObjectName(u"pushButton_Connect")

        self.horizontalLayout_Addr.addWidget(self.pushButton_Connect)


        self.gridLayout_Main.addWidget(self.groupBox_Addr, 3, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_Main.addItem(self.verticalSpacer_3, 6, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_Main.addItem(self.verticalSpacer_2, 4, 0, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_Main.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_Port.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AcqNomade", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Logiciel Acquisition Instrument en Format Tdms", None))
        self.groupBox_Visual.setTitle(QCoreApplication.translate("MainWindow", u"Visualisation", None))
        self.groupBox_Save.setTitle(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_AcqAll.setText(QCoreApplication.translate("MainWindow", u"Faire l'aquisition de toutes les voies : ", None))
        self.pushButton_AcqAll.setText(QCoreApplication.translate("MainWindow", u"Lancer", None))
        self.label_AcqCh.setText(QCoreApplication.translate("MainWindow", u"Faire l'aquisition de la voie : ", None))
        self.pushButton_AcqCh.setText(QCoreApplication.translate("MainWindow", u"Lancer", None))
        self.groupBox_Addr.setTitle(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.comboBox_Port.setItemText(0, QCoreApplication.translate("MainWindow", u"IP", None))
        self.comboBox_Port.setItemText(1, QCoreApplication.translate("MainWindow", u"GPIB", None))
        self.comboBox_Port.setItemText(2, QCoreApplication.translate("MainWindow", u"IP/GPIB", None))
        self.comboBox_Port.setItemText(3, QCoreApplication.translate("MainWindow", u"USB", None))
        self.comboBox_Port.setItemText(4, QCoreApplication.translate("MainWindow", u"Autre", None))

        self.comboBox_Port.setCurrentText("")
        self.lineEdit_Addr.setInputMask("")
        self.lineEdit_Addr.setText("")
        self.lineEdit_Addr.setPlaceholderText("")
        self.pushButton_Connect.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
    # retranslateUi

