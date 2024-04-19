# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(697, 626)
        MainWindow.setAutoFillBackground(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(80, 5, 80, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.stockListBox = QComboBox(self.centralwidget)
        self.stockListBox.setObjectName(u"stockListBox")
        sizePolicy.setHeightForWidth(self.stockListBox.sizePolicy().hasHeightForWidth())
        self.stockListBox.setSizePolicy(sizePolicy)
        self.stockListBox.setMinimumSize(QSize(0, 0))
        self.stockListBox.setEditable(True)

        self.horizontalLayout_2.addWidget(self.stockListBox)

        self.updateStockListButton = QPushButton(self.centralwidget)
        self.updateStockListButton.setObjectName(u"updateStockListButton")

        self.horizontalLayout_2.addWidget(self.updateStockListButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.startDateEdit = QDateEdit(self.tab)
        self.startDateEdit.setObjectName(u"startDateEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.startDateEdit.sizePolicy().hasHeightForWidth())
        self.startDateEdit.setSizePolicy(sizePolicy2)
        self.startDateEdit.setAlignment(Qt.AlignCenter)
        self.startDateEdit.setDateTime(QDateTime(QDate(2015, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_3.addWidget(self.startDateEdit)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.endDateEdit = QDateEdit(self.tab)
        self.endDateEdit.setObjectName(u"endDateEdit")
        sizePolicy2.setHeightForWidth(self.endDateEdit.sizePolicy().hasHeightForWidth())
        self.endDateEdit.setSizePolicy(sizePolicy2)
        self.endDateEdit.setAlignment(Qt.AlignCenter)
        self.endDateEdit.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_3.addWidget(self.endDateEdit)

        self.getHistoryInfoButton = QPushButton(self.tab)
        self.getHistoryInfoButton.setObjectName(u"getHistoryInfoButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.getHistoryInfoButton.sizePolicy().hasHeightForWidth())
        self.getHistoryInfoButton.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.getHistoryInfoButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.historyInfoBrowser = QTextBrowser(self.tab)
        self.historyInfoBrowser.setObjectName(u"historyInfoBrowser")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.historyInfoBrowser.sizePolicy().hasHeightForWidth())
        self.historyInfoBrowser.setSizePolicy(sizePolicy5)

        self.verticalLayout_6.addWidget(self.historyInfoBrowser)

        self.historyPlot = PlotWidget(self.tab)
        self.historyPlot.setObjectName(u"historyPlot")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.historyPlot.sizePolicy().hasHeightForWidth())
        self.historyPlot.setSizePolicy(sizePolicy6)

        self.verticalLayout_6.addWidget(self.historyPlot)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 697, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30c8\u30c3\u30af\u30b3\u30fc\u30c9\u306e\u66f4\u65b0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9298\u67c4\u540d\u307e\u305f\u306f\u30b3\u30fc\u30c9\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044", None))
        self.updateStockListButton.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30c8\u30c3\u30af\u30ea\u30b9\u30c8\u306e\u66f4\u65b0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6642\u9593\u7bc4\u56f2\uff1a", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-M-d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.endDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-M-d", None))
        self.getHistoryInfoButton.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u5f97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u6b74\u53f2\u7684\u540d\u8a00\uff1f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u30ea\u30a2\u30eb\u30bf\u30a4\u30e0\u5f15\u7528", None))
    # retranslateUi

