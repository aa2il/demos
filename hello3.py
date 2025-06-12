#!/usr/bin/env -S uv run --script
#
# OLD: ! /usr/bin/python3
#
################################################################################
#
# A very simple Hello World using Qt
#
################################################################################

import sys
if False:
    from PyQt6 import QtCore, QtWidgets
    from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QApplication
    from PyQt6.QtCore import QSize
    from PyQt6.QtCore import Qt,qVersion
elif True:
    # ... there was a bug in PySide6 and this hangs on exit - is it fixed?
    from PySide6 import QtCore, QtWidgets
    from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QApplication,QMessageBox
    from PySide6.QtCore import QSize
    from PySide6.QtCore import Qt,qVersion
elif False:
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtGui import QMainWindow, QLabel, QGridLayout, QWidget,QApplication
    from PyQt4.QtCore import QSize
    from PyQt4.QtCore import Qt,qVersion
else:
    from PyQt5 import QtCore, QtWidgets
    from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QApplication
    from PyQt5.QtCore import QSize
    from PyQt5.QtCore import Qt,qVersion

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world - "+qVersion()+" Gui")

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  

        title = QLabel("Hello World from "+qVersion(), self)
        if int(qVersion().split('.')[0])>=6:
            title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            title.setAlignment(QtCore.Qt.AlignCenter) 
            title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
    print('QT Version=',qVersion())
    app = QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()

    # This is problematic on a headless RPi
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Icon.Information)
    msgBox.setText("Really Quit?")
    msgBox.setWindowTitle("Really Quit")
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

    # Trying to find a kludge - no such luck yet ...
    msgBox.show()
        
    qr = msgBox.frameGeometry()
    w=qr.width()
    h=qr.height()
    print('qr=',qr,w,h)
    if w<100 or h<100:
        msgBox.resize( max(w,100) , max(h,100) )
        qr = msgBox.frameGeometry()
        w=qr.width()
        h=qr.height()
        print('qr=',qr,w,h)

    returnValue = msgBox.exec()
    
    if int(qVersion().split('.')[0])>=6:
        sys.exit( app.exec() )
    else:
        sys.exit( app.exec_() )

