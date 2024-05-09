from PySide6 import QtCore
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

import numpy as np

try:
    apikey_path = './.alpha_vantage_apikey'
    with open(apikey_path) as f:
        API_KEY = f.readlines()[0]
except Exception:
    pass

from dataclasses import dataclass
@dataclass
class FinData:
    duration: str
    symbol: str
    region_disp: float

from datetime import datetime
class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(TimeAxisItem, self).__init__(*args, **kwargs)
    
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(v).strftime('%Y %m/%d %H:%M') for v in values]

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

        clr_up, clr_down, clr_line = '#0F0f', '#F00f', '#FFFF'
        lp = pg.mkPen(clr_line)
        up = pg.mkPen(clr_up)
        dp = pg.mkPen(clr_down)
        brush_up = pg.mkBrush(clr_up)
        brush_dn = pg.mkBrush(clr_down)

        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        '''
        #w = (self.data[1][0] - self.data[0][0])
        #w = 1500 # for 60min
        #w = 750 # for 30min
        #w = 375 # for 15min
        #w = 125 # for 5min
        w = 25 # for 1min
        '''
        if FinData.duration == '1min':
            w = 25*0.95
        elif FinData.duration == '5min':
            w = 125*0.95
        elif FinData.duration == '15min':
            w = 375*0.95
        elif FinData.duration == '30min':
            w = 750*0.95
        elif FinData.duration == '60min':
            w = 1500*0.95
        else:
            w = 1500*0.95

        for (t, open, close, min, max) in self.data:
            p.setPen(lp) # ヒゲの色
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            p.setPen(up if close>open else dp) # コメントアウトすればふちが有るかんじのローソクになる
            p.setBrush(brush_up if close>open else brush_dn)
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())



def fetch_4values(company_data, fetch_span):
    # 四本値を取ってくる。
    from alpha_vantage.techindicators import TechIndicators
    symbol=company_data[0]
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    FinData.duration = fetch_span
    if fetch_span == 'Daily':
        data, meta_data = ts.get_daily(symbol=symbol,outputsize='full')
    else:
        data, meta_data = ts.get_intraday(symbol=symbol,interval=fetch_span, outputsize='full')
    # 行名を変更する。
    df = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low':'Low','4. close':'Close', '5. volume':'Volume'})
    df = df.sort_index(axis=0, level=None, ascending=True)
    print(type(df))
    return df

def create_df():
    import pandas as pd
    n = 100000
    index = pd.date_range(start='20220101', periods=n, freq='T')
    s = pd.Series(np.random.randn(n).cumsum(), index=index)
    s += abs(s.min())*2
    df = s.resample('H').ohlc()
    df.columns = df.columns.map(str.capitalize)
    return df



