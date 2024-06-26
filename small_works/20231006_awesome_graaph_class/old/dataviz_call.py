import os
import sys
from PySide6 import QtCore, QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton
from PySide6.QtWidgets import QTableView
import dash
from dash import dcc
from dash import html
import sqlite3


import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


import random
import plotly

import io
import folium
from folium import plugins

sys.setrecursionlimit(2000)

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
from pyqtgraph.opengl import GLViewWidget


# Key Event
from PySide6.QtCore import Qt

# 自作のライブラリ
from my_modules.syntax_highlighter import *
from my_modules.finance_lib import *
# setpropは、それぞれのモデル側から読み込む（docstring的にオイシイから）
from my_modules.prop_func import *
from my_modules.map import *

import numpy as np
import pandas as pd
import math

def test_deco(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

os.environ["PYSIDE_DESIGNER_PLUGINS"]="."
os.environ["QT_LOGGING_RULES"]='*.debug=false;qt.pysideplugin=false'
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)


"""
This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with 
the left/right mouse buttons. Right click on any plot to show a context menu.
"""
import numpy as np
import pyqtgraph as pg
import pandas as pd
import math
import matplotlib.pyplot as plt


import pyqtgraph as pg

fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}
fontCss["color"] = '#fff' 

# DockLabelをグレーにする
# http://fatbald.seesaa.net/article/451667700.html
from pyqtgraph.dockarea.Dock import DockLabel
def updateStyle(self):
    self.setStyleSheet("DockLabel { color: #FFF; background-color: #444; font-size:20pt}")
setattr(DockLabel, 'updateStyle', updateStyle)


# tag::model[]

class FileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, path=None):
        super().__init__()

        # common data path
        self.path_data = './data/'

        # for amalytical visualization
        self.path_analytical_viz = './models/analyticalViz'
        # Nodata

        # for finance
        self.path_finance = './models/Finance'
        self.path_finance_data = './data/finance'

        # for Prototype
        self.path_prototype = './models/prototype'
        # data path -> common

        # for my data visualization
        self.path_my_dataviz = './models/myDataViz'
        # data path -> common


        # for matplotlib
        self.path_matplt = './models/matplotlib'
        # data path -> common
 
        # for DASH
        self.path_dash = './models/dash'
        # data path -> common





# end::model[]

from dataclasses import dataclass
@dataclass
class FilePath:
    filename: str
    data_filename: str

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        # QUiLoaderで.uiファイルを読み込む
        self.Ui_MainWindow = QtUiTools.QUiLoader().load("./dataviz_ui3.ui")
        self.Ui_MainWindow.setWindowTitle("Awesome Visualization TOOL")
        self.Ui_MainWindow.setGeometry(50, 50, 2400, 1600) # WQXGA (Wide-QXGA)


        # ボタン操作
        self.Ui_MainWindow.btnFin.clicked.connect(lambda:self.pltFin())
        self.Ui_MainWindow.btnFin.setStyleSheet("QPushButton:checked{background-color: rgb(100, 200, 0)}")
        self.Ui_MainWindow.btnAnalytic.clicked.connect(lambda:self.pltAnalytic())
        self.Ui_MainWindow.btnAnalytic.setStyleSheet("QPushButton:checked{background-color: rgb(100, 200, 0)}")
        self.Ui_MainWindow.btnMyData.clicked.connect(lambda:self.pltMyData())
        self.Ui_MainWindow.btnMyData.setStyleSheet("QPushButton:checked{background-color: rgb(100, 200, 0)}")
        self.Ui_MainWindow.btnProtoType.clicked.connect(lambda:self.pltProtoType())
        self.Ui_MainWindow.btnProtoType.setStyleSheet("QPushButton:checked{background-color: rgb(100, 200, 0)}")
        self.Ui_MainWindow.btnMatplt.clicked.connect(lambda:self.pltMatplt())
        self.Ui_MainWindow.btnMatplt.setStyleSheet("QPushButton:checked{background-color: rgb(100, 200, 0)}")
        self.Ui_MainWindow.btnDash.clicked.connect(lambda:self.pltDash())
        self.Ui_MainWindow.btnDash.setStyleSheet("QPushButton:checked{background-color: rgb(100, 200, 0)}")

        self.Ui_MainWindow.plotButton.clicked.connect(lambda:self.load_model())


        # codeView関連のイベント
        hl = PythonHighlighter(self.Ui_MainWindow.codeView.document())
        self.Ui_MainWindow.codeView.installEventFilter(self)
        self.Ui_MainWindow.codeView.cursorPositionChanged.connect(self.count_line_number)
        self.Ui_MainWindow.codeView.textChanged.connect(self.auto_save_file)

        layout = QVBoxLayout()
        self.Ui_MainWindow.widget.setLayout(layout)
        self.layout = layout

    def pltProtoType(self):
        self.file_system_model = FileSystemModel()
        self.file_system_model.setRootPath(self.file_system_model.path_prototype)
        self.file_system_model.setNameFilters(['*.py','*.fo'])
        self.file_system_model.setNameFilterDisables(False)

        self.file_system_model_for_data = FileSystemModel()
        self.file_system_model_for_data.setRootPath(self.file_system_model_for_data.path_data)
        self.file_system_model_for_data.setNameFilters(['*.csv'])
        self.file_system_model_for_data.setNameFilterDisables(False)

        self.file_system_view = self.Ui_MainWindow.treeView
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.file_system_model.path_prototype))
        self.file_system_view.setColumnWidth(0,300)

        self.file_system_view_for_data = self.Ui_MainWindow.treeViewData
        self.file_system_view_for_data.setModel(self.file_system_model_for_data)
        self.file_system_view_for_data.setRootIndex(self.file_system_model_for_data.index(self.file_system_model_for_data.path_data))
        self.file_system_view_for_data.setColumnWidth(0,300)

        self.file_system_view.clicked.connect(self.getFileContents)
        self.file_system_view_for_data.clicked.connect(self.getFileName)

    def pltMyData(self):
        self.file_system_model = FileSystemModel()
        self.file_system_model.setRootPath(self.file_system_model.path_my_dataviz)
        self.file_system_model.setNameFilters(['*.py'])
        self.file_system_model.setNameFilterDisables(False)

        self.file_system_model_for_data = FileSystemModel()
        self.file_system_model_for_data.setRootPath(self.file_system_model_for_data.path_data)
        self.file_system_model_for_data.setNameFilters(['*.csv','*.db'])
        self.file_system_model_for_data.setNameFilterDisables(False)

        self.file_system_view = self.Ui_MainWindow.treeView
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.file_system_model.path_my_dataviz))
        self.file_system_view.setColumnWidth(0,300)

        self.file_system_view_for_data = self.Ui_MainWindow.treeViewData
        self.file_system_view_for_data.setModel(self.file_system_model_for_data)
        self.file_system_view_for_data.setRootIndex(self.file_system_model_for_data.index(self.file_system_model_for_data.path_data))
        self.file_system_view_for_data.setColumnWidth(0,300)

        self.file_system_view.clicked.connect(self.getFileContents)
        self.file_system_view_for_data.clicked.connect(self.getFileName)
        self.file_system_view_for_data.doubleClicked.connect(lambda:self.load_model())



    def pltAnalytic(self):
        self.file_system_model = FileSystemModel()
        self.file_system_model.setRootPath(self.file_system_model.path_analytical_viz)
        self.file_system_model.setNameFilters(['*.py'])
        self.file_system_model.setNameFilterDisables(False)

        self.file_system_model_for_data = FileSystemModel()
        self.file_system_model_for_data.setRootPath(self.file_system_model_for_data.path_data)
        self.file_system_model_for_data.setNameFilters(['*.none'])
        self.file_system_model_for_data.setNameFilterDisables(False)

        self.file_system_view = self.Ui_MainWindow.treeView
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.file_system_model.path_analytical_viz))
        self.file_system_view.setColumnWidth(0,300)

        self.file_system_view_for_data = self.Ui_MainWindow.treeViewData
        self.file_system_view_for_data.setModel(self.file_system_model_for_data)
        self.file_system_view_for_data.setRootIndex(self.file_system_model_for_data.index(self.file_system_model_for_data.path_data))
        self.file_system_view_for_data.setColumnWidth(0,300)

        self.file_system_view.clicked.connect(self.getFileContents)
        self.file_system_view_for_data.clicked.connect(self.getFileName)

    def pltFin(self):
        self.file_system_model = FileSystemModel()
        self.file_system_model.setRootPath(self.file_system_model.path_finance)
        self.file_system_model.setNameFilters(['*.py'])
        self.file_system_model.setNameFilterDisables(False)

        self.file_system_model_for_data = FileSystemModel()
        self.file_system_model_for_data.setRootPath(self.file_system_model_for_data.path_finance_data)
        self.file_system_model_for_data.setNameFilters(['*.csv'])
        self.file_system_model_for_data.setNameFilterDisables(False)

        self.file_system_view = self.Ui_MainWindow.treeView
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.file_system_model.path_finance))
        self.file_system_view.setColumnWidth(0,300)

        self.file_system_view_for_data = self.Ui_MainWindow.treeViewData
        self.file_system_view_for_data.setModel(self.file_system_model_for_data)
        self.file_system_view_for_data.setRootIndex(self.file_system_model_for_data.index(self.file_system_model_for_data.path_finance_data))
        self.file_system_view_for_data.setColumnWidth(0,300)

        self.file_system_view.clicked.connect(self.getFileContents)
        self.file_system_view_for_data.clicked.connect(self.getFileName)

    def pltMatplt(self):
        self.file_system_model = FileSystemModel()
        self.file_system_model.setRootPath(self.file_system_model.path_matplt)
        self.file_system_model.setNameFilters(['*.py'])
        self.file_system_model.setNameFilterDisables(False)

        self.file_system_model_for_data = FileSystemModel()
        self.file_system_model_for_data.setRootPath(self.file_system_model_for_data.path_data)
        self.file_system_model_for_data.setNameFilters(['*.none'])
        self.file_system_model_for_data.setNameFilterDisables(False)

        self.file_system_view = self.Ui_MainWindow.treeView
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.file_system_model.path_matplt))
        self.file_system_view.setColumnWidth(0,300)

        self.file_system_view_for_data = self.Ui_MainWindow.treeViewData
        self.file_system_view_for_data.setModel(self.file_system_model_for_data)
        self.file_system_view_for_data.setRootIndex(self.file_system_model_for_data.index(self.file_system_model_for_data.path_data))
        self.file_system_view_for_data.setColumnWidth(0,300)

        self.file_system_view.clicked.connect(self.getFileContents)
        self.file_system_view_for_data.clicked.connect(self.getFileName)

    def pltDash(self):
        self.file_system_model = FileSystemModel()
        self.file_system_model.setRootPath(self.file_system_model.path_dash)
        self.file_system_model.setNameFilters(['*.py'])
        self.file_system_model.setNameFilterDisables(False)

        self.file_system_model_for_data = FileSystemModel()
        self.file_system_model_for_data.setRootPath(self.file_system_model_for_data.path_data)
        self.file_system_model_for_data.setNameFilters(['*.csv'])
        self.file_system_model_for_data.setNameFilterDisables(False)

        self.file_system_view = self.Ui_MainWindow.treeView
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.file_system_model.path_dash))
        self.file_system_view.setColumnWidth(0,300)

        self.file_system_view_for_data = self.Ui_MainWindow.treeViewData
        self.file_system_view_for_data.setModel(self.file_system_model_for_data)
        self.file_system_view_for_data.setRootIndex(self.file_system_model_for_data.index(self.file_system_model_for_data.path_data))
        self.file_system_view_for_data.setColumnWidth(0,300)

        self.file_system_view.clicked.connect(self.getFileContents)
        self.file_system_view_for_data.clicked.connect(self.getFileName)


    def count_line_number(self):
        line_num = self.Ui_MainWindow.codeView.textCursor().blockNumber()
        line_num = str(line_num + 1) # 0行目から数え始めなので、+1。
        self.Ui_MainWindow.lineNum.setText(line_num)
        # self.Ui_MainWindow.codeView.textChanged.textCursor().position()


    def getFileContents(self, index):
        '''
        クリックしたファイルの中身をtextに格納する。
        '''
        try:
            filepath = []
            indexItem = self.file_system_model.index(index.row(), 0, index.parent())
            if os.path.isfile(self.file_system_model.filePath(indexItem)):
                filepath.insert(0,self.file_system_model.filePath(indexItem))
                FilePath.filename = filepath[0]
                text = open(FilePath.filename, encoding='utf-8').read()
                self.Ui_MainWindow.codeView.setPlainText(text)
            else:
                pass

        except AttributeError as e:
            pass

    def load_model(self):
        self.clearLayout(self.layout)
        if self.Ui_MainWindow.btnDash.isChecked() == True:
            import subprocess
            import time
            import sys
            import psutil


            def destroyed(proc_pid):
                process = psutil.Process(proc_pid)
                for proc in process.children(recursive=True):
                    proc.kill()
                process.kill()
            proc = subprocess.Popen(['python' ,FilePath.filename])
            time.sleep(1)
            proc.kill()
            #destroyed(proc.pid)

            '''
            # as of Oct.5.'23
            # プロセスのkillが怪しかったけど、動いていたコード。
            self.proc = subprocess.Popen(['python', FilePath.filename])
            time.sleep(1)
            self.proc.kill()
            '''
            #try:
            #    proc.wait(timeout=1)
            #except subprocess.TimeoutExpired:
            #    destroyed(proc.pid)
            #command = ["python", FilePath.filename]
            #res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            addDashCode='''
import dash
from dash import dcc
from dash import html

def draw_map(self, area):
    # tag::visualize plot data:
    # 表示領域の確保
    d1 = Dock("Map", size=(1, 2))
    area.addDock(d1) ## place d1 at left edge of dock area
    # Widgetのインスタンス
    from PySide6.QtWebEngineWidgets import QWebEngineView
    widget = QWebEngineView()
    d1.addWidget(widget)
    widget.setUrl('http://127.0.0.1:8050')
    d1.addWidget(widget)


from PySide6.QtWebEngineWidgets import QWebEngineView
area = DockArea()
# DockAreaをlayout内に配置する。
self.layout.addWidget(area)



from types import MethodType
MainWindow.draw_map = MethodType(draw_map, MainWindow)
self.draw_map(area)
'''
            exec(addDashCode)
        else:
            #print(self.Ui_MainWindow.btnDash.isChecked())
            try:
                self.timer.stop()
            except Exception as e:
                pass
            model_code = self.Ui_MainWindow.codeView.toPlainText()
            if FilePath.filename.endswith('.py'):
                #print("python!!")
                exec(model_code)
            elif FilePath.filename.endswith('.fo'):
                # QtWebEngineWidgetsを読み込んで、openglのグラフを描こうとすると
                # エラーになるよ。
                '''
                OpenGL.error.GLError: GLError(
                err = 1282,
                description = b'invalid operation',
                baseOperation = glMatrixMode,
                cArguments = (GL_PROJECTION,)
                '''
                from PySide6.QtWebEngineWidgets import QWebEngineView
                addCode='''
self.widget2 = QWebEngineView()
self.layout.addWidget(self.widget2)
data = io.BytesIO()
m.save(data, close_file=False)
self.widget2.setHtml(data.getvalue().decode())
'''
                exec(model_code+addCode)
            else:
                pass

    def getFileName(self, index):
        '''
        クリックしたファイルの中身をtextに格納する。
        '''
        try:
            filepath = []
            indexItem = self.file_system_model_for_data.index(index.row(), 0, index.parent())
            if os.path.isfile(self.file_system_model_for_data.filePath(indexItem)):
                filepath.insert(0,self.file_system_model_for_data.filePath(indexItem))
                FilePath.data_filename = filepath[0]
            else:
                pass

        except AttributeError as e:
            pass

    def auto_save_file(self):
        with open(FilePath.filename, encoding='utf-8', mode='w') as f:
            f.write(self.Ui_MainWindow.codeView.toPlainText())


    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            childWidget = child.widget()
            if childWidget:
                childWidget.setParent(None)
                childWidget.deleteLater()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.Ui_MainWindow.codeView:
            if event.key() == Qt.Key_Tab and self.Ui_MainWindow.codeView.hasFocus():
                # Special tab handling
                tc = self.Ui_MainWindow.codeView.textCursor()
                tc.insertText("    ")
                return True
            else:
                return False
        return False


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