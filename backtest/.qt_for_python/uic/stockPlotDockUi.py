# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockPlotDockUi.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

from pyqtgraph.dockarea import DockArea

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1596, 831)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpenDialog = QAction(MainWindow)
        self.actionOpenDialog.setObjectName(u"actionOpenDialog")
        self.actionQuit2 = QAction(MainWindow)
        self.actionQuit2.setObjectName(u"actionQuit2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.dockWidget = DockArea(self.centralwidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.dockWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 10, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, 0, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMaximumSize(QSize(250, 16777215))
        self.lineEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.lineEdit_TickSyml = QLineEdit(self.centralwidget)
        self.lineEdit_TickSyml.setObjectName(u"lineEdit_TickSyml")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_TickSyml.sizePolicy().hasHeightForWidth())
        self.lineEdit_TickSyml.setSizePolicy(sizePolicy3)
        self.lineEdit_TickSyml.setMaximumSize(QSize(170, 21))
        self.lineEdit_TickSyml.setFont(font)

        self.horizontalLayout_7.addWidget(self.lineEdit_TickSyml)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMaximumSize(QSize(63, 32))
        self.pushButton.setFont(font)

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy4)
        self.tableView.setMaximumSize(QSize(350, 16777215))
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(350, 132))
        self.groupBox.setMaximumSize(QSize(350, 16777215))
        self.groupBox.setBaseSize(QSize(0, 0))
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 24, 181, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.comboBox)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 55, 341, 34))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinBox_Short = QSpinBox(self.layoutWidget1)
        self.spinBox_Short.setObjectName(u"spinBox_Short")
        self.spinBox_Short.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Short.setAlignment(Qt.AlignCenter)
        self.spinBox_Short.setMinimum(5)

        self.horizontalLayout_4.addWidget(self.spinBox_Short)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 16777215))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBox_Long = QSpinBox(self.layoutWidget1)
        self.spinBox_Long.setObjectName(u"spinBox_Long")
        self.spinBox_Long.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Long.setAlignment(Qt.AlignCenter)
        self.spinBox_Long.setMinimum(20)

        self.horizontalLayout_4.addWidget(self.spinBox_Long)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 95, 241, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox_InsMethod = QComboBox(self.layoutWidget2)
        self.comboBox_InsMethod.addItem("")
        self.comboBox_InsMethod.addItem("")
        self.comboBox_InsMethod.addItem("")
        self.comboBox_InsMethod.addItem("")
        self.comboBox_InsMethod.setObjectName(u"comboBox_InsMethod")

        self.horizontalLayout_5.addWidget(self.comboBox_InsMethod)


        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.label_InsMethod = QLabel(self.centralwidget)
        self.label_InsMethod.setObjectName(u"label_InsMethod")
        self.label_InsMethod.setMaximumSize(QSize(170, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_InsMethod.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_InsMethod)

        self.lineEdit_InsMethod = QLineEdit(self.centralwidget)
        self.lineEdit_InsMethod.setObjectName(u"lineEdit_InsMethod")
        self.lineEdit_InsMethod.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_InsMethod.setFont(font1)
        self.lineEdit_InsMethod.setAlignment(Qt.AlignCenter)
        self.lineEdit_InsMethod.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_InsMethod)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit_APU = QLineEdit(self.centralwidget)
        self.lineEdit_APU.setObjectName(u"lineEdit_APU")
        self.lineEdit_APU.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_APU.setFont(font1)
        self.lineEdit_APU.setAlignment(Qt.AlignCenter)
        self.lineEdit_APU.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_APU)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.lineEdit_Percent = QLineEdit(self.centralwidget)
        self.lineEdit_Percent.setObjectName(u"lineEdit_Percent")
        self.lineEdit_Percent.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_Percent.setFont(font1)
        self.lineEdit_Percent.setAlignment(Qt.AlignCenter)
        self.lineEdit_Percent.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_Percent)

        self.horizontalSpacer_2 = QSpacerItem(765, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        sizePolicy3.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy3)
        self.quitButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.quitButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1596, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpenDialog)
        self.menuFile.addAction(self.actionQuit2)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)
        self.actionQuit2.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpenDialog.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit2.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ticker Symbol", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u30d1\u30e9\u30e1\u30fc\u30bf\u30fc\u8a2d\u5b9a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time Span", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Daily", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"60min", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"30min", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"15min", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5min", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SMA Short", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SMA Long", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u691c\u8a3c\u65b9\u6cd5", None))
        self.comboBox_InsMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Golden Cross", None))
        self.comboBox_InsMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"LowerBBTouched", None))
        self.comboBox_InsMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"MACD Uptrend", None))
        self.comboBox_InsMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"Price Touch RSI30", None))

        self.label_InsMethod.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Actual Price Up :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Percentage :", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

