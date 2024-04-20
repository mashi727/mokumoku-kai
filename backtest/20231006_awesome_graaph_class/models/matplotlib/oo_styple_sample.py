'''
Object Orientedな記法
'''
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

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
        t = np.arange(0.0, 1.0, 0.01)

        # 図、座標軸を明示的に定義して、折れ線グラフを描画
        MplCanvas.fig = plt.figure()
        canvas = FigureCanvasQTAgg(MplCanvas.fig)
        self.layout.addWidget(canvas)

        ax1 = MplCanvas.fig.add_subplot(211)
        ax1.plot(t, np.sin(2*np.pi*t))
        ax1.grid(True)
        ax1.set_ylim( (-2,2) )
        ax1.set_xlabel('t')
        ax1.set_ylabel('f(t)')
        ax1.set_title('sin function')

        ax2 = MplCanvas.fig.add_subplot(212)
        ax2.plot(t, np.cos(2*np.pi*t))
        ax2.grid(True)
        ax2.set_ylim( (-2,2) )
        ax2.set_xlabel('t')
        ax2.set_ylabel('f(t)')
        ax2.set_title('cos function')

