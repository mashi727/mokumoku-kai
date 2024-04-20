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


    def mapPlot(center_of_interest, df, route_pos):
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
        m = DrawGraph.mapPlot(center_of_interest, df, route_pos)

        from PySide6.QtWebEngineWidgets import QWebEngineView
        widget = QWebEngineView()
        d1.addWidget(widget)

        #layout.addWidget(widget)
        data = io.BytesIO()
        m.save(data, close_file=False)
        widget.setHtml(data.getvalue().decode())


        # tag::visualize plot data:
        # 表示領域の確保
        graphics_w = pg.GraphicsLayoutWidget()
        fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}

        d2 = Dock("解析結果", size=(4, 1)) # 横, 縦
        area.addDock(d2) ## place d1 at left edge of dock area
        d2.addWidget(graphics_w)

        p1 = graphics_w.addPlot(row=0, col=0)
        pen_dist = pg.mkPen(color='#00849c', width=5)
        p1.plot(x=df['dist_sum(km)'],
                y=df['Alt(m)'],
                name= '<p>Dist.(km)</p>',
                pen=pen_dist,
                )
        #p1.setLabels(right='高度(m)')
        setprop_func_route(p1)
        styles = {'color':'white','font-size':'20px', 'font-style':'bold'}
        p1.setLabel('right', text='高度', units='m', **styles)

        p2 = graphics_w.addPlot(row=1, col=0)
        # 斜度に応じてポイントを色分け
        cm = pg.colormap.get('CET-L19') # prepare a diverging color map
        cm.setMappingMode('diverging') # set mapping mode
        brush = cm.getBrush( span=(-10, 10) , orientation='horizontal') #gradient from blue at -1 to red at +1
        #pen = cm.getPen( span=(df['slope(%).mean'].min(), 10), width=7) #gradient from blue at -1 to red at +1
        pen = cm.getPen( span=(-10, 10), width=5) # gradient from blue at -1to red at +1
        pen_h = cm.getPen( span=(-10, 10), orientation='horizontal',width=3)
        p2.plot(x=df['dist_sum(km)'],
                    y=df['slope(%).mean'],
                    name= '<p>Slope(%)</p>',
                    pen=pen,
                    #brush=brush,
                    )
        p2.getAxis('right').setLabel(**fontCss)
        p2.getAxis('left').setWidth(40)
        setprop_func_route(p2)
        #p2.setLabels(right='斜度(%)')
        p2.setLabel('right', text='斜度', units='%', **styles)
        p2.setXLink(p1)
        
        plt_region = graphics_w.addPlot(row=2, col=0)
        num_of_df = len(df['dist_sum(km)'])
        #self.region.setRegion([df['dist_sum(km)'][num_of_df-math.floor(num_of_df/10)], df['dist_sum(km)'][num_of_df-1]])
        region = pg.LinearRegionItem([0, num_of_df], bounds=[0,100], movable=True) # http://www.pyqtgraph.org/documentation/graphicsItems/linearregionitem.html
        region.setZValue(10)
        setprop_region_route(plt_region)
        plt_region.addItem(region, ignoreBounds=True)
        plt_region.plot(df['dist_sum(km)'],df['Alt(m)'], pen='#fff6')
        plt_region.getAxis('bottom').setLabel(**fontCss)
        plt_region.setLabels(bottom='距離(km)')
        setprop_region_route(plt_region)

        plt_hist = graphics_w.addPlot(row=0, col=1, rowspan=3, colspan=3)
        setprop_hist_route(plt_hist,'頻度','')
        graphics_w.ci.layout.setColumnStretchFactor(0, 3)
        graphics_w.ci.layout.setRowStretchFactor(0, 7)
        graphics_w.ci.layout.setRowStretchFactor(1, 7)
        graphics_w.ci.layout.setRowStretchFactor(2, 1)

        from shapely.geometry import MultiPoint
        def updatePlot():
            p1.setXRange(*region.getRegion(), padding=0)
            minx, maxx = region.getRegion()

            # ヒストグラムの更新更新表示のための計算
            # dfからminx,maxxの範囲を切り出してnpにてヒストグラム用の値を計算
            distindex =df['dist_sum(km)']
            df_range = df[(distindex >= minx) & (distindex <=maxx)]
            slope = df_range['slope(%).mean']
            import math
            resol = (math.ceil(slope.max()) - math.floor(slope.min())) * 16
            y, x = np.histogram(slope, bins=np.linspace(math.floor(slope.min()),math.ceil(slope.max()), resol))
            hist_x = np.delete(x,0)# データが一つ多いので末尾を削除
            # ここで、addItem
            plt_hist.clear() # clearしないと、データが重ね描きされる。
            plt_hist.setAutoVisible(y=True)
            plt_hist.addItem(pg.PlotDataItem(hist_x,y,pen =pen_h,symbolBrush =None,symbolPen=None , symbolSize = 5))
            #df_range, df_analysis = update_df(minx, maxx, df)

            distindex = df['dist_sum(km)']
            df_range = df[(distindex >= minx) & (distindex <= maxx)]
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
