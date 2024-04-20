class MainWindow(object):
    main_name = "i'm now in MainWindow!!"
    def __init__(self):
        print('1st')
        self.test = 'self test'
        from dataclasses import dataclass
        @dataclass
        class Data:
            from_main_dataclass : str = "i'm now in main dataclass"
        
    def run(self):
        print('run')
        print(self.test)

    
class DataViz(MainWindow):
    sub_name = "i'm now in DataViz"
    def __init__(self):
        super(MainWindow, self).__init__()

    def auto_run(self):
        print('auto run')

    def run2(self):
        print('super fast')
        print(MainWindow.)
    

    from dataclasses import dataclass
    @dataclass
    class Data:
        from_dataclass : str = "i'm now in dataclass"

    class DataPlot():
        def __init__(self):
            pass
        def runrun(self):
            print('runrun')
            print(DataViz.Data.from_dataclass)
            print(DataViz.sub_name)
            print(MainWindow.main_name)

mainwin = MainWindow()
mainwin.run()

dataviz = DataViz()
dataviz.run2()

win = DataViz.DataPlot()
win.runrun()