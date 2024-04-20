
import os
import sys
from PySide6 import QtCore, QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton
from PySide6.QtWidgets import QTableView

from PySide6.QtGui import QFont



from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

import platform
sys.setrecursionlimit(2000)

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
from pyqtgraph.opengl import GLViewWidget




os.environ["PYSIDE_DESIGNER_PLUGINS"]="."
os.environ["QT_LOGGING_RULES"]='*.debug=false;qt.pysideplugin=false'
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        # QUiLoaderで.uiファイルを読み込む
        self.Ui_MainWindow = QtUiTools.QUiLoader().load("./stockPlotUi.ui")
        self.Ui_MainWindow.setWindowTitle("Awesome Visualization TOOL")
        self.Ui_MainWindow.setGeometry(50, 50, 1920, 1080) # WQXGA (Wide-QXGA)

        font = QFont()
        font1 = QFont()
        osname = platform.system()
        if osname == 'Darwin':
            font.setPointSize(12)
            font1.setPointSize(12)
            #self.Ui_MainWindow.btnMyData.setFont(font)

            self.Ui_MainWindow.label_8.setFont(font)
            self.Ui_MainWindow.groupBox_2.setFont(font1)
            self.Ui_MainWindow.label_10.setFont(font1)
            self.Ui_MainWindow.lineEdit.setFont(font1)
            self.Ui_MainWindow.label_3.setFont(font1)
            self.Ui_MainWindow.lineEdit_TickSyml.setFont(font1)
            self.Ui_MainWindow.label_22.setFont(font1)
            self.Ui_MainWindow.SB_sma_short.setFont(font1)
            self.Ui_MainWindow.label_24.setFont(font1)
            self.Ui_MainWindow.SB_sma_med.setFont(font1)
            self.Ui_MainWindow.label_25.setFont(font1)
            self.Ui_MainWindow.SB_sma_long.setFont(font1)
            self.Ui_MainWindow.label_26.setFont(font1)
            self.Ui_MainWindow.comboBox.setFont(font1)
            self.Ui_MainWindow.tableView.setFont(font1)
            self.Ui_MainWindow.label_5.setFont(font)
            self.Ui_MainWindow.tabWidget_2.setFont(font1)
            self.Ui_MainWindow.label_45.setFont(font1)
            self.Ui_MainWindow.label_46.setFont(font1)
            self.Ui_MainWindow.label_47.setFont(font1)
            self.Ui_MainWindow.label_38.setFont(font1)
            self.Ui_MainWindow.label_39.setFont(font1)
            self.Ui_MainWindow.label_40.setFont(font1)
            self.Ui_MainWindow.label_4.setFont(font1)
            self.Ui_MainWindow.lineEdit_start_region.setFont(font1)
            self.Ui_MainWindow.label_6.setFont(font1)
            self.Ui_MainWindow.tableView_backtesting.setFont(font1)
            self.Ui_MainWindow.label_7.setFont(font)
            self.Ui_MainWindow.tabWidget_3.setFont(font1)
            self.Ui_MainWindow.label_9.setFont(font1)
            self.Ui_MainWindow.lineEdit_start_region_2.setFont(font1)
            self.Ui_MainWindow.label_30.setFont(font1)
            self.Ui_MainWindow.tableView_backtesting_2.setFont(font1)
            self.Ui_MainWindow.quitButton.setFont(font1)


            print('Im in Mac!')
            #view.setFont(font)
            #self.listWData.setFont(font)
        elif osname == 'Windows':
            font.setPointSize(8)
            #view.setFont(font)
            #self.listWData.setFont(font)            
        else:
            FontFamily = 'FreeSerif'

def main():
    # Qt Applicationを作ります
    app = QApplication(sys.argv)
    # formを作成して表示します
    mainWin = MainWindow()
    mainWin.Ui_MainWindow.show()
    # Qtのメインループを開始します
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
