def new_method(self, text='defaultの引数やね'):
    print("i say hello from new_method!!!")
    print(text)

from types import MethodType
MainWindow.new_method = MethodType(new_method, MainWindow)


def data_func(self):
    self.test = "i'm defined in data_func!!!"
    from dataclasses import dataclass
    @dataclass
    class Data:
        degree : float = 45
    print(Data.degree,'in data_func')


from types import MethodType
MainWindow.data_func = MethodType(data_func, MainWindow)


def draw_graph(self):
    print("i'm now in draw_graph!!! in exec CODE!!!")
    # 以下の処理は、timer付きのグラフから他のグラフを表示した際に、timerを止める処置を行う。

    #model_code = self.Ui_MainWindow.codeView.toPlainText()
    #exec(model_code)

from types import MethodType
MainWindow.draw_graph = MethodType(draw_graph, MainWindow)

#text = 'そとからやね'

self.data_func()
self.draw_graph()
self.new_method()

