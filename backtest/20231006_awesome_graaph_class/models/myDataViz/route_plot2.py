'''
Mapで調理した際に保存されるcsvを表示するためのコード
'''
# 各モジュールは、こちらからも読み込む（docstring的にオイシイから）
import numpy as np

import pyqtgraph as pg
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea



from my_modules.prop_func import *
from my_modules.map import *



class DrawGraph():
    def __init__(self, *args, **kwargs):
        super(DrawGraph, self).__init__(*args, **kwargs)

    def make_df(filename):
        df = pd.read_csv(filename, header=0)
        df['delta_Alt(m)'] = df['Alt(m)'].diff()
        df['slope(%)'] = df['delta_Alt(m)']*(100/(df['dist(km)']*1000))
        df['slope(%).mean'] = df['slope(%)'].rolling(100).mean()
        start = df['dist_sum(km)'][0]
        goal = df['dist_sum(km)'][len(df)-1]
        start_point = (df['Lat'][0],df['Long'][0])
        goal_point = (df['Lat'][len(df)-1],df['Long'][len(df)-1])
        
        # 斜度（slopeの計算を行う）
        return df, start, goal, start_point, goal_point

    def update_df(minX, maxX, df):
        # テーブル表示用
        form3 = lambda x: ('{:.3f}'.format(x))
        full_dist = form3(df['dist_sum(km)'][len(df)-1])

        distindex =df['dist_sum(km)']
        df_range = df[(distindex >= minX) & (distindex <= maxX)]
        df_range_pos = df_range.where(df_range > 0,0)

        sum_of_delta_alt = df_range_pos['delta_Alt(m)'].sum()
        max_slope = df_range['slope(%).mean'].max()
        min_slope = df_range['slope(%).mean'].min()
        ave_slope = df_range['slope(%).mean'].sum()/len(df_range['slope(%).mean'])
        df_analysis = pd.DataFrame(
            data={   'Index':['総行程(km)','Region(km)','獲得標高(m)','最大斜度（登）(%)','最大斜度（下）(%)','平均斜度(%)'],
                        'Value(往路)':[full_dist,form3(maxX-minX),sum_of_delta_alt, max_slope, min_slope, ave_slope],
                    'Value(復路)':['km','km','m','%','%','%']}
                    )
        return df_range, df_analysis



    def LatLongData(df):
        list = df.loc[:, 'Lat':'Long'].values.tolist()
        return list




    def mapPlot(center_of_interest, route_pos):
        m = folium.Map(
            location = center_of_interest,
            #zoom_start=8,
            #tiles='https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png', # 通常
            #tiles='Stamen Terrain',
            tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png', # 淡色
            #tiles='https://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg', # 航空写真
            #tiles='https://cyberjapandata.gsi.go.jp/xyz/ort_old10/{z}/{x}/{y}.png', # 国土地理院 空中写真（1961～1964年）
            #attr='国土地理院 空中写真（1961～1964年）',
            attr='&copy; <ahref="https://maps.gsi.go.jp/development/ichiran.html">国土地理院</a>'
        )


        # 折り畳み式ミニマップを追加
        plane_line = folium.PolyLine(
            route_pos,
            weight=8,
            color="#0086CC", 
            #color="#e4041c",
        )
        m.add_child(plane_line)
        
        plugins.MiniMap().add_to(m)
        data = io.BytesIO()
        m.save(data, close_file=False)
        return m



    def draw_graph(self):
        area = DockArea()
        self.layout.addWidget(area)  

        d1 = Dock("Map", size=(1, 2))
        area.addDock(d1) ## place d1 at left edge of dock area


        # Mapのデータ作成とプロット
        from shapely.geometry import MultiPoint
        df, start, goal, start_point , goal_point = DrawGraph.make_df(FilePath.data_filename)
        points = MultiPoint([start_point, goal_point])
        
        # Widgetのインスタンスに地図（m）を入れて表示する。
        route_pos = DrawGraph.LatLongData(df)
        center_of_interest = (points.centroid.x, points.centroid.y)
        m = DrawGraph.mapPlot(center_of_interest, route_pos)

        from PySide6.QtWebEngineWidgets import QWebEngineView
        widget = QWebEngineView()
        d1.addWidget(widget)

        #layout.addWidget(widget)
        data = io.BytesIO()
        m.save(data, close_file=False)
        widget.setHtml(data.getvalue().decode())


        graphics_w = pg.GraphicsLayoutWidget()
        fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}

        d2 = Dock("解析結果", size=(4, 1)) # 横, 縦
        area.addDock(d2) ## place d1 at left edge of dock area
        d2.addWidget(graphics_w)

        last_region = []

        df1, self.start1, self.goal1, self.start_point1 , self.goal_point1 = DrawGraph.make_df(FilePath.data_filename)
        self.df1 = df1

        p1 = graphics_w.addPlot(row=0, col=0)
        fontCss = {'font-family': "Arial", 'font-size': '16pt'}
        fontCssLegend = {'font-family': "Arial", 'font-size': '16pt'}
        fontCss["color"] = '#fff'

        pen_dist = pg.mkPen(color='#00849c', width=5)
        p1.plot(x=df1['dist_sum(km)'],
                    y=df1['Alt(m)'],
                    #name= fontCssLegend +'<p>Dist.(km)</p>',
                    pen=pen_dist,
                    )
        p1.getAxis('right').setLabel(**fontCss)
        p1.getAxis('left').setWidth(40)
        #dist.hideAxis('bottom'),
        p1.setLabels(right='高度(m)')
        setprop_func_route(p1)
        self.p1 = p1

        # 斜度に応じてポイントを色分け
        cm = pg.colormap.get('CET-L19') # prepare a diverging color map
        cm.setMappingMode('diverging') # set mapping mode
        brush = cm.getBrush( span=(-10, 10) , orientation='horizontal') #gradient from blue at -1 to red at +1
        #pen = cm.getPen( span=(df['slope(%).mean'].min(), 10), width=7) #gradient from blue at -1 to red at +1
        pen = cm.getPen( span=(-10, 10), width=5) # gradient from blue at -1to red at +1
        pen_h = cm.getPen( span=(-10, 10), orientation='horizontal',width=3)
        self.pen = pen
        self.pen_h = pen_h
        self.brush = brush

        slope = graphics_w.addPlot(row=1, col=0)
        slope.plot(x=df1['dist_sum(km)'],
                    y=df1['slope(%).mean'],
                    #name= self.fontCssLegend +'<p>Slope(%)</p>',
                    pen=pen,
                    #brush=brush,
                    )
        slope.getAxis('right').setLabel(**fontCss)
        slope.getAxis('left').setWidth(40)
        slope.setLabels(right='斜度(%)')
        slope.setXLink(p1)
        setprop_func_route(slope)
        self.slope = slope


        region = pg.LinearRegionItem() #http://www.pyqtgraph.org/documentation/graphicsItems/linearregionitem.html
        plt_region = graphics_w.addPlot(row=2, col=0)
        plt_region.addItem(region, ignoreBounds=True)
        plt_region.plot(df1['dist_sum(km)'],df1['Alt(m)'], pen='#fff6')
        plt_region.getAxis('bottom').setLabel(**fontCss)
        plt_region.setLabels(bottom='距離(km)')
        setprop_region_route(plt_region)
        self.region = region


        # Histogram
        plt_hist = graphics_w.addPlot(row=0, col=1, rowspan=3, colspan=3)
        setprop_route(plt_hist)
        # addItem()は、下から。
        self.plt_hist = plt_hist
        plt_hist.getAxis('bottom').setLabel(**fontCss)
        plt_hist.setLabels(bottom='斜度(%)')
        plt_hist.getAxis('right').setLabel(**fontCss)
        plt_hist.setLabels(right='頻度(回)')
        plt_hist.setAutoVisible(y=True)


        if last_region == []: # 初めてプロットするときのRegion
            # for df.sort_index(axis=0, level=None, ascending=True)
            self.region.setRegion([self.start1, self.goal1])
        else:
            self.region.setRegion(last_region) # メイン画面のSMAの値を変更した際のRegion
        
        from shapely.geometry import MultiPoint
        def updatePlot():
            region.setZValue(10)
            minX, maxX = region.getRegion()
            self.p1.setXRange(minX, maxX, padding=0)

            # ヒストグラムの更新更新表示のための計算
            # dfからminx,maxxの範囲を切り出してnpにてヒストグラム用の値を計算
            distindex =self.df1['dist_sum(km)']
            df_range = self.df1[(distindex >= minX) & (distindex <=maxX)]
            slope = df_range['slope(%).mean']
            import math
            resol = (math.ceil(slope.max()) - math.floor(slope.min())) * 16
            y, x = np.histogram(slope, bins=np.linspace(math.floor(slope.min()),math.ceil(slope.max()), resol))
            hist_x = np.delete(x,0)# データが一つ多いので末尾を削除
            # ここで、addItem
            self.plt_hist.clear() # clearしないと、データが重ね描きされる。
            self.plt_hist.setAutoVisible(y=True)
            self.plt_hist.addItem(pg.PlotDataItem(hist_x,y,pen =self.pen_h,symbolBrush =None,symbolPen=None , symbolSize = 5))
            #df_range, df_analysis = update_df(minX, maxX, self.df1)

            distindex = self.df1['dist_sum(km)']
            df_range = self.df1[(distindex >= minX) & (distindex <= maxX)]
            route_pos_region = DrawGraph.LatLongData(df_range)
            
            df_range.reset_index()
            start_point = (df_range['Lat'][0],df_range['Long'][0])
            goal_point = (df_range['Lat'][len(df_range)-1],df_range['Long'][len(df_range)-1])
            points = MultiPoint([start_point, goal_point])
            center_of_interest = (points.centroid.x, points.centroid.y)
            
        def updateRegion():
            region.setRegion(p1.getViewBox().viewRange()[0])

        region.sigRegionChanged.connect(updatePlot)
        p1.sigXRangeChanged.connect(updateRegion)
        updatePlot()


        if self.start_point1 ==None:
            points = MultiPoint([self.start_point2, self.goal_point2])
            center_of_interest = (points.centroid.x, points.centroid.y)
        elif self.start_point2 == None:
            points = MultiPoint([self.start_point1, self.goal_point1])
            center_of_interest = (points.centroid.x, points.centroid.y)
        else:
            points = MultiPoint([self.start_point1, self.goal_point1])
            #points = MultiPoint([self.start_point1, self.goal_point1, self.start_point2, self.goal_point2])
            center_of_interest = (points.centroid.x, points.centroid.y)


        '''
        self.mapPlot(center_of_interest, route_pos_region)
        plane_line_region = folium.PolyLine(
            route_pos_region,
            weight=8,
            #color="#00849c", # 浅葱色
            #color="#e4041c",
            color='#E24F93',
        )
        plane_line_region.add_to(self.m)
        popup1 = folium.LatLngPopup()
        self.m.add_child(popup1)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.mapWidget.setHtml(data.getvalue().decode())


        plane_line_region = folium.PolyLine(
            route_pos_region,
            weight=8,
            #color="#00849c", # 浅葱色
            #color="#e4041c",
            color='#E24F93',
        )
        plane_line_region.add_to(self.m)
        popup1 = folium.LatLngPopup()
        self.m.add_child(popup1)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.mapWidget.setHtml(data.getvalue().decode())

    def get_map_profile(self):
        import inspect
        LIST = inspect.getmembers(self.m)
        #for i in LIST:
        #    print(i)
        self.plainTextEdit.setPlainText(str(self.m.get_bounds())+'\n')
        self.plainTextEdit.insertPlainText('options() : ' + str(self.m.options))

    '''