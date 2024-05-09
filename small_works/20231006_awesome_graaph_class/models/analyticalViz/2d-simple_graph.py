'''
for xy plot
Draw the trajectory of a body in projectile motion
'''
import math
from my_modules.prop_func import *

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

    def draw_graph(self):
        area = DockArea()
        self.layout.addWidget(area)  

        d1 = Dock("pyqtgraph example: Basic Plots", size=(1, 1))
        area.addDock(d1) ## place d1

        win = pg.GraphicsLayoutWidget()
        win.setWindowTitle('Awesome Graph')
        d1.addWidget(win)
        name_of_xaxis = 'x-coordinate'
        name_of_yaxis = 'y-coordinate'

        p1 = win.addPlot()
        x, y = DrawGraph.draw_trajectory(Data.u, Data.theta, Data.g)
        setprop(p1, name_of_xaxis, name_of_yaxis)
        p1.plot(x=x,
                y=y,
                pen='#0a0',
                symbolBrush='#0f0',
                symbolPen='w',
                symbol='o',
                symbolSize=14,
                )

    # 定義域(x: 距離)を算出する。
    def frange(start, final, interval):
        numbers = []
        while start < final:
            numbers.append(start)
            start = start + interval
        return numbers

    # 値域(y: 高さ)を算出する。
    def draw_trajectory(u, theta, g):
        # list of x and y co-ordinates
        intervals = DrawGraph.frange(0, Data.t_flight, 0.05)
        x = []
        y = []
        for t in intervals:
            x.append(u*math.cos(theta)*t)
            y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        return x, y


