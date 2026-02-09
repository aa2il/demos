#! /usr/bin/python3

# A very simple Hello World using Qt

import sys
from PyQt6.QtWidgets import *       # Exists fine
#from PySide6.QtWidgets import *    # Hangs on exit --> bug in PySide6
from PyQt6.QtCore import Qt,qVersion
from PyQt6.QtGui import QFont

def window():
   app = QApplication(sys.argv)
   w = QWidget()

   print(QFont.__dict__)
   print(dir(QFont))
   font=QFont('Arial',20)
   font.setBold(True)
   
   b = QLabel(w,font=font)
   b.setText("Hello World! - PyQt Gui")

   w.show()
   sys.exit(app.exec())
	
if __name__ == '__main__':
   msg="Hello World! - QT Version ="+qVersion()
   print(msg)
   window()
