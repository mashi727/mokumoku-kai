'''
Object Orientedな記法
'''

import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import  NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import math
import numpy as np

from my_modules.prop_func import *

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)


    def f(x,y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

    def draw_graph(self):
        # 図、座標軸を明示的に定義して、グラフを描画
        MplCanvas.fig = plt.figure()
        canvas = FigureCanvas(MplCanvas.fig)
        self.layout.addWidget(canvas)

        ################################
        #         1つ目のグラフ
        ################################    
        # 等高線
        ax1 = MplCanvas.fig.add_subplot(211)
        n = 256
        x = np.linspace(-3, 3, n)
        y = np.linspace(-3, 3, n)
        X,Y = np.meshgrid(x, y)

        ax1.contourf(X, Y, DrawGraph.f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
        C = ax1.contour(X, Y, DrawGraph.f(X, Y), 8, colors='black')
        ax1.clabel(C, inline=1, fontsize=10)
        ax1.set_title('contour')

        ################################
        #         2つ目のグラフ
        ################################
        ax2 = MplCanvas.fig.add_subplot(212)
        ax2.plot([1, 4, 3, 6, 5, 9])
        ax2.grid(True)
        ax2.set_ylabel('values')
        ax2.set_title('points')
        