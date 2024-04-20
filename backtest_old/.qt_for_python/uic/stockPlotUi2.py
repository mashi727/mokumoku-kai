# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockPlotUi2.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableView,
    QTextBrowser, QVBoxLayout, QWidget)

from pyqtgraph.dockarea import DockArea

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(2392, 1365)
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
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, 10, 0)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(350, 80))
        self.groupBox_2.setMaximumSize(QSize(350, 80))
        self.groupBox_2.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.groupBox_2.setFont(font1)
        self.layoutWidget_3 = QWidget(self.groupBox_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 13, 323, 54))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMaximumSize(QSize(140, 23))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10.setIndent(15)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(180, 23))
        self.lineEdit.setMaximumSize(QSize(180, 23))
        self.lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(140, 23))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setMargin(0)
        self.label_3.setIndent(15)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_TickSyml = QLineEdit(self.layoutWidget_3)
        self.lineEdit_TickSyml.setObjectName(u"lineEdit_TickSyml")
        sizePolicy1.setHeightForWidth(self.lineEdit_TickSyml.sizePolicy().hasHeightForWidth())
        self.lineEdit_TickSyml.setSizePolicy(sizePolicy1)
        self.lineEdit_TickSyml.setMinimumSize(QSize(180, 23))
        self.lineEdit_TickSyml.setMaximumSize(QSize(180, 23))
        self.lineEdit_TickSyml.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit_TickSyml, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMinimumSize(QSize(40, 0))
        self.label_22.setMaximumSize(QSize(40, 16777215))
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22.setIndent(10)

        self.horizontalLayout_6.addWidget(self.label_22)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMinimumSize(QSize(47, 0))
        self.label_23.setMaximumSize(QSize(47, 16777215))
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_23.setIndent(0)

        self.horizontalLayout_6.addWidget(self.label_23)

        self.SB_sma_short = QSpinBox(self.centralwidget)
        self.SB_sma_short.setObjectName(u"SB_sma_short")
        self.SB_sma_short.setMinimumSize(QSize(50, 0))
        self.SB_sma_short.setMaximumSize(QSize(50, 16777215))
        self.SB_sma_short.setFont(font1)
        self.SB_sma_short.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_sma_short.setMinimum(1)
        self.SB_sma_short.setMaximum(500)
        self.SB_sma_short.setValue(5)

        self.horizontalLayout_6.addWidget(self.SB_sma_short)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMaximumSize(QSize(40, 16777215))
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_24.setIndent(0)

        self.horizontalLayout_6.addWidget(self.label_24)

        self.SB_sma_med = QSpinBox(self.centralwidget)
        self.SB_sma_med.setObjectName(u"SB_sma_med")
        sizePolicy1.setHeightForWidth(self.SB_sma_med.sizePolicy().hasHeightForWidth())
        self.SB_sma_med.setSizePolicy(sizePolicy1)
        self.SB_sma_med.setMinimumSize(QSize(50, 0))
        self.SB_sma_med.setMaximumSize(QSize(50, 16777215))
        self.SB_sma_med.setFont(font1)
        self.SB_sma_med.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_sma_med.setMinimum(1)
        self.SB_sma_med.setMaximum(500)
        self.SB_sma_med.setValue(20)

        self.horizontalLayout_6.addWidget(self.SB_sma_med)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setMaximumSize(QSize(40, 16777215))
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_25.setIndent(0)

        self.horizontalLayout_6.addWidget(self.label_25)

        self.SB_sma_long = QSpinBox(self.centralwidget)
        self.SB_sma_long.setObjectName(u"SB_sma_long")
        self.SB_sma_long.setMinimumSize(QSize(50, 0))
        self.SB_sma_long.setMaximumSize(QSize(50, 16777215))
        self.SB_sma_long.setFont(font1)
        self.SB_sma_long.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_sma_long.setMinimum(1)
        self.SB_sma_long.setMaximum(500)
        self.SB_sma_long.setValue(60)

        self.horizontalLayout_6.addWidget(self.SB_sma_long)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setMaximumSize(QSize(150, 16777215))
        self.label_26.setFont(font1)
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_26.setIndent(10)

        self.horizontalLayout_4.addWidget(self.label_26)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        self.comboBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMaximumSize(QSize(350, 16777215))
        self.tableView.setBaseSize(QSize(0, 15))
        self.tableView.setFont(font1)
        self.tableView.setFrameShape(QFrame.StyledPanel)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(350, 0))
        self.textBrowser.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.dockWidget = DockArea(self.centralwidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.dockWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 10, 10, 0)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setMargin(7)

        self.verticalLayout.addWidget(self.label_5)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy1.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy1)
        self.tabWidget_2.setMinimumSize(QSize(350, 250))
        self.tabWidget_2.setFont(font1)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(Qt.ElideMiddle)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tab_SMACross = QWidget()
        self.tab_SMACross.setObjectName(u"tab_SMACross")
        self.layoutWidget_2 = QWidget(self.tab_SMACross)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 317, 170))
        self.gridLayout_6 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.layoutWidget_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)

        self.gridLayout_6.addWidget(self.label_45, 0, 0, 1, 1)

        self.lineEdit_cash_5 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_cash_5.setObjectName(u"lineEdit_cash_5")

        self.gridLayout_6.addWidget(self.lineEdit_cash_5, 0, 1, 1, 3)

        self.label_46 = QLabel(self.layoutWidget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)

        self.gridLayout_6.addWidget(self.label_46, 1, 0, 1, 1)

        self.lineEdit_commision_5 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_commision_5.setObjectName(u"lineEdit_commision_5")

        self.gridLayout_6.addWidget(self.lineEdit_commision_5, 1, 1, 1, 3)

        self.label_47 = QLabel(self.layoutWidget_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)

        self.gridLayout_6.addWidget(self.label_47, 2, 0, 1, 1)

        self.lineEdit_margin_5 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_margin_5.setObjectName(u"lineEdit_margin_5")
        self.lineEdit_margin_5.setAutoFillBackground(False)
        self.lineEdit_margin_5.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_6.addWidget(self.lineEdit_margin_5, 2, 1, 1, 3)

        self.label_48 = QLabel(self.layoutWidget_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(70, 0))
        self.label_48.setMaximumSize(QSize(70, 16777215))
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_48, 3, 0, 1, 1)

        self.spinBox_Short_5 = QSpinBox(self.layoutWidget_2)
        self.spinBox_Short_5.setObjectName(u"spinBox_Short_5")
        sizePolicy1.setHeightForWidth(self.spinBox_Short_5.sizePolicy().hasHeightForWidth())
        self.spinBox_Short_5.setSizePolicy(sizePolicy1)
        self.spinBox_Short_5.setMinimumSize(QSize(70, 0))
        self.spinBox_Short_5.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Short_5.setAlignment(Qt.AlignCenter)
        self.spinBox_Short_5.setMinimum(5)

        self.gridLayout_6.addWidget(self.spinBox_Short_5, 3, 1, 1, 2)

        self.label_49 = QLabel(self.layoutWidget_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(70, 0))
        self.label_49.setMaximumSize(QSize(70, 16777215))
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_49, 3, 3, 1, 1)

        self.spinBox_Long_5 = QSpinBox(self.layoutWidget_2)
        self.spinBox_Long_5.setObjectName(u"spinBox_Long_5")
        self.spinBox_Long_5.setMinimumSize(QSize(70, 0))
        self.spinBox_Long_5.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Long_5.setAlignment(Qt.AlignCenter)
        self.spinBox_Long_5.setMinimum(20)

        self.gridLayout_6.addWidget(self.spinBox_Long_5, 3, 4, 1, 1)

        self.label_50 = QLabel(self.layoutWidget_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(100, 0))
        self.label_50.setMaximumSize(QSize(100, 16777215))
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_50, 4, 0, 1, 2)

        self.comboBox_ToC_5 = QComboBox(self.layoutWidget_2)
        self.comboBox_ToC_5.addItem("")
        self.comboBox_ToC_5.addItem("")
        self.comboBox_ToC_5.setObjectName(u"comboBox_ToC_5")
        self.comboBox_ToC_5.setMinimumSize(QSize(200, 0))
        self.comboBox_ToC_5.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.comboBox_ToC_5, 4, 2, 1, 3)

        self.label_51 = QLabel(self.layoutWidget_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(100, 0))
        self.label_51.setMaximumSize(QSize(100, 16777215))
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_51, 5, 0, 1, 2)

        self.comboBox_EO_5 = QComboBox(self.layoutWidget_2)
        self.comboBox_EO_5.addItem("")
        self.comboBox_EO_5.addItem("")
        self.comboBox_EO_5.setObjectName(u"comboBox_EO_5")
        self.comboBox_EO_5.setMinimumSize(QSize(200, 0))
        self.comboBox_EO_5.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.comboBox_EO_5, 5, 2, 1, 3)

        self.tabWidget_2.addTab(self.tab_SMACross, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 317, 199))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.layoutWidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.gridLayout_3.addWidget(self.label_38, 0, 0, 1, 1)

        self.lineEdit_cash_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_cash_4.setObjectName(u"lineEdit_cash_4")

        self.gridLayout_3.addWidget(self.lineEdit_cash_4, 0, 1, 1, 3)

        self.label_39 = QLabel(self.layoutWidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.gridLayout_3.addWidget(self.label_39, 1, 0, 1, 1)

        self.lineEdit_commision_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_commision_4.setObjectName(u"lineEdit_commision_4")

        self.gridLayout_3.addWidget(self.lineEdit_commision_4, 1, 1, 1, 3)

        self.label_40 = QLabel(self.layoutWidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.gridLayout_3.addWidget(self.label_40, 2, 0, 1, 1)

        self.lineEdit_margin_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_margin_4.setObjectName(u"lineEdit_margin_4")
        self.lineEdit_margin_4.setAutoFillBackground(False)
        self.lineEdit_margin_4.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.lineEdit_margin_4, 2, 1, 1, 3)

        self.label_41 = QLabel(self.layoutWidget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(70, 0))
        self.label_41.setMaximumSize(QSize(70, 16777215))
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_41, 3, 0, 1, 1)

        self.spinBox_Short_4 = QSpinBox(self.layoutWidget)
        self.spinBox_Short_4.setObjectName(u"spinBox_Short_4")
        sizePolicy1.setHeightForWidth(self.spinBox_Short_4.sizePolicy().hasHeightForWidth())
        self.spinBox_Short_4.setSizePolicy(sizePolicy1)
        self.spinBox_Short_4.setMinimumSize(QSize(70, 0))
        self.spinBox_Short_4.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Short_4.setAlignment(Qt.AlignCenter)
        self.spinBox_Short_4.setMinimum(12)

        self.gridLayout_3.addWidget(self.spinBox_Short_4, 3, 1, 1, 2)

        self.label_42 = QLabel(self.layoutWidget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(70, 0))
        self.label_42.setMaximumSize(QSize(70, 16777215))
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_42, 3, 3, 1, 1)

        self.spinBox_Long_4 = QSpinBox(self.layoutWidget)
        self.spinBox_Long_4.setObjectName(u"spinBox_Long_4")
        self.spinBox_Long_4.setMinimumSize(QSize(70, 0))
        self.spinBox_Long_4.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Long_4.setAlignment(Qt.AlignCenter)
        self.spinBox_Long_4.setMinimum(26)

        self.gridLayout_3.addWidget(self.spinBox_Long_4, 3, 4, 1, 1)

        self.label_52 = QLabel(self.layoutWidget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(100, 0))
        self.label_52.setMaximumSize(QSize(100, 16777215))
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_52, 4, 0, 1, 2)

        self.spinBox_Long_6 = QSpinBox(self.layoutWidget)
        self.spinBox_Long_6.setObjectName(u"spinBox_Long_6")
        self.spinBox_Long_6.setMinimumSize(QSize(70, 0))
        self.spinBox_Long_6.setMaximumSize(QSize(70, 16777215))
        self.spinBox_Long_6.setAlignment(Qt.AlignCenter)
        self.spinBox_Long_6.setMinimum(26)

        self.gridLayout_3.addWidget(self.spinBox_Long_6, 4, 2, 1, 2)

        self.label_43 = QLabel(self.layoutWidget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(100, 0))
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_43, 5, 0, 1, 2)

        self.comboBox_ToC_4 = QComboBox(self.layoutWidget)
        self.comboBox_ToC_4.addItem("")
        self.comboBox_ToC_4.addItem("")
        self.comboBox_ToC_4.setObjectName(u"comboBox_ToC_4")
        self.comboBox_ToC_4.setMinimumSize(QSize(200, 0))
        self.comboBox_ToC_4.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_ToC_4, 5, 2, 1, 3)

        self.label_44 = QLabel(self.layoutWidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(100, 16777215))
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_44, 6, 0, 1, 2)

        self.comboBox_EO_4 = QComboBox(self.layoutWidget)
        self.comboBox_EO_4.addItem("")
        self.comboBox_EO_4.addItem("")
        self.comboBox_EO_4.setObjectName(u"comboBox_EO_4")
        self.comboBox_EO_4.setMinimumSize(QSize(200, 0))
        self.comboBox_EO_4.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_EO_4, 6, 2, 1, 3)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")

        self.verticalLayout.addWidget(self.tabWidget_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(40, 0))
        self.label_4.setMaximumSize(QSize(40, 16777215))
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_start_region = QLineEdit(self.centralwidget)
        self.lineEdit_start_region.setObjectName(u"lineEdit_start_region")
        sizePolicy1.setHeightForWidth(self.lineEdit_start_region.sizePolicy().hasHeightForWidth())
        self.lineEdit_start_region.setSizePolicy(sizePolicy1)
        self.lineEdit_start_region.setMinimumSize(QSize(120, 21))
        self.lineEdit_start_region.setMaximumSize(QSize(120, 21))
        self.lineEdit_start_region.setFont(font1)
        self.lineEdit_start_region.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_start_region)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(40, 0))
        self.label_6.setMaximumSize(QSize(40, 16777215))
        self.label_6.setFont(font1)

        self.horizontalLayout.addWidget(self.label_6)

        self.lineEdit_end_region = QLineEdit(self.centralwidget)
        self.lineEdit_end_region.setObjectName(u"lineEdit_end_region")
        sizePolicy1.setHeightForWidth(self.lineEdit_end_region.sizePolicy().hasHeightForWidth())
        self.lineEdit_end_region.setSizePolicy(sizePolicy1)
        self.lineEdit_end_region.setMinimumSize(QSize(120, 21))
        self.lineEdit_end_region.setMaximumSize(QSize(120, 21))
        self.lineEdit_end_region.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_end_region)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView_backtesting = QTableView(self.centralwidget)
        self.tableView_backtesting.setObjectName(u"tableView_backtesting")
        sizePolicy.setHeightForWidth(self.tableView_backtesting.sizePolicy().hasHeightForWidth())
        self.tableView_backtesting.setSizePolicy(sizePolicy)
        self.tableView_backtesting.setMinimumSize(QSize(350, 0))
        self.tableView_backtesting.setMaximumSize(QSize(350, 16777215))
        self.tableView_backtesting.setFont(font1)
        self.tableView_backtesting.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView_backtesting)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 10, 10, 0)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setMargin(7)

        self.verticalLayout_3.addWidget(self.label_7)

        self.tabWidget_3 = QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy1.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy1)
        self.tabWidget_3.setMinimumSize(QSize(350, 250))
        self.tabWidget_3.setFont(font1)
        self.tabWidget_3.setTabShape(QTabWidget.Rounded)
        self.tabWidget_3.setElideMode(Qt.ElideMiddle)
        self.tabWidget_3.setUsesScrollButtons(False)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tab_SMACross_2 = QWidget()
        self.tab_SMACross_2.setObjectName(u"tab_SMACross_2")
        self.tabWidget_3.addTab(self.tab_SMACross_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")

        self.verticalLayout_3.addWidget(self.tabWidget_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(40, 0))
        self.label_9.setMaximumSize(QSize(40, 16777215))
        self.label_9.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.lineEdit_start_region_2 = QLineEdit(self.centralwidget)
        self.lineEdit_start_region_2.setObjectName(u"lineEdit_start_region_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_start_region_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_start_region_2.setSizePolicy(sizePolicy1)
        self.lineEdit_start_region_2.setMinimumSize(QSize(120, 21))
        self.lineEdit_start_region_2.setMaximumSize(QSize(120, 21))
        self.lineEdit_start_region_2.setFont(font1)
        self.lineEdit_start_region_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_start_region_2)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setMinimumSize(QSize(40, 0))
        self.label_30.setMaximumSize(QSize(40, 16777215))
        self.label_30.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_30)

        self.lineEdit_end_region_2 = QLineEdit(self.centralwidget)
        self.lineEdit_end_region_2.setObjectName(u"lineEdit_end_region_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_end_region_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_end_region_2.setSizePolicy(sizePolicy1)
        self.lineEdit_end_region_2.setMinimumSize(QSize(120, 21))
        self.lineEdit_end_region_2.setMaximumSize(QSize(120, 21))
        self.lineEdit_end_region_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_end_region_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tableView_backtesting_2 = QTableView(self.centralwidget)
        self.tableView_backtesting_2.setObjectName(u"tableView_backtesting_2")
        sizePolicy.setHeightForWidth(self.tableView_backtesting_2.sizePolicy().hasHeightForWidth())
        self.tableView_backtesting_2.setSizePolicy(sizePolicy)
        self.tableView_backtesting_2.setMinimumSize(QSize(350, 0))
        self.tableView_backtesting_2.setMaximumSize(QSize(350, 16777215))
        self.tableView_backtesting_2.setFont(font1)
        self.tableView_backtesting_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_3.addWidget(self.tableView_backtesting_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, 10)
        self.horizontalSpacer_2 = QSpacerItem(765, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        sizePolicy1.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy1)
        self.quitButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.quitButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2392, 22))
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

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpenDialog.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit2.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9298\u67c4\u6307\u5b9a", None))
        self.groupBox_2.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"from Alphavantage", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search NASDAQ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SMA :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Med.", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Time Span", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Daily", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"60min", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"30min", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"15min", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5min", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u691c\u8a3c\uff11(backtesting.py)", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.lineEdit_cash_5.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Commision", None))
        self.lineEdit_commision_5.setText(QCoreApplication.translate("MainWindow", u"0.00495", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
        self.lineEdit_margin_5.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"SMA Short", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"SMA Long", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Trade on Close", None))
        self.comboBox_ToC_5.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.comboBox_ToC_5.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Exclusive Orders", None))
        self.comboBox_EO_5.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.comboBox_EO_5.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_SMACross), QCoreApplication.translate("MainWindow", u"SmaCross", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.lineEdit_cash_4.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Commision", None))
        self.lineEdit_commision_4.setText(QCoreApplication.translate("MainWindow", u"0.00495", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
        self.lineEdit_margin_4.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u77ed\u671fEMA", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u9577\u671fEMA", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"SMA for MACD", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Trade on Close", None))
        self.comboBox_ToC_4.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.comboBox_ToC_4.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Exclusive Orders", None))
        self.comboBox_EO_4.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.comboBox_EO_4.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"MACDCross", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u30da\u30fc\u30b8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u30da\u30fc\u30b8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u30da\u30fc\u30b8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u30da\u30fc\u30b8", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"End :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u691c\u8a3c\uff12(backtesting.py)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_SMACross_2), QCoreApplication.translate("MainWindow", u"SmaCross", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"MACDCross", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Start :", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"End :", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

