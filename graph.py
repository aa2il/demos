#!/usr/bin/env -S uv run --script
#
# OLD: ! /usr/bin/python3
#
################################################################################
#
# Simple graph example
#
# This shows the problem with using pyqtgraph with pyside6 under uv
#
################################################################################

import sys
import contextlib
import importlib
import pyqtgraph as pg
#from pyqtgraph import Qt

import importlib.metadata

# Function to sort out which of the Qt front ends are available
def FindQtFrontEnds2():
    frontends = {'PyQt6' : False,
                 'PySide6' : False,
                 'PyQt5' : False,
                 'PySide2' : False }
    
    for frontend in frontends.keys():
        try:
            print(frontend+' version=',importlib.metadata.version(frontend))
            frontends[frontend] = True
            return frontend
        except:
            print(frontend+' not found')
    print('frontends=',frontends)

if False:
    # This works
    from PyQt6.QtWidgets import QApplication, QMainWindow
elif True:
    # Dynamic importing - this works!
    QTLIB=FindQtFrontEnds2()
    print(QTLIB)
    exec('from '+QTLIB+'.QtWidgets import QApplication, QMainWindow')
elif False:
    # Moving toward dynamic importing
    QTLIB=pg.Qt.QT_LIB+".QtWidgets"
    print(QTLIB)
    #from QT_LIB import QApplication, QMainWindow
    module = importlib.import_module(QTLIB)
    QMainWindow = getattr(module,'QMainWindow')
    QApplication = getattr(module,'QApplication')
    #print(method)
else:
    # This doesn't
    from PySide6.QtWidgets import QApplication, QMainWindow


# Function to sort out which of the Qt front ends are available
def FindQtFrontEnds():
    print('Qt.QT_LIB=',pg.Qt.QT_LIB)

    frontends = {
        pg.Qt.PYQT5: False,
        pg.Qt.PYQT6: False,
        pg.Qt.PYSIDE2: False,
        pg.Qt.PYSIDE6: False,
    }
    
    for frontend in frontends.keys():
        with contextlib.suppress(ImportError):
            importlib.import_module(frontend)
            frontends[frontend] = True
    print('frontends=',frontends)
FindQtFrontEnds()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
