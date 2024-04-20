def setprop(graph_object, name_of_xaxis='', name_of_yaxis=''):
    """
    グラフ表示のプロパティを設定する。
    
    Parameters
    ----------
    graph_object : グラフのインスタンス名
        対象とするグラフのインスタンスを指定
    location_id : int
        対象地域のマスタID。
    """
    styles = {'color':'white',
                    'font-size':'24px',
                    'font-style':'bold',
                    'font-family': 'Helvetica, MeiryoKe_Console'
                    }
    graph_object.enableAutoRange(False)
    graph_object.showAxis('right')
    graph_object.showAxis('left')
    #graph_object.showAxis('top')
    #graph_object.getAxis('top').setHeight(50)
    #graph_object.getAxis('bottom').setHeight(50)
    graph_object.getAxis('right').setWidth(60)
    graph_object.getAxis('left').setWidth(60)
    graph_object.showGrid(x=True, y=True, alpha = 1)
    graph_object.setAutoVisible(y=True)
    #graph_object.addLegend(offset=(10,10))
    graph_object.setLabel('left'  , text=name_of_yaxis, units='', **styles)
    graph_object.setLabel('bottom', text=name_of_xaxis, units='', **styles)
    #graph_object.setLabel('right'  , text='y', units='', **styles)
    #graph_object.setLabel('top', text='x', units='', **styles)

def setprop_func(plt):
    fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}
    plt.showGrid(x=True, y=True, alpha=0.5),
    plt.setAutoVisible(y=True),
    #plt.getAxis('top').setLabel(**fontCss),
    plt.setAutoVisible(y=True),
    plt.enableAutoRange('y'),
    plt.showAxis('right'),
    plt.hideAxis('left'),
    plt.getAxis('right'),
    plt.addLegend(offset=(-100,-100)) # legendには、nameが必要

def setprop_stock_func(plt):
    fontCss = {'font-family': "Arial, Meiryo", 'font-size': '16pt'}
    plt.showGrid(x=True, y=True, alpha=0.5),
    plt.getAxis('right').setWidth(75),
    plt.setAutoVisible(y=True),
    plt.enableAutoRange('y'),
    plt.showAxis('right'),
    plt.hideAxis('left'),
    plt.getAxis('right'),
    plt.addLegend(offset=(0,0)) # legendには、nameが必要

setprop_stock = lambda x: (x.showGrid(x=True, y=True, alpha=0.75),
                                x.getAxis('right').setWidth(75),
                                x.setAutoVisible(y=True),
                                x.enableAutoRange('y'),
                                x.showAxis('right'),
                                x.hideAxis('left'),
                                x.addLegend(),
                                x.getAxis('right'),
                                )
'''
setprop = lambda x: (x.showGrid(x=True, y=True, alpha=0.75),
                                x.setAutoVisible(y=True),
                                x.enableAutoRange('y'),
                                x.showAxis('right'),
                                x.hideAxis('left'),
                                x.getAxis('right'),
                                x.addLegend(),
                                )
'''


setprop_region = lambda x: (x.setAutoVisible(y=True),
                        x.getAxis('right').setWidth(50),
                        x.enableAutoRange('y'),
                        x.hideAxis('right'),
                        x.hideAxis('left'), 
                        x.addLegend(),
                        )


setprop_route = lambda x: (x.showGrid(x=True, y=True, alpha=0.75),
                       x.showAxis('right'),
                       x.hideAxis('left'),
                       x.setAutoVisible(y=True))

setprop_region_route = lambda x: (x.setAutoVisible(y=True),
                       x.getAxis('right').setWidth(50),
                       x.getAxis('left').setWidth(20),
                       x.enableAutoRange('y'),
                       x.showAxis('right'),
                       x.hideAxis('left'),
                       x.addLegend(),
                       )


def setprop_hist_route(graph_object, name_of_xaxis='', name_of_yaxis=''):
    """
    グラフ表示のプロパティを設定する。
    
    Parameters
    ----------
    graph_object : グラフのインスタンス名
        対象とするグラフのインスタンスを指定
    location_id : int
        対象地域のマスタID。
    """
    styles = {'color':'white',
                    'font-size':'24px',
                    'font-style':'bold',
                    'font-family': 'Helvetica, MeiryoKe_Console'
                    }
    fontCss = {'font-family': "Arial", 'font-size': '16pt'}
    graph_object.enableAutoRange(False)
    graph_object.showAxis('right')
    graph_object.showAxis('left')
    #graph_object.showAxis('top')
    #graph_object.getAxis('top').setHeight(50)
    #graph_object.getAxis('bottom').setHeight(50)
    graph_object.getAxis('right').setWidth(10)
    graph_object.getAxis('left').setWidth(10)
    graph_object.showGrid(x=True, y=True, alpha = 1)
    graph_object.setAutoVisible(y=True)
    #graph_object.addLegend(offset=(10,10))
    graph_object.setLabel('left'  , text=name_of_yaxis, units='', **styles)
    graph_object.setLabel('bottom', text=name_of_xaxis, units='', **styles)



def setprop_func_route(plt):
    styles = {'color':'white',
                    'font-size':'24px',
                    'font-style':'bold',
                    'font-family': 'Helvetica, MeiryoKe_Console'
                    }
    fontCss = {'font-family': "Arial", 'font-size': '16pt'}
    #plt.getAxis('top').setHeight(50)
    #plt.getAxis('bottom').setHeight(50)
    plt.getAxis('right').setWidth(50)
    plt.getAxis('left').setWidth(20)
    plt.showGrid(x=True, y=True, alpha=0.7),
    plt.setAutoVisible(y=True),
    #plt.getAxis('top').setLabel(**fontCss),
    #plt.getAxis('bottom').setLabel(**fontCss),
    #plt.getAxis('left').setLabel(**fontCss),
    plt.getAxis('right').setLabel(**styles),
    plt.setAutoVisible(y=True),
    plt.enableAutoRange('y'),
    plt.showAxis('right'),
    plt.hideAxis('left'),
    #plt.getAxis('right'),
    plt.addLegend(offset=(-200,-200)) # legendには、nameが必要

