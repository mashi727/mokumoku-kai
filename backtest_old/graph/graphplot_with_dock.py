import pyqtgraph as pg
from pyqtgraph.dockarea import *
import numpy as np
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from datetime import datetime 
    

class TimeAxisItem(pg.AxisItem):
    '''
    時間をを表示する。
    UNIX時間を以下の様にJSTに変換する。
    pd.to_datetime(df['date']).dt.tz_localize(tz='Asia/Tokyo')
    self.dt = df.index.astype(np.int64)//10**9
    PlotWidgetの中で、以下の用に使用する
    pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
    '''
    def __init__(self, *args, **kwargs):
        super(TimeAxisItem, self).__init__(*args, **kwargs)
    
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(v).strftime('%Y %m/%d %H:%M') for v in values]
        '''
        フォーマットの例
        %Y：西暦 ( 4桁) の 10 進表記を表します。
        %m：0埋めした10進数で表記した月。
        %d：0埋めした10進数で表記した月中の日にち。
        %H：0埋めした10進数で表記した時 (24時間表記)。
        %I：0埋めした10進数で表記した時 (12時間表記)。
        %M：0埋めした10進数で表記した分。
        %S：0埋めした10進数で表記した秒。
        %b：ロケールの月名を短縮形で表示します。
        %B：ロケールの月名を表示します。
        
        詳細はこちら。
        https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-behavior
        '''


class TestCandle(pg.GraphicsObject):
    def __init__(self, df):
        super(TestCandle, self).__init__()
        # https://deepage.net/features/numpy-cr.html
        # np._c 多次元配列の結合を行う。
        self.data = np.c_[df.index.view(np.int64)//10**9, df.values]
        print(df.values)
        self.picture = QPicture()
        self.generatePicture(self.data)
    
    def generatePicture(self, data):
        clr_up, clr_down, clr_line = (0,128,0), (128,0,0), (128,128,128)
        lp = pg.mkPen(clr_line)
        up = pg.mkPen(clr_up)
        dp = pg.mkPen(clr_down)
        brush_up = pg.mkBrush(clr_up)
        brush_dn = pg.mkBrush(clr_down)
        self.p = QPainter(self.picture)
        self.p.setPen(lp)
        w = (data[-1][0]-data[-2][0]) / 3
        for (t, o, h, l, c) in data:
            self.p.setPen(lp)
            if h!=l:
                self.p.drawLine(QPointF(t, l), QPointF(t, h)) # line
            self.p.setPen(up if c>o else dp) # コメントアウトすればふちが有るかんじのローソクになる
            self.p.setBrush(brush_up if c>o else brush_dn)
            self.p.drawRect(QRectF(t-w, o, w*2, c-o)) # w -> 1にしてみたら、ローソクの足が真ん中にいかない。
            # self.p.drawRect(QRectF(t-w, o, w*2, c-o)) # candle body
        self.p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        return QRectF(self.picture.boundingRect())


from pyqtgraph import QtCore, QtGui

## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see QGraphicsItem documentation)
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, df):
        data = np.c_[df.index.view(np.int64)//10**9, df.values]
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()
    
    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('#fff9')) # ヒゲの色
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('#f00'))
            else:
                p.setBrush(pg.mkBrush('#0f0'))
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())