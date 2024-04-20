'''
plotwidgetとopenglの同時表示
（glwへのopenglの表示は不可）

Lissajous Curve と適当な3dグラフ
'''
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea

# setpropは、それぞれのモデル側から読み込む（docstring的にオイシイから）
from my_modules.prop_func import *

# 3D表示なので、openglが必要
from pyqtgraph.opengl import GLViewWidget
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np


class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    def draw_graph(self):
        area = DockArea()
        self.layout.addWidget(area)  


        d1 = Dock("Doc1", size=(1, 1))
        area.addDock(d1) ## place d1

        graphics_w = pg.GraphicsLayoutWidget()
        graphics_w.setWindowTitle('Lissa.')

        # データの生成
        def generate_xy():
            # tag::plot data:
            import numpy as np

            m = 4
            n = 6
            t = np.linspace(-np.pi,np.pi,200)
            x = np.sin(m * t)
            y = np.sin(n * t)
            return x, y
        
        x, y = generate_xy()

        d1.addWidget(graphics_w)
        p1 = graphics_w.addPlot()
        p1.plot(x=x,
                y=y,
                #name= self.fontCssLegend +'<p>Legend test</p>',
                pen='#0a0',
                symbolBrush='#0f0',
                symbolPen='w',
                symbol='o',
                symbolSize=14,
                )

        # 2つ目のグラフ
        d2 = Dock("Dock2", size=(1, 1))
        area.addDock(d2) ## place d1 at left edge of dock area (it will fill 
        openGLWidget = GLViewWidget()
        viewt = openGLWidget
        viewt.opts['distance'] = 50
        d2.addWidget(viewt)

        n = 51
        y = np.linspace(-10,10,n)
        x = np.linspace(-10,10,100)
        for i in range(n):
            yi = y[i]
            d = np.hypot(x, yi)
            z = 10 * np.cos(d) / (d+1)
            pts = np.column_stack([x, np.full_like(x, yi), z])
            p2 = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i,len(y)*1.3)), width=(i+1)/10., antialias=True)
            viewt.addItem(p2)

