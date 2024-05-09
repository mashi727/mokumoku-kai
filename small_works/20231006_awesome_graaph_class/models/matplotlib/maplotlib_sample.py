'''
Object Orientedな記法

fig, ax1 = plt.subplots()
で受けて、プロットする方法が不明。
2023.10.07時点で未完成
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
        self.axes = fig.add_subplot()
        super(MplCanvas).__init__(fig)

class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    def draw_graph(self):
        fig = plt.figure()
        #MplCanvas.fig = plt.figure()
        # 図、座標軸を明示的に定義して、グラフを描画
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)

        # test data
        data = np.array([0.7,0.7,0.7,0.8,0.9,0.9,1.5,1.5,1.5,1.5])        
        fig, ax1 = plt.subplots()
        bins = np.arange(0.6, 1.62, 0.02)
        n1, bins1, patches1 = ax1.hist(data, bins, alpha=0.6, density=False, cumulative=False)

        '''
        参考にしたページ
        https://stackoverflow.com/questions/53157230/embed-a-matplotlib-plot-in-a-pyqt5-gui
        '''