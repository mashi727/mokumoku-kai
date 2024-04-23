'''
Matplotlibをpyqtgraphの中に埋め込む。
参考にしたサイトは、こちら。

https://www.pythonguis.com/tutorials/pyside6-plotting-matplotlib/

アニメーションにトライしてみる。
'''
import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)
        DrawGraph.x = []
        DrawGraph.y = []

    def update_plot():
        # Drop off the first y element, append a new one.
        DrawGraph.y = DrawGraph.y[1:] + [random.randint(0, 10)]
        DrawGraph.canvas.axes.cla()  # Clear the canvas.
        DrawGraph.canvas.axes.plot(DrawGraph.x, DrawGraph.y, 'r')
        # Trigger the canvas to update and redraw.
        DrawGraph.canvas.draw()

    def generate_xy():
        n_data = 50
        DrawGraph.x = list(range(n_data))
        DrawGraph.y = [random.randint(0, 10) for i in range(n_data)]
        return DrawGraph.x, DrawGraph.y

    def draw_graph(self):
        DrawGraph.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(DrawGraph.canvas)
        DrawGraph.x, DrawGraph.y = DrawGraph.generate_xy()
        DrawGraph.update_plot()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(DrawGraph.update_plot)
        self.timer.start()
