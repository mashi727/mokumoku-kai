from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileSystemModel,	QWidget
from PySide6.QtGui import *
from PySide6 import QtWidgets
# Only needed for access to command line arguments

import sys
import time
import pandas as pd
import numpy as np
from math import sin, cos, acos, asin, atan2, radians, degrees
from Ui_GLW_Map2 import Ui_MainWindow

import folium
from folium import plugins
import io

import timeit

from shapely.geometry import MultiPoint


#from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel,QVBoxLayout, QWidget
#from PyQt5 import uic

import pyqtgraph as pg  # import PyQtGraph after Qt

# 自作のライブラリ
from commands.make_tableview_mode import *

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

setprop = lambda x: (x.showGrid(x=True, y=True, alpha=0.75),
                       x.showAxis('right'),
                       x.hideAxis('left'),
                       x.setAutoVisible(y=True))

setprop_region = lambda x: (x.setAutoVisible(y=True),
                       x.getAxis('right').setWidth(60),
                       x.getAxis('left').setWidth(50),
                       x.enableAutoRange('y'),
                       x.showAxis('right'),
                       x.hideAxis('left'),
                       x.addLegend(),
                       )

def setprop_func(plt):
    fontCss = {'font-family': "Arial", 'font-size': '16pt'}
    plt.showGrid(x=True, y=True, alpha=0.7),
    plt.setAutoVisible(y=True),
    plt.getAxis('top').setLabel(**fontCss),
    plt.setAutoVisible(y=True),
    plt.enableAutoRange('y'),
    plt.getAxis('right').setWidth(65)
    plt.showAxis('right'),
    #plt.hideAxis('left'),
    plt.getAxis('right'),
    plt.addLegend(offset=(-200,-200)) # legendには、nameが必要


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()
        self.glw1 = self.graphicsView1
        self.glw2 = self.graphicsView2
        #self.plotArea()

        # pathを引数にて指定
        try:
            path = sys.argv[1]
        except IndexError:
            path = './data'
        
        self.filepath1 = []
        self.filepath2 = []
        self.model = QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setNameFilters(['*.csv']) # この設定だけだと、非該当の拡張子はグレー表示
        self.model.setNameFilterDisables(False) # 上記フィルターに該当しないファイルは非表示

        self.start_point1 = None
        self.start_point2 = None
        self.goal_point1 = None
        self.goal_point2 = None
        
        view1 = self.treeView1
        view1.setModel(self.model)
        view1.setRootIndex(self.model.index(path))
        view1.setColumnWidth(0,260)
        view1.clicked.connect(self.getFileName1)
        view1.clicked.connect(self.graphPlot1)


        view2 = self.treeView2
        view2.setModel(self.model)
        view2.setRootIndex(self.model.index(path))
        view2.setColumnWidth(0,260)
        view2.clicked.connect(self.getFileName2)
        view2.clicked.connect(self.graphPlot2)

        self.pushButton.clicked.connect(self.get_map_profile)

    def init_ui(self):
        self.setGeometry(50, 50, 1700, 1560) # WQXGA (Wide-QXGA)
        self.fontCssLegend = '<style type="text/css"> p {font-family: Arial;font-size: 16pt; color: "#FFF"} </style>'


    def getFileName1(self, index):
        try:
            import os
            indexItem = self.model.index(index.row(), 0, index.parent())#print(indexItem)
            if os.path.isfile(self.model.filePath(indexItem)):
                self.filepath1.insert(0,self.model.filePath(indexItem))
                #print('File Path :',self.filepath[0],type(self.filepath[0]))
                self.filename1 = self.filepath1[0]
                #self.df1 = self.make_df(self.filepath1[0])
                #print(self.df1)
            else:
                pass
                #QMessageBox.warning(None, "Notice!", "Select File!",QMessageBox.Yes)
        except AttributeError as e:
            pass

    def getFileName2(self, index):
        try:
            import os
            indexItem = self.model.index(index.row(), 0, index.parent())#print(indexItem)
            if os.path.isfile(self.model.filePath(indexItem)):
                self.filepath2.insert(0,self.model.filePath(indexItem))
                self.filename2 = self.filepath2[0]
            else:
                pass
                #QMessageBox.warning(None, "Notice!", "Select File!",QMessageBox.Yes)
        except AttributeError as e:
            pass

    def graphPlot1(self):
        self.glw1.clear()
        # Plotエリアの確保
        dist = self.glw1.addPlot(row=0, col=0)
        slope = self.glw1.addPlot(row=1, col=0)
        plt_region = self.glw1.addPlot(row=2, col=0)
        plt_hist = self.glw1.addPlot(row=0, col=1, rowspan=3)
        self.glw1.ci.layout.setColumnStretchFactor(0, 3)
        self.glw1.ci.layout.setRowStretchFactor(0, 10)
        self.glw1.ci.layout.setRowStretchFactor(1, 10)
        self.glw1.ci.layout.setRowStretchFactor(2, 1)

        last_region = []

        df1, self.start1, self.goal1, self.start_point1 , self.goal_point1 = make_df(self.filename1)
        self.df1 = df1

        fontCss = {'font-family': "Arial", 'font-size': '16pt'}
        fontCss["color"] = '#fff'

        pen_dist = pg.mkPen(color='#00849c', width=5)
        dist.plot(x=df1['dist_sum(km)'],
                    y=df1['Alt(m)'],
                    name= self.fontCssLegend +'<p>Dist.(km)</p>',
                    pen=pen_dist,
                    )
        dist.getAxis('right').setLabel(**fontCss)
        dist.getAxis('left').setWidth(40)
        #dist.hideAxis('bottom'),
        dist.setLabels(right='高度(m)')
        setprop_func(dist)
        self.dist = dist

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

        slope.plot(x=df1['dist_sum(km)'],
                    y=df1['slope(%).mean'],
                    name= self.fontCssLegend +'<p>Slope(%)</p>',
                    pen=pen,
                    #brush=brush,
                    )
        slope.getAxis('right').setLabel(**fontCss)
        slope.getAxis('left').setWidth(40)
        slope.setLabels(right='斜度(%)')
        slope.setXLink(dist)
        setprop_func(slope)
        self.slope = slope


        region = pg.LinearRegionItem() #http://www.pyqtgraph.org/documentation/graphicsItems/linearregionitem.html

        plt_region.addItem(region, ignoreBounds=True)
        plt_region.plot(df1['dist_sum(km)'],df1['Alt(m)'], pen='#fff6')
        plt_region.getAxis('bottom').setLabel(**fontCss)
        plt_region.setLabels(bottom='距離(km)')
        setprop_region(plt_region)
        self.region = region


        # Histogram
        setprop(plt_hist)
        # addItem()は、下から。
        self.plt_hist = plt_hist
        plt_hist.getAxis('bottom').setLabel(**fontCss)
        plt_hist.setLabels(bottom='斜度(%)')
        plt_hist.getAxis('right').setLabel(**fontCss)
        plt_hist.setLabels(right='頻度(回)')
        plt_hist.setAutoVisible(y=True)


        self.region.sigRegionChanged.connect(self.update_region_change)


        if last_region == []: # 初めてプロットするときのRegion
            # for df.sort_index(axis=0, level=None, ascending=True)
            self.region.setRegion([self.start1, self.goal1])
        else:
            self.region.setRegion(last_region) # メイン画面のSMAの値を変更した際のRegion




    def graphPlot2(self):
        self.glw2.clear()
        # Plotエリアの確保
        dist2 = self.glw2.addPlot(row=0, col=0)
        slope = self.glw2.addPlot(row=1, col=0)
        plt_region2 = self.glw2.addPlot(row=2, col=0)
        plt_hist2 = self.glw2.addPlot(row=0, col=1, rowspan=3)
        self.glw2.ci.layout.setColumnStretchFactor(0, 3)
        self.glw2.ci.layout.setRowStretchFactor(0, 10)
        self.glw2.ci.layout.setRowStretchFactor(1, 10)
        self.glw2.ci.layout.setRowStretchFactor(2, 1)

        last_region2 = []
        df2, self.start2, self.goal2, self.start_point2, self.goal_point2 = make_df(self.filename2)
        self.df2 = df2

        fontCss = {'font-family': "Arial", 'font-size': '16pt'}
        fontCss["color"] = '#fff'

        pen_dist = pg.mkPen(color='#00849c', width=5)
        dist2.plot(x=df2['dist_sum(km)'],
                    y=df2['Alt(m)'],
                    name= self.fontCssLegend +'<p>Dist.(km)</p>',
                    pen=pen_dist,
                    )
        dist2.getAxis('right').setLabel(**fontCss)
        dist2.getAxis('left').setWidth(40)
        #dist.hideAxis('bottom'),
        dist2.setLabels(right='高度(m)')
        setprop_func(dist2)
        self.dist2 = dist2

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

        slope.plot(x=df2['dist_sum(km)'],
                    y=df2['slope(%).mean'],
                    name= self.fontCssLegend +'<p>Slope(%)</p>',
                    pen=pen,
                    #brush=brush,
                    )
        slope.getAxis('right').setLabel(**fontCss)
        slope.getAxis('left').setWidth(40)
        slope.setLabels(right='斜度(%)')
        slope.setXLink(dist2)
        setprop_func(slope)
        self.slope = slope


        region2 = pg.LinearRegionItem() #http://www.pyqtgraph.org/documentation/graphicsItems/linearregionitem.html

        plt_region2.addItem(region2, ignoreBounds=True)
        plt_region2.plot(df2['dist_sum(km)'],df2['Alt(m)'], pen='#fff6')
        plt_region2.getAxis('bottom').setLabel(**fontCss)
        plt_region2.setLabels(bottom='距離(km)')
        setprop_region(plt_region2)
        self.region2 = region2


        # Histogram
        setprop(plt_hist2)
        # addItem()は、下から。
        self.plt_hist2 = plt_hist2
        plt_hist2.getAxis('bottom').setLabel(**fontCss)
        plt_hist2.setLabels(bottom='斜度(%)')
        plt_hist2.getAxis('right').setLabel(**fontCss)
        plt_hist2.setLabels(right='頻度(回)')
        plt_hist2.setAutoVisible(y=True)


        self.region2.sigRegionChanged.connect(self.update_region2_change)


        if last_region2 == []: # 初めてプロットするときのRegion
            # for df.sort_index(axis=0, level=None, ascending=True)
            self.region2.setRegion([self.start2, self.goal2])
        else:
            self.region2.setRegion(last_region2) # メイン画面のSMAの値を変更した際のRegion



    def mapPlot(self,center_of_interest):
        route_pos1 = LatLongData(self.df1)
        self.m = folium.Map(
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
        self.plane_line = folium.PolyLine(
            route_pos1,
            weight=8,
            color="#0086CC", 
            #color="#e4041c",
        )
        self.m.add_child(self.plane_line)
        
        plugins.MiniMap().add_to(self.m)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.mapWidget.setHtml(data.getvalue().decode())

    def mapPlot2(self,center_of_interest):
        route_pos2 = LatLongData(self.df2)
        self.m = folium.Map(
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
        self.plane_line = folium.PolyLine(
            route_pos2,
            weight=8,
            color="#0086CC", 
            #color="#e4041c",
        )
        from map_center_coord import MapCenterCoord
        MapCenterCoord().add_to(self.m)
        self.m.add_child(self.plane_line)
        plugins.MiniMap().add_to(self.m)
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.mapWidget.setHtml(data.getvalue().decode())


    def update_region_change(self, region):
        region.setZValue(10)
        minX, maxX = region.getRegion()
        self.dist.setXRange(minX, maxX, padding=0)

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
        route_pos_region = LatLongData(df_range)
        
        df_range.reset_index()
        start_point = (df_range['Lat'][0],df_range['Long'][0])
        goal_point = (df_range['Lat'][len(df_range)-1],df_range['Long'][len(df_range)-1])
        points = MultiPoint([start_point, goal_point])
        center_of_interest = (points.centroid.x, points.centroid.y)
        
        '''
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

        self.mapPlot(center_of_interest)
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


    def update_region2_change(self, region):
        region.setZValue(10)
        minX, maxX = region.getRegion()
        self.dist2.setXRange(minX, maxX, padding=0)
        self.rangeDist = [minX, maxX]

        # ヒストグラムの更新更新表示のための計算
        # dfからminx,maxxの範囲を切り出してnpにてヒストグラム用の値を計算
        distindex =self.df2['dist_sum(km)']
        df_range = self.df2[(distindex >= minX) & (distindex <=maxX)]
        print(minX, maxX)
        slope = df_range['slope(%).mean']
        import math
        resol = (math.ceil(slope.max()) - math.floor(slope.min())) * 16
        y, x = np.histogram(slope, bins=np.linspace(math.floor(slope.min()),math.ceil(slope.max()), resol))
        hist_x = np.delete(x,0)# データが一つ多いので末尾を削除
        # ここで、addItem
        self.plt_hist2.clear() # clearしないと、データが重ね描きされる。
        self.plt_hist2.setAutoVisible(y=True)
        self.plt_hist2.addItem(pg.PlotDataItem(hist_x,y,pen =self.pen_h,symbolBrush =None,symbolPen=None , symbolSize = 5))
        #df_range, df_analysis = update_df(minX, maxX, self.df2)
        distindex = self.df2['dist_sum(km)']
        df_range = self.df2[(distindex >= minX) & (distindex <= maxX)]
        route_pos_region = LatLongData(df_range)

        df_range = df_range.reset_index(drop=True)
        #print(df_range)
        start_point = (df_range['Lat'][0],df_range['Long'][0])
        goal_point = (df_range['Lat'][len(df_range)-1],df_range['Long'][len(df_range)-1])
        print(start_point, goal_point)
        points = MultiPoint([start_point, goal_point])
        center_of_interest = (points.centroid.x, points.centroid.y)


        '''
        if self.start_point1 ==None:
            points = MultiPoint([self.start_point2, self.goal_point2])
            center_of_interest = (points.centroid.x, points.centroid.y)
        elif self.start_point2 == None:
            points = MultiPoint([self.start_point1, self.goal_point1])
            center_of_interest = (points.centroid.x, points.centroid.y)
        else:
            points = MultiPoint([self.start_point2, self.goal_point2])
            #points = MultiPoint([self.start_point1, self.goal_point1, self.start_point2, self.goal_point2])
            center_of_interest = (points.centroid.x, points.centroid.y)
        '''

        self.mapPlot2(center_of_interest)


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




def main():
    #import qdarktheme
    app = QApplication(sys.argv)
    # Apply dark theme to Qt application
    #app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()
    window.show()
    app.exec()

if __name__== '__main__':
    main()

