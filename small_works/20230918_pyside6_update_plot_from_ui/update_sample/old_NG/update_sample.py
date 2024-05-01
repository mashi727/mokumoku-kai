'''
アニメーションのサンプル。
本家ではこんな書き方をするみたい。

'''

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import GraphicsLayoutWidget
from threading import Thread, Event
import time

# Routine to acquire and serve data
# This might be a camera driver, notifying when a new frame is available
def generate_data(callback, threadkill):
    while not threadkill.is_set():
        width = 1600
        data = np.zeros(width)
        data += np.cos(np.arange(0, 10*np.pi, 10*np.pi/width) - 9*time.monotonic())
        data += np.cos(np.arange(0, 4*np.pi, 4*np.pi/width) + 4*time.monotonic())
        callback(data)
        time.sleep(0.01)

class PyQtGraphTest(GraphicsLayoutWidget):

    # Signal to indicate new data acquisition
    # Note: signals need to be defined inside a QObject class/subclass
    data_acquired = Signal(np.ndarray)

    def __init__(self):
    
        super().__init__()

        self.setWindowTitle('Test pyqtgraph paint signals')
        self.resize(640, 400)
        self.plot = self.addPlot()
        self.spectrum = self.plot.plot()
        self.plot.enableAutoRange(pg.ViewBox.XYAxes)
        self.plot.setRange(yRange = (-2.5, 2.5), padding = 0)

        # Connect the signal
        self.data_acquired.connect(self.update_data)

        # Make and start the background thread to acquire data
        # Pass it the signal.emit as the callback function
        self.threadkill = Event()
        self.thread = Thread(target=generate_data, args=(self.data_acquired.emit, self.threadkill))
        self.thread.start()

    # Kill our data acquisition thread when shutting down
    def closeEvent(self, close_event):
        self.threadkill.set()

    # Slot to receive acquired data and update plot
    @Slot(np.ndarray)
    def update_data(self, data):
        self.spectrum.setData(data)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtGraphTest()
    window.show()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        sys.exit(app.exec())