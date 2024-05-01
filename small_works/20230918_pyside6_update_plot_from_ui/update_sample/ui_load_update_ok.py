import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow


# ここからUI関連の記述
#from my_data_viz_ui_ui import Ui_MainWindow
import os
import sys
from PySide6 import QtCore, QtUiTools
from PySide6.QtWidgets import QVBoxLayout
os.environ["PYSIDE_DESIGNER_PLUGINS"]="."
os.environ["QT_LOGGING_RULES"]='*.debug=false;qt.pysideplugin=false'
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)




import pyqtgraph as pg

from PySide6.QtCore import QTimer
import time
import numpy as np

def setprop(plt):
    fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}
    plt.getAxis('left').setWidth(35),
    plt.showGrid(x=True, y=True, alpha=0.5),
    plt.getAxis('top').setLabel(**fontCss),
    plt.setAutoVisible(y=True),
    plt.showAxis('left'),
    plt.addLegend(offset=(0,0)) # legendには、nameが必要

def setprop_nogrid(plt):
    fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}
    plt.getAxis('left').setWidth(35),
    plt.getAxis('top').setLabel(**fontCss),
    plt.setAutoVisible(y=False),
    plt.setAutoVisible(x=False),
    plt.showAxis('left'),
    plt.addLegend(offset=(0,0)) # legendには、nameが必要


from dataclasses import dataclass
@dataclass
class DataClass:
    n_data: int = 1000
    # x : ndarray  np.random.normal(0.0, 1.0, self.n_data)
    test = lambda self, n: np.random.normal(0.0, 1.0, n)


class dataModel:
    def __init__(self):
        super().__init__()
        self.x = self.test(self.n_data)
        


class MainWindow(QMainWindow, DataClass, dataModel):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # QUiLoaderで.uiファイルを読み込む
        # uiをpyで読み込むと、self.setupUi(self)を実行し、Window関連の初期化を行う
        # 以下の処理にて、その代替を行う。
        self.Ui_MainWindow = QtUiTools.QUiLoader().load("./untitled.ui")
        self.Ui_MainWindow.setWindowTitle("MainWindow Title")
        self.init_ui()

        self.fontCssLegend = '<style type="text/css"> p {font-family: Arial, Meiryo; font-size: 14pt; color: "#FFF"} </style>'

        # tag::plot data: x, y values
        self.graphWidget = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.Ui_MainWindow.setCentralWidget(self.graphWidget)

        self.plot()
        model = dataModel
        print(model)

    def plot(self):
        pg.setConfigOptions(antialias=True)
        self.p1 = self.graphWidget.addPlot(row=0, col=0, colspan=1, title="real-time scatter plot") # PlotItem オブジェクト生成
        setprop_nogrid(self.p1)
        self.curve_update = self.p1.plot(pen='y')
        self.data_update = np.random.normal(size=(10,1000))
        self.ptr_update = 0
        self.p1.setYRange(-10, 10)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.update)
        self.timer2.start(50)

        # for update plot2

        self.p2 = self.graphWidget.addPlot(row=1, col=0, title="real-time scatter plot") # PlotItem オブジェクト生成
        setprop_nogrid(self.p2)

        self.curve = self.p2.plot(pen=None, symbol="o", symbolPen='b', symbolSize=10, symbolBrush='c') # PlotDataItemオブジェクト生成。pen=Noneで点のみ
        
        self.x = self.test(self.n_data)
        self.y = np.random.normal(0.0, 1.0, self.n_data)
        
        self.p2.setXRange(-10, 10)
        self.p2.setYRange(-10, 10)

        self.iter = 0
        self.pretime = time.time()
        fps = 60
        self.timer = QTimer()
        self.timer.timeout.connect(self.update2)
        self.timer.start(1/fps * 1000)
        
        self.graphWidget.nextRow()

        p3 = self.graphWidget.addPlot(row=0, col=1, title="Drawing with points")
        p3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')


        p4 = self.graphWidget.addPlot(row=1, col=1, title="Parametric, grid enabled")
        x = np.cos(np.linspace(0, 2*np.pi, 1000))
        y = np.sin(np.linspace(0, 4*np.pi, 1000))
        p4.plot(x, y)
        p4.showGrid(x=True, y=True)



    def init_ui(self):
        # self.Ui_MainWindowと明示しないと、表示されない。
        # あくまでも表示されるのは、self.Ui_MainWindowなのだ。　⇐ とても重要
        self.Ui_MainWindow.setGeometry(10, 10, 1280 , 780)
        
    def update(self):
        self.curve_update.setData(self.data_update[self.ptr_update%10])
        if self.ptr_update == 0:
            self.p1.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.ptr_update += 1


    def update2(self):
        # x, y座標を変更（アニメーション）
        self.x += np.random.normal(0.0, 0.1, self.n_data) + 0.01*np.cos(2*np.pi*self.iter/300)
        self.y += np.random.normal(0.0, 0.1, self.n_data) + 0.01*np.sin(2*np.pi*self.iter/120)
        
        if self.iter > 0:
            self.p2.enableAutoRange('xy', False) # x, y軸のスケール固定

        self.curve.setData(self.x, self.y)
        self.curve.setAlpha(0.5, False)
        
        
        self.curtime = time.time()
        fps = 1.0 / (self.curtime - self.pretime + 1e-16)
        self.p2.setTitle(f"fps: {fps:0.1f} Hz")
        self.pretime = self.curtime
        self.iter += 1


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.Ui_MainWindow.show()
    app.exec()

if __name__== '__main__':
    main()