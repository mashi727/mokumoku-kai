from os import PathLike
import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QFont
from stockPlotUi3 import Ui_MainWindow


import platform

import pyqtgraph as pg
from pyqtgraph.dockarea import *
from datetime import datetime

# 自作のライブラリです。
from api.fetch_ticker_symbol import *
from api.prepare_dataframe import *
from graph.graphplot_with_dock import *
#from data.data_class import *

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

def check_method(object_name):
    import inspect
    print(type(object_name))
    for method in inspect.getmembers(object_name):
        print(method)

def test_method(object_name):
    import inspect
    print(type(object_name))
    for x in inspect.getmembers(object_name, inspect.ismethod):
        print(x[0])

class SmaCross(Strategy):
    n1 = 10 # 短期SMA
    n2 = 30 # 長期SMA

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1) 
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self): #チャートデータの行ごとに呼び出される
        if crossover(self.sma1, self.sma2): #sma1がsma2を上回った時
            self.buy() # 買い
        elif crossover(self.sma2, self.sma1):
            self.position.close() # 売り

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    '''初期化メソッド（インスタンス変数の定義）'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self) # この中で必要なMainWindowの定数が宣言
        self.init_ui()
        # いらないみたい
        #self.SB_sma_short  = self.SB_sma_short
        #self.SB_sma_med  = self.SB_sma_med
        #self.SB_sma_long  = self.SB_sma_long
        # OSによってフォントサイズを変更
        #view.setColumnWidth(0,260)
        #self.tableView = self.tableView
        # 検索キー（searchSymbol）が変更されたら、自動的にtableViewに表示
        self.lineEdit.textEdited.connect(self.searchSymbol)
        self.lineEdit_TickSyml.returnPressed.connect(self.searchSymbol_from_alphavantage)
        # self.lineEdit.returnPressed.connect(self.searchSymbol)
        # Enterキーを押すか、フィールドがフォーカスを失ったとき
        # self.lineEdit.editingFinished.connect(self.searchSymbol)
        # viewのコラムがダブルクリックされると、
        # 左端のtickersymbolを取得する関数（get_ticker_symbol）を実行
        # get_ticker_symbolの中で、plot_graphを呼び出す
        
        
        '''
        Backtestのパラメータを取得するよ
        
        
        self.tableView.doubleClicked.connect(lambda: self.plot_graph_offline('fetch_4values'))
        self.SB_sma_short.valueChanged.connect(lambda: self.plot_graph_offline('sma_update_only'))
        self.SB_sma_med.valueChanged.connect(lambda: self.plot_graph_offline('sma_update_only'))
        self.SB_sma_long.valueChanged.connect(lambda: self.plot_graph_offline('sma_update_only'))
        '''
        
        
        
        self.tableView.doubleClicked.connect(lambda: self.plot_graph('fetch_4values'))
        self.SB_sma_short.valueChanged.connect(lambda: self.plot_graph('sma_update_only'))
        self.SB_sma_med.valueChanged.connect(lambda: self.plot_graph('sma_update_only'))
        self.SB_sma_long.valueChanged.connect(lambda: self.plot_graph('sma_update_only'))
        
        # わざわざ呼ばなくてもlineEdit_end_region.textChangedで、backtest()が起動する。
        # self.tableView.doubleClicked.connect(lambda: self.backtest())
        self.lineEdit_end_region.textChanged.connect(lambda: self.backtest())
        self.lineEdit_start_region.textChanged.connect(lambda: self.backtest())
        self.lineEdit_end_region_2.textChanged.connect(lambda: self.backtest2())
        self.lineEdit_start_region_2.textChanged.connect(lambda: self.backtest2())
        '''
        これでも渡せる。
        self.SB_sma_long.valueChanged.connect(lambda: self.test('sma_update_only',self.SB_sma_long))
        '''



        # 後で使うよ
        #self.spinBox_Long_ini.valueChanged.connect(self.dummy_func)
        #self.spinBox_Short_ini.valueChanged.connect(self.dummy_func)

        # ボタンをクリックすると、plot_graphを呼び出す

        #self.pushButton.clicked.connect(lambda : prepare_dataframe(self.lineEdit_TickSyml.text(), self.comboBox.currentText()))

    '''インスタンスメソッドの定義'''    
    def test_get_parameter(self):
        initview_param = InitialViewer(self.spinBox_Long_ini.text(),self.spinBox_Short_ini.text())
        return initview_param
        
    def init_ui(self):
        #self.setGeometry(0, 0, 2880, 1750) # WQXGA (Wide-QXGA)
        self.setGeometry(10, 10, 2760, 1600) # WQXGA (Wide-QXGA)
        #self.setGeometry(100, 100, 2560, 1440) # WQHD
        #self.setGeometry(100, 100, 1920, 1200) # WUXGA
        font1 = QFont()
        osname = platform.system()
        if osname == 'Darwin':
            font1.setPointSize(18)
            self.label_46.setFont(font1)
            #view.setFont(font)
            #self.listWData.setFont(font)
        elif osname == 'Windows':
            font1.setPointSize(8)
            #view.setFont(font)
            #self.listWData.setFont(font)            
        else:
            FontFamily = 'FreeSerif'


    def searchSymbol(self):
        ticker_search_keyword = self.lineEdit.text() # Search Keywordの取得
        self.tableView.setModel(make_masked_tableview_model(search_symbol(),ticker_search_keyword))
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode(1)) # 1 -> stretch

    def searchSymbol_from_alphavantage(self):
        ticker_search_keyword = self.lineEdit_TickSyml.text() # Search Keywordの取得
        self.tableView.setModel(make_tableview_model(search_symbol_alphavantage(ticker_search_keyword)))
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode(1)) # 1 -> stretch

    def get_ticker_symbol(self):
        index = self.tableView.currentIndex()
        #company_name = self.tableView.model().index(index.row(), 1).data()
        company_data = []
        for i in range(2):
            company_data.append(self.tableView.model().index(index.row(), i).data())
        return company_data # ticker_symbol, 社名

    def test(self,discriminator,value):
        print('discri:',discriminator)
        print('value:',value.text())
        

    def plot_graph(self, discriminator):
        if discriminator=='fetch_4values':
            print('Im in fetch_4values!')
            company_data = self.get_ticker_symbol()
            # for dummy data
            #self.df_4values = create_df() # comboBox.current.Text()は、取得するspan
            # for actual data
            #self.df_4values = fetch_4values_adjust(company_data, self.comboBox.currentText()) # comboBox.current.Text()は、取得するspan
            # テスト用に、ローカルファイルから四本値を読み込み
            #self.df_4values.to_csv('data/aapl.csv')
            self.df_4values = pd.read_csv('./data/aapl.csv', index_col='date', parse_dates=True)
            if not company_data:
                #pass
                QMessageBox.warning(None, "Notice!", "Ticker symbolを入力してください!", QMessageBox.Yes)
            else:
                # status barの表示
                status_bar = self.statusBar() # 下にあるステータスバー
                status_bar.showMessage('表示中の銘柄 : ' + str(company_data[1])) # 書きたいメッセージ
                df = make_dataframe(self.df_4values, int(self.SB_sma_short.text()), int(self.SB_sma_med.text()), int(self.SB_sma_long.text()))
                last_region = []
                self.plot_stock(df, last_region)
        else:
            print('Im in update sma_values!')
            df = make_dataframe(self.df_4values, int(self.SB_sma_short.text()), int(self.SB_sma_med.text()), int(self.SB_sma_long.text()))
            last_region = [self.minx, self.maxx]
            self.plot_stock(df, last_region)

    def backtest(self):
        from backtesting import Backtest, Strategy
        from backtesting.lib import crossover
        from backtesting.test import SMA
        
        #print(self.last_region)
        #self.df_region_4values = 

        bt = Backtest(
            self.df_region_4values, # チャートデータ
            SmaCross, # 売買戦略
            cash=1000, # 最初の所持金
            commission=0.00495, # 取引手数料
            margin=1.0, # レバレッジ倍率の逆数（0.5で2倍レバレッジ）
            trade_on_close=True, # True：現在の終値で取引，False：次の時間の始値で取引
            exclusive_orders=True #自動でポジションをクローズ
        )

        output = bt.run() # バックテスト実行
        df_backtesting = pd.DataFrame(output).reset_index().rename(columns={'index': 'INDEX',0:'Value'})        
        self.tableView_backtesting.setModel(make_tableview_model(df_backtesting))
        self.tableView_backtesting.horizontalHeader().setStretchLastSection(False)
        self.tableView_backtesting.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_backtesting.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode(1)) # 1 -> stretch
        self.tableView_backtesting.verticalHeader().setVisible(False) # これでindexの列が非表示になるよ。

        #check_method(self.plainTextEdit)
        #self.plainTextEdit.setPlainText(output) # 実行結果(データ)
        #bt.plot() # 実行結果（グラフ）


    def backtest2(self):
        from backtesting import Backtest, Strategy # バックテスト、ストラテジー
        from backtesting.lib import crossover

        import talib as ta

        def MACD(close, n1, n2, ns):
            macd, macdsignal, macdhist = ta.MACD(close, fastperiod=n1, slowperiod=n2, signalperiod=ns)
            return macd, macdsignal

        class MACDCross(Strategy):
            n1 = 12 #短期EMAの期間
            n2 = 26 #長期EMAの期間
            ns = 9 #シグナル（MACDのSMA）の期間

            def init(self):
                self.macd, self.macdsignal = self.I(MACD, self.data.Close, self.n1, self.n2, self.ns)

            def next(self): # チャートデータの行ごとに呼び出される
                if crossover(self.macd, self.macdsignal): #macdがsignalを上回った時
                    self.buy() # 買い
                elif crossover(self.macdsignal, self.macd): #signalがmacdを上回った時
                    self.position.close() # 売り

        # バックテストを設定
        bt = Backtest(
            self.df_region_4values, # チャートデータ
            MACDCross, # 売買戦略
            cash=1000, # 最初の所持金
            commission=0.00495, # 取引手数料
            margin=1.0, # レバレッジ倍率の逆数（0.5で2倍レバレッジ）
            trade_on_close=True, # True：現在の終値で取引，False：次の時間の始値で取引
            exclusive_orders=True #自動でポジションをクローズ(オープン)
        )

        output = bt.run() # バックテスト実行
        df_backtesting_2 = pd.DataFrame(output).reset_index().rename(columns={'index': 'INDEX',0:'Value'})        
        self.tableView_backtesting_2.setModel(make_tableview_model(df_backtesting_2))
        self.tableView_backtesting_2.horizontalHeader().setStretchLastSection(False)
        self.tableView_backtesting_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_backtesting_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode(1)) # 1 -> stretch
        self.tableView_backtesting_2.verticalHeader().setVisible(False) # これでindexの列が非表示になるよ。

        #check_method(self.plainTextEdit)
        #self.plainTextEdit.setPlainText(output) # 実行結果(データ)
        #bt.plot() # 実行結果（グラフ）


    def plot_stock(self, df, last_region):
        self.dockWidget.clear()
        # DockWIdgetをExpandしないと、こじんまりと表示される。
        d1 = Dock('chart', size=(20, 15))
        d2 = Dock('6values', size=(20,2))
        d3 = Dock('macd', size=(10,7))
        d4 = Dock('region', size=(1, 2))
        d5 = Dock('Volume',size=(10, 5))
        self.dockWidget.addDock(d1)
        self.dockWidget.addDock(d2)
        self.dockWidget.addDock(d3)
        self.dockWidget.addDock(d5)
        self.dockWidget.addDock(d4)
        
        # dfからNonのデータを削除して、表示用にリージョン内の最大/最少を求めるためのdfを作成
        self.df = df.dropna(how='any')
        self.dt2 = self.df.index.view(np.int64)//10**9
        self.sma_long = self.df['sma_short'].values
        self.sma_med = self.df['sma_med'].values
        self.sma_short = self.df['sma_long'].values
        self.macd_hist = self.df['macd_hist'].values
        self.macd = self.df['macd'].values
        self.macd_sig = self.df['macd_sig'].values
        self.Volume = self.df['Volume'].values

        

        # こちらは、もろもろ用のデータフレーム
        self.dt = df.index.view(np.int64)//10**9
        self.close = df['Close'].values

        setprop = lambda x: (x.showGrid(x=True, y=True, alpha=0.75),
                                x.showAxis('right'),
                                x.hideAxis('left'), 
                                x.setAutoVisible(y=True))

        plt_chart = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})

        
        ''' 2軸表示用
        self.p2 = pg.ViewBox()
        # scene(p2)用の軸を右側に設定
        plt_chart.scene().addItem(self.p2)
        plt_chart.showAxis('right')
        # 以下の行にて右側の軸がp2に連動するように指定
        # 指定しないと左側の軸と右側の軸が同じになる
        plt_chart.getAxis('right').linkToView(self.p2)
        
        # p1とp2のx軸を連動させる場合は指定
        self.p2.setXLink(plt_chart)
        '''
        

        setprop(plt_chart)
        plt_chart.getPlotItem().getAxis('bottom').setHeight(0) # hideAxis('bottom')だと縦のグリッドが消えてしまう
        #CandlestickItem : data must have fields: time, open, close, min, max
        plt_chart.addItem(CandlestickItem(df[['Open', 'Close', 'Low', 'High']]))
        #plt_chart.addItem(TestCandle(df[['Open', 'High', 'Low', 'Close']]))
        # ma & hl bands
        #pen = pg.mkPen(color=(255, 0, 0, 100), width=5)
        pen = pg.mkPen(color='#FF07', width=3)
        pen1 = pg.mkPen(color='#0F07', width=3)
        pen2 = pg.mkPen(color='#FFF7', width=3)

        cm = pg.colormap.get('CET-L17') # prepare a linear color map
        cm.reverse()                    # reverse it to put light colors at the top 
        pen = cm.getPen( span=(0.0,6.0), width=1 ) # gradient from blue (y=0) to white (y=1)
        brush = cm.getBrush( span=(0.0,6.0)) # gradient from blue (y=0) to white (y=1)
        
        # 2軸表示用
        # plot a curve drawn with a pen colored according to y value:
        # self.p2.addItem(pg.PlotDataItem(x=self.dt, y=df['stage'], pen=pen, brush=brush, fillLevel=0.1))

        plt_chart.addItem(pg.PlotDataItem(self.dt, df['sma_short'], pen=pen, label='test'))
        plt_chart.addItem(pg.PlotDataItem(self.dt, df['sma_med'], pen=pen1))
        plt_chart.addItem(pg.PlotDataItem(self.dt, df['sma_long'], pen=pen2))
        #plt_chart.addItem(pg.PlotDataItem(self.dt, df['Hband'], pen='r'))
        #plt_chart.addItem(pg.PlotDataItem(self.dt, df['Lband'], pen='#08F'))
        plt_chart.setAutoVisible(y=True)
        self.plt_chart = plt_chart
        plt_chart.setStyleSheet("""
                            border-top: 5px solid rgba(0,0,0,0);
                            border-style: outset;
                            border-width: 5px;
                            border-color: orange;
                            padding: 4px;
                            """)
        
        
        ''' Y軸の2軸表示用
        self.updateViews()
        self.plt_chart.plotItem.vb.sigResized.connect(self.updateViews)
        '''
        
        d1.addWidget(plt_chart)
    
        # stc K
        plt_k = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        setprop(plt_k)    
        # Prepare demonstration data
        cm = pg.colormap.get('CET-L17') # prepare a linear color map
        cm.reverse()                    # reverse it to put light colors at the top 
        pen = cm.getPen( span=(0.0,6.0), width=1 ) # gradient from blue (y=0) to white (y=1)
        brush = cm.getBrush( span=(0.0,6.0)) # gradient from blue (y=0) to white (y=1)
        # plot a curve drawn with a pen colored according to y value:
        plt_k.getPlotItem().getAxis('bottom').setHeight(0)
        plt_k.addItem(pg.PlotDataItem(x=self.dt, y=df['stage'], pen=pen, brush=brush, fillLevel=0.1))
        #plt_k.addItem(pg.PlotDataItem(self.dt, df['stage'], pen='#FF0',symbolSize=9, symbolBrush='#FF07', symbolPen='#FF07'))
        plt_k.setXLink(plt_chart)
        plt_k.setYRange(0,6)

        d2.addWidget(plt_k)
        
        # macd
        plt_macd = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        setprop(plt_macd)
        
        # print('self.dt[2]-self.dt[1]:',self.dt[2]-self.dt[1])
        plt_macd.addItem(pg.BarGraphItem(x=self.dt, height=df['macd_hist'], width=self.dt[2]-self.dt[1], pen=None ,alpha=1, brush='#0D0'))
        plt_macd.addItem(pg.PlotDataItem(self.dt, df['macd'], pen='w'))
        plt_macd.addItem(pg.PlotDataItem(self.dt, df['macd_sig'], pen='r'))
        plt_macd.setXLink(plt_chart)
        self.plt_macd = plt_macd
        d3.addWidget(plt_macd)

        # region
        region = pg.LinearRegionItem() # http://www.pyqtgraph.org/documentation/graphicsItems/linearregionitem.html
        plt_region = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        plt_region.showAxis('right')
        plt_region.hideAxis('left')
        plt_region.addItem(region, ignoreBounds=True)
        plt_region.plot(self.dt, self.close, pen=(96,96,96))
        self.region = region
        d4.addWidget(plt_region)
        
        # As ReqとしてVolumeを表示
        plt_volume = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        setprop(plt_volume)
        # print('self.dt[2]-self.dt[1]:',self.dt[2]-self.dt[1])
        #plt_volume.addItem(pg.PlotDataItem(self.dt, df['Volume'], pen='g'))
        #plt_volume.addItem(pg.BarGraphItem(self.dt, df['Volume']))
        # こういうことができれば良いなと思うよ
        # https://www.wizard-notes.com/entry/python/matplotlib-barplot-with-colormap
        # 2021.11.21記
        # 以下のコードを参考にしよ
        # Example 2: Gradient brush
        cm = pg.colormap.get('CET-L19') # prepare a diverging color map
        cm.setMappingMode('diverging') # set mapping mode
        brush = cm.getBrush( span=(0., df['Volume'].max()) ) # gradient from blue at -1 to red at +1
        pen = cm.getPen( span=(0., df['Volume'].max()), width=1.2) # gradient from blue at -1 to red at +1

        # plot a curve that is filled to zero with the gradient brush:

        plt_volume.addItem(pg.PlotDataItem( x=self.dt, y=df['Volume'], pen=pen, brush=brush))
        #plt_volume.addItem(pg.PlotDataItem(self.dt, df['Volume'], pen='#1FF8',symbolSize=9, symbolBrush='#1FF4', symbolPen='#1FF2'))
        plt_volume.setXLink(plt_chart)
        self.plt_volume = plt_volume
        #d5.addWidget(plt_volume)
        d2.addWidget(plt_volume)
        #check_method(plt_volume)


        self.plt_chart.sigRangeChanged.connect(self.update_region)
        self.region.sigRegionChanged.connect(self.update_region_change)

        if last_region == []: # 初めてプロットするときのRegion
            # for df.sort_index(axis=0, level=None, ascending=True)
            self.region.setRegion([self.dt[len(self.dt)-int(len(self.dt)/10)], self.dt[len(self.dt)-1]])
        else:
            self.region.setRegion(last_region) # メイン画面のSMAの値を変更した際のRegion


    '''
    ## Handle view resizing
    def updateViews(self):
        ## view has resized; update auxiliary views to match
        self.p2.setGeometry(self.plt_chart.plotItem.vb.sceneBoundingRect())
        ## need to re-update linked axes since this was called
        ## incorrectly while views had different shapes.
        ## (probably this should be handled in ViewBox.resizeEvent)
        self.p2.linkedViewChanged(self.plt_chart.plotItem.vb, self.p2.XAxis)
    '''
    
    def update_region_change(self, region):
        region.setZValue(10)
        # plt_chartのグラフy軸をRegionの最大最小にあわせて表示する
        self.minx, self.maxx = region.getRegion()
        # ここからBacktest用の処理
        # Backtest用にリージョンを取得
        from datetime import datetime
        dt_minx = datetime.fromtimestamp(self.minx)
        dt_maxx = datetime.fromtimestamp(self.maxx)
        minx_str = dt_minx.strftime("'%y.%m.%d %H:%M")
        maxx_str = dt_maxx.strftime("'%y.%m.%d %H:%M")
        # Backtest用にRegionの範囲の行を抽出して、データフレームを準備
        idx = (self.dt>=self.minx) & (self.dt<=self.maxx)
        if idx.sum()<2:
            return
        self.df_region_4values =  self.df_4values[idx]
        
        # 株価のデータのテーブル表示
        data_table_model = TableModel(self.df_region_4values)
        self.tableView_df.setModel(data_table_model)
        self.tableView_df.horizontalHeader().setStretchLastSection(False)
        self.tableView_df.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_df.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_df.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_df.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_df.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_df.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_df.horizontalHeader().setSectionResizeMode(14, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents


        # !!!!!!!!! NOTE !!!!!!!!!
        # lineEdit_start_regionを変更すると、backtest関数が呼ばれるので、
        # 以下の設定より前に、データフレームを準備する必要がある。
        self.lineEdit_start_region.setText(minx_str)
        self.lineEdit_end_region.setText(maxx_str)
        self.lineEdit_start_region_2.setText(minx_str)
        self.lineEdit_end_region_2.setText(maxx_str)
        
        self.plt_chart.setXRange(self.minx, self.maxx, padding=0)
        # y軸の最適表示のためのindexを作成
        idx2 = (self.dt2>=self.minx) & (self.dt2<=self.maxx)
        if idx2.sum()<2:
            return
        miny = min([self.sma_short[idx2].min(),self.sma_med[idx2].min(),self.sma_long[idx2].min()])
        maxy = max([self.sma_short[idx2].max(),self.sma_med[idx2].max(),self.sma_long[idx2].max()])
        self.plt_chart.setYRange(miny*0.97, maxy*1.03)


        # macdグラフy軸をRegionの最大最小にあわせて表示する
        # y軸の最適表示のためのindexを作成
        idx3 = (self.dt2>=self.minx) & (self.dt2<=self.maxx)
        '''
        print('idx3.sum()',idx3.sum())
        print('idx3.sum()<1',idx3.sum()<1)
        print('idx3.sum()<2',idx3.sum()<2)
        print('idx3.sum()<3',idx3.sum()<3)
        print('idx3.sum()<4',idx3.sum()<4)
        '''
        if idx3.sum()<1:
            return
        macd_miny = min([self.macd_hist[idx3].min(),self.macd[idx3].min(),self.macd_sig[idx3].min()])
        macd_maxy = max([self.macd_hist[idx3].max(),self.macd[idx3].max(),self.macd_sig[idx3].max()])
        self.plt_macd.setYRange(macd_miny*0.8, macd_maxy*1.2) # 倍数が効かない気がする。。。

        Volume_miny = min([self.Volume[idx3].min(),self.Volume[idx3].min(),self.Volume[idx3].min()])
        Volume_maxy = max([self.Volume[idx3].max(),self.Volume[idx3].max(),self.Volume[idx3].max()])
        self.plt_volume.setYRange(Volume_miny*0.8, Volume_maxy*1.2) # 倍数が効かない気がする。。。


        '''
        import math
        if math.isnan(minyy):
            minyy = 50
            maxyy =-50
        else:
            pass
        '''
        #print(miny,maxy,minyy,maxyy)
        
        # plt_chart.setAutoVisible(y=True) しても縦のスケールが
        # 自動調整されないのでとりあえずここでsetYRangeしたよくわからない
    
    def update_region(self, window, viewRange):
        self.region.setRegion(viewRange[0])



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    # http://fatbald.seesaa.net/article/451667700.html
    from pyqtgraph.dockarea.Dock import DockLabel
    def updateStyle(self):
        self.setStyleSheet("DockLabel { color: #FFF; background-color: #444; font-size:20pt}")
    setattr(DockLabel, 'updateStyle', updateStyle)
    
    style = """
        QWidget { color: #AAA; background-color: #333; border: 0px; padding: 0px; }
        QWidget:item:selected { background-color: #666; }
        QMenuBar::item { background: transparent; }
        QMenuBar::item:selected { background: transparent; border: 1px solid #666; }
    """
    main()
