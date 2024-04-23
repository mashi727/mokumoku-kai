'''
plotwidgetとopenglの同時表示
（glwへのopenglの表示は不可）

Lissajous Curve と適当な3dグラフ
'''
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
import pyqtgraph.opengl as gl

# setpropは、それぞれのモデル側から読み込む（docstring的にオイシイから）
from my_modules.prop_func import *

from PySide6 import QtCore
import numpy as np


# 3D表示なので、openglが必要
import pyqtgraph as pg

from dataclasses import dataclass
@dataclass
class PlotData():
    i : int = 0
    samplingNum : int = 300
    m : int = 5
    n : int = 8


class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    def draw_graph(self):
        area = DockArea()
        self.layout.addWidget(area)  

        d1 = Dock("lissa animation", size=(1, 1))
        area.addDock(d1) ## place d1

        win = pg.GraphicsLayoutWidget()
        win.setWindowTitle('Awesome Graph')
        d1.addWidget(win)
    


        p1 = DrawGraph.set_graph_ui(self, win)
        
        #p1 = DrawGraph.set_graph_ui()
        self.p1 = p1

        def update():
            if PlotData.i < PlotData.samplingNum - 1:
                x,y = DrawGraph.lissajous(PlotData.i)
                self.p1.plot([x],[y],
                    clear=True,
                    pen='#0F0',
                    alpha=1,
                    symbolBrush='#0F0',
                    symbolSize=10,
                    name=self.fontCssLegend + '<p>Plotポイント</p>'
                    )
                PlotData.i  += 1
            else:
                PlotData.i = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(update)
        self.timer.start(50)

    def lissajous(self):
        t = np.linspace(-np.pi,np.pi,PlotData.samplingNum)
        x = np.sin(PlotData.m * t[PlotData.i])
        y = np.sin(PlotData.n * t[PlotData.i])
        return x, y



    
    def set_graph_ui(self, win):
        """_summary_

        Returns:
            _type_: _description_
            軸やレジェンドなどを設定してGraphオブジェクトを返す
        """
        setprop = lambda x: (x.setAutoVisible(y=True),
                             x.enableAutoRange(False),
                             x.showAxis('right'),
                             x.showAxis('left'),
                             x.showAxis('top'),
                             x.getAxis('top').setHeight(50),
                             x.getAxis('bottom').setHeight(50),
                             x.getAxis('right').setWidth(50),
                             x.getAxis('left').setWidth(50),
                             x.showGrid(x=True, y=True, alpha = 1),
                             x.setAutoVisible(y=True),
                             x.setXRange(-1, 1, padding=0.1),
                             x.setYRange(-1, 1, padding=0.1),
                             x.addLegend(offset=(10,10)),
                             x.setTitle('<font size=\'14\' color=\'#FFFFFF\'>'+ 'Lissajous' +'</font>'),
                             x.setLabel('left'  , text='y', units='', **styles),
                             x.setLabel('bottom', text='x', units='', **styles),
                             x.setLabel('right'  , text='y', units='', **styles),
                             x.setLabel('top', text='x', units='', **styles),
                             )
        '''
        Macの場合、フォントはFont Bookの正式名称の下にある「ファミリー」を使用する。
        ときどき、non-localizedといわれる以下のメッセージが出力される。

        qt.qpa.fonts: Populating font family aliases took 512 ms. Replace uses of "ヒラギノ角ゴシック"
        with its non-localized name "Hiragino Sans" to avoid this cost.

        この場合は、指示通りにHiragino Sansを設定すれば問題はない。
        '''
        self.fontCssLegend = '<style type="text/css"> p {font-family: Helvetica, HackGen35 Console NFJ; font-size: 15pt; color: "#ffffff"} </style>'
        styles = {'color':'white',
                  'font-size':'30px',
                  'font-style':'bold',
                  'font-family': 'Helvetica, HackGen35 Console NFJ'
                  }

        p1 = win.addPlot()
        setprop(p1)
        return p1
