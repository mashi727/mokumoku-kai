'''
plotwidgetとopenglの同時表示
（glwへのopenglの表示は不可）

Lissajous Curve と適当な3dグラフ
'''
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
import pyqtgraph.opengl as gl


from PySide6 import QtCore

# setpropは、それぞれのモデル側から読み込む（docstring的にオイシイから）
from my_modules.prop_func import *

# 3D表示なので、openglが必要
from pyqtgraph.opengl import GLViewWidget
import pyqtgraph as pg
#area = DockArea()
# DockAreaをlayout内に配置する。
#self.layout.addWidget(area)

import numpy as np

class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    def draw_graph(self):
        area = DockArea()
        self.layout.addWidget(area)

        d1 = Dock("Dock2", size=(1, 1))
        area.addDock(d1) ## place d1 at left edge of dock area (it will fill 
        ## Create a GL View widget to display data
        w = gl.GLViewWidget()
        w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
        w.setCameraPosition(distance=27)
        d1.addWidget(w)

        ## Add a grid to the view
        g = gl.GLGridItem()
        g.scale(2,2,1)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)

        ## Animated example
        ## compute surface vertex data
        cols = 90
        rows = 100
        x = np.linspace(-8, 8, cols+1).reshape(cols+1,1)
        y = np.linspace(-8, 8, rows+1).reshape(1,rows+1)
        d = (x**2 + y**2) * 0.1
        d1 = d ** 0.5 + 0.1

        ## precompute height values for all frames
        phi = np.arange(0, np.pi*2, np.pi/20.)
        z = np.sin(d[np.newaxis,...] + phi.reshape(phi.shape[0], 1, 1)) / d1[np.newaxis,...]

        ## create a surface plot, tell it to use the 'heightColor' shader
        ## since this does not require normal vectors to render (thus we 
        ## can set computeNormals=False to save time when the mesh updates)
        p4 = gl.GLSurfacePlotItem(x=x[:,0], y = y[0,:], shader='heightColor', computeNormals=False, smooth=False)
        p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
        p4.translate(0, 0, 0) # 位置のオフセット
        w.addItem(p4)

        index = 0
        self.index = index
        def update():
            #global p4, z, index
            self.index -= 1
            p4.setData(z=z[self.index%z.shape[0]])
            
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(update)
        self.timer.start(30)

    def __del__(self):
        print('Goog Bye!!')