import os
import sys
from PySide6 import QtCore, QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication, QMainWindow


import numpy as np
from PySide6.QtWidgets import QVBoxLayout
import pyqtgraph as pg


from PySide6.QtCore import QTimer

os.environ["PYSIDE_DESIGNER_PLUGINS"]="."
os.environ["QT_LOGGING_RULES"]='*.debug=false;qt.pysideplugin=false'
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.graphWidget = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")

        # QUiLoaderで.uiファイルを読み込む
        self.Ui_MainWindow = QtUiTools.QUiLoader().load("./untitled.ui")
        self.Ui_MainWindow.setWindowTitle("MainWindow Title")
        #self.Ui_MainWindow.setGeometry(50, 50, 2000, 1200) # WQXGA (Wide-QXGA)
        layout = QVBoxLayout()
        #self.Ui_MainWindow.setCentralWidget(self.graphWidget)
        self.Ui_MainWindow.centralwidget.setLayout(layout)
        layout.addWidget(self.graphWidget)
        # tag::plot data: x, y values
        self.plot()


    def update(self):
        global curve, data, ptr, p6
        
        self.curve.setData(self.data[self.ptr%10])
        if self.ptr == 0:
            self.p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.ptr += 1


    def plot(self):
        
        self.p6 = self.graphWidget.addPlot(title="Updating plot")
        self.curve = self.p6.plot(pen='y')
        self.data = np.random.normal(size=(10,1000))
        self.ptr = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)


def main():
    # Qt Applicationを作ります
    app = QApplication(sys.argv)
    # formを作成して表示します
    mainWin = MainWindow()
    mainWin.Ui_MainWindow.show()

    # Qtのメインループを開始します
    sys.exit(app.exec())

if __name__ == '__main__':
    main()