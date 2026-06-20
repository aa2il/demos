#! /usr/bin/python3

# Example of how to put a radio button in a menu

# Source - https://stackoverflow.com/a/48447711
# Posted by eyllanesc, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-26, License - CC BY-SA 4.0

import sys
#from PyQt5.QtWidgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        menu = self.menuBar()
        paymentType = QMenu('Payment Type', self)
        group = QActionGroup(paymentType)
        texts = ["Cash", "Noncash Payment", "Cash on Delivery", "Bank Transfer"]
        for text in texts:
            action = QAction(text, paymentType, checkable=True, checked=text==texts[0])
            paymentType.addAction(action)
            group.addAction(action)
        group.setExclusive(True)
        group.triggered.connect(self.onTriggered)
        menu.addMenu(paymentType)

    def onTriggered(self, action):
        print(action.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
