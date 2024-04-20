# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataviz_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setBaseSize(QSize(1200, 0))
        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnFin = QPushButton(self.layoutWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btnFin)
        self.btnFin.setObjectName(u"btnFin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnFin.sizePolicy().hasHeightForWidth())
        self.btnFin.setSizePolicy(sizePolicy2)
        self.btnFin.setMinimumSize(QSize(80, 50))
        self.btnFin.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setPointSize(20)
        self.btnFin.setFont(font)
        self.btnFin.setCheckable(True)
        self.btnFin.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btnFin)

        self.btnMyData = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.btnMyData)
        self.btnMyData.setObjectName(u"btnMyData")
        sizePolicy2.setHeightForWidth(self.btnMyData.sizePolicy().hasHeightForWidth())
        self.btnMyData.setSizePolicy(sizePolicy2)
        self.btnMyData.setMinimumSize(QSize(80, 50))
        self.btnMyData.setMaximumSize(QSize(200, 50))
        self.btnMyData.setFont(font)
        self.btnMyData.setCheckable(True)
        self.btnMyData.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btnMyData)

        self.btnAnalytic = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.btnAnalytic)
        self.btnAnalytic.setObjectName(u"btnAnalytic")
        sizePolicy2.setHeightForWidth(self.btnAnalytic.sizePolicy().hasHeightForWidth())
        self.btnAnalytic.setSizePolicy(sizePolicy2)
        self.btnAnalytic.setMinimumSize(QSize(80, 50))
        self.btnAnalytic.setMaximumSize(QSize(200, 50))
        self.btnAnalytic.setFont(font)
        self.btnAnalytic.setCheckable(True)
        self.btnAnalytic.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btnAnalytic)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(22)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.treeView = QTreeView(self.layoutWidget)
        self.treeView.setObjectName(u"treeView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy3)
        self.treeView.setMinimumSize(QSize(400, 0))
        self.treeView.setMaximumSize(QSize(16777215, 300))
        self.treeView.setSizeIncrement(QSize(1, 0))
        self.treeView.setBaseSize(QSize(600, 0))
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        font2.setPointSize(20)
        self.treeView.setFont(font2)

        self.verticalLayout.addWidget(self.treeView)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(150, 16777215))
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.treeViewData = QTreeView(self.layoutWidget)
        self.treeViewData.setObjectName(u"treeViewData")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.treeViewData.sizePolicy().hasHeightForWidth())
        self.treeViewData.setSizePolicy(sizePolicy4)
        self.treeViewData.setMinimumSize(QSize(400, 0))
        self.treeViewData.setMaximumSize(QSize(16777215, 16777215))
        self.treeViewData.setSizeIncrement(QSize(1, 0))
        self.treeViewData.setBaseSize(QSize(600, 0))
        self.treeViewData.setFont(font2)
        self.treeViewData.setLineWidth(1)
        self.treeViewData.setMidLineWidth(1)

        self.verticalLayout.addWidget(self.treeViewData)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setPointSize(22)
        self.label_3.setFont(font3)

        self.verticalLayout.addWidget(self.label_3)

        self.codeView = QPlainTextEdit(self.layoutWidget)
        self.codeView.setObjectName(u"codeView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.codeView.sizePolicy().hasHeightForWidth())
        self.codeView.setSizePolicy(sizePolicy5)
        self.codeView.setMinimumSize(QSize(400, 0))
        self.codeView.setMaximumSize(QSize(16777215, 16777215))
        self.codeView.setSizeIncrement(QSize(1, 0))
        self.codeView.setBaseSize(QSize(600, 0))
        font4 = QFont()
        font4.setFamilies([u"Ricty"])
        font4.setPointSize(18)
        self.codeView.setFont(font4)

        self.verticalLayout.addWidget(self.codeView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        font5 = QFont()
        font5.setFamilies([u".AppleSystemUIFont"])
        font5.setPointSize(36)
        self.label_4.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineNum = QLabel(self.layoutWidget)
        self.lineNum.setObjectName(u"lineNum")
        sizePolicy6.setHeightForWidth(self.lineNum.sizePolicy().hasHeightForWidth())
        self.lineNum.setSizePolicy(sizePolicy6)
        self.lineNum.setMinimumSize(QSize(100, 0))
        font6 = QFont()
        font6.setFamilies([u".AppleSystemUIFont"])
        font6.setPointSize(36)
        font6.setBold(True)
        font6.setUnderline(False)
        self.lineNum.setFont(font6)
        self.lineNum.setFrameShadow(QFrame.Raised)
        self.lineNum.setLineWidth(0)
        self.lineNum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineNum)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.plotButton = QPushButton(self.layoutWidget)
        self.plotButton.setObjectName(u"plotButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.plotButton.sizePolicy().hasHeightForWidth())
        self.plotButton.setSizePolicy(sizePolicy7)
        self.plotButton.setMinimumSize(QSize(120, 80))
        self.plotButton.setMaximumSize(QSize(120, 80))
        self.plotButton.setFont(font5)

        self.horizontalLayout_2.addWidget(self.plotButton)

        self.quitButton = QPushButton(self.layoutWidget)
        self.quitButton.setObjectName(u"quitButton")
        sizePolicy7.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy7)
        self.quitButton.setMinimumSize(QSize(120, 80))
        self.quitButton.setMaximumSize(QSize(120, 80))
        self.quitButton.setFont(font5)

        self.horizontalLayout_2.addWidget(self.quitButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnFin.setText(QCoreApplication.translate("MainWindow", u"Finance", None))
        self.btnMyData.setText(QCoreApplication.translate("MainWindow", u"myDataViz", None))
        self.btnAnalytic.setText(QCoreApplication.translate("MainWindow", u"AnalyticViz", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model Script", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Edit Code", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u884c\u756a\u53f7\uff1a", None))
        self.lineNum.setText("")
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

