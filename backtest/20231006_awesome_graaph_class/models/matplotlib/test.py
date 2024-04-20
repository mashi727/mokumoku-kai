'''
Matplotlibをpyqtgraphの中に埋め込む。
参考にしたサイトは、こちら。

https://www.pythonguis.com/tutorials/pyside6-plotting-matplotlib/

てはじめに、最も簡単なグラフを描いてみる。

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

from dataclasses import dataclass
@dataclass
class Data:
    degree : float = 45
    u : float = 40
    g : float = 9.8
    theta : float = math.radians(degree)
    t_flight : float = 2 * u * math.sin(theta) / g



class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    # 定義域(x: 距離)を算出する。
    def frange(start, final, interval):
        numbers = []
        while start < final:
            numbers.append(start)
            start = start + interval
        return numbers

    # 値域(y: 高さ)を算出する。
    def draw_trajectory(u, theta, g, intervals):
        # list of x and y co-ordinates
        x = []
        y = []
        for t in intervals:
            x.append(u*math.cos(theta)*t)
            y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        return x, y


    # Time of flight
    # find time intervals

    def draw_graph(self):
        sc = MplCanvas(width=5, height=4, dpi=300)
        toolbar = NavigationToolbar(sc)
        self.layout.addWidget(toolbar)
        self.layout.addWidget(sc)
        toolbar = NavigationToolbar(sc)
        
        # ここから
        intervals = DrawGraph.frange(0, Data.t_flight, 0.05)
        x, y = DrawGraph.draw_trajectory(Data.u, Data.theta, Data.g, intervals)
        sc.axes.plot(x, y)



