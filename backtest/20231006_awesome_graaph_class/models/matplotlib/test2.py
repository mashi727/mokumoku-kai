'''
Matplotlibをpyqtgraphの中に埋め込む。
参考にしたサイトは、こちら。

https://www.pythonguis.com/tutorials/pyside6-plotting-matplotlib/

データの生成方法が異なるだけで、やっていることはほぼ同じ。

'''
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import math
from my_modules.prop_func import *


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    def draw_graph(self):
        sc = MplCanvas(width=5, height=4, dpi=300)
        toolbar = NavigationToolbar(sc)
        self.layout.addWidget(toolbar)
        self.layout.addWidget(sc)
        # Create toolbar, passing canvas as first parameter, parent (self, the MainWindow) as second.
        # データ生成
        import pandas as pd
        df = pd.DataFrame([[0, 10], [5, 15], [2, 20], [15, 25], [4, 10],], columns=["A", "B"])
        
        # plot the pandas DataFrame, passing in the
        # matplotlib Canvas axes.
        df.plot(ax=sc.axes)


