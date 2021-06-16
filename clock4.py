#!/usr/bin/python3

import sys
#from PyQt4 import QtCore, QtGui
#from PyQt4.QtGui import QApplication,QLCDNumber
from PyQt5.QtWidgets import QApplication,QLCDNumber
from PyQt5.QtCore import QTimer,QTime

class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)
        self.setDigitCount(8)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(250, 60)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        #if (time.second() % 2) == 0:
        #    text = text[:2] + ' ' + text[3:]

        print('text=',text)
        self.display(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
    
