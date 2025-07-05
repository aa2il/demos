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

# Dynamic importing - this works!
QTLIB='PyQt6'
exec('from '+QTLIB+'.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QApplication,QSizePolicy,'+
     'QPushButton,QMessageBox,QDialog,QVBoxLayout')
exec('from '+QTLIB+'.QtCore import Qt,qVersion,QSize')
exec('from '+QTLIB+'.QtGui import QPalette')    

################################################################################

"""
    def show_dialog(self):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog Box")

        # Create a label with a message
        label = QLabel("This is a message in the dialog box.")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.exec()
"""

class MyDialog(QDialog):
    def __init__(self,msg,title=None):
        super().__init__()

        if title!=None:
            self.setWindowTitle(title)
        #self.setGeometry(100, 100, 300, 150)

        #layout = QVBoxLayout()
        layout = QGridLayout(self)     

        self.label = QLabel(msg)
        layout.addWidget(self.label,0,0,1,2)

        self.btn1 = QPushButton('Yes')
        self.btn1.clicked.connect(self.yes)
        layout.addWidget(self.btn1,1,0)

        self.btn2 = QPushButton('No')
        self.btn2.clicked.connect(self.no)
        layout.addWidget(self.btn2,1,1)

        self.setLayout(layout)

    def yes(self):
        print('Yes')
        self.accept()

    def no(self):
        print('No')
        self.close()

        
    
class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world - "+qVersion()+" Gui")

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
        gridLayout = QGridLayout(self)     

        msg = QLabel("Hello World from "+qVersion(), self)
        if int(qVersion().split('.')[0])>=6:
            msg.setAlignment(Qt.AlignmentFlag.AlignCenter) 
            msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            msg.setAlignment(Qt.AlignCenter) 
            msg.setAlignment(Qt.AlignCenter) 
        gridLayout.addWidget(msg, 0, 0)

        btn = QPushButton('Quit')
        btn.clicked.connect(self.btnCB)
        gridLayout.addWidget(btn, 1, 0)

        centralWidget.setLayout(gridLayout)  
        
    def btnCB(self):
        print('btnCB')

        if True:
            
            # This works on a headless RPi
            dialog = MyDialog('Really Quit?')
            result = dialog.exec()
            print(result)
            if result:
                self.close()

        else:

            # This does not work on a headless RPi accessed via VNC
            # but it is fine if we use ssh -X instead
            msgBox = QMessageBox.question(self,
                                          'Confirmation',
                                          'Do you want to quit?',
                                          QMessageBox.StandardButton.Yes |
                                          QMessageBox.StandardButton.No  )

            if msgBox == QMessageBox.StandardButton.Yes:
                QMessageBox.information( self,
                                         'Information',
                                         'You selected Yes. The program will be terminated.',
                                         QMessageBox.StandardButton.Ok )
                self.close()


if __name__ == "__main__":
    print('QT Version=',qVersion())
    app = QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()

    if int(qVersion().split('.')[0])>=6:
        sys.exit( app.exec() )
    else:
        sys.exit( app.exec_() )

sys.exit(0)
    
"""
    # This is problematic on a headless RPi
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Icon.Information)
    msgBox.setText("Really Quit?")
    msgBox.setWindowTitle("Really Quit")
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

    # Trying to find a kludge - no such luck yet ...
    msgBox.open()
    msgBox.show()

    print('baseSize=',msgBox.baseSize())
    print('frameSize=',msgBox.frameSize())
    print('minSize=',msgBox.minimumSize())
    #print('sizePolicy=',msgBox.sizePolicy)
    print('geometry=',msgBox.geometry())
    print('frameGeometry=',msgBox.frameGeometry())

    sizePolicy = QSizePolicy( QSizePolicy.Policy.Minimum, 
                              QSizePolicy.Policy.Minimum)
    msgBox.setSizePolicy(sizePolicy)
    msgBox.setMinimumSize(200,200)
    print('minSize=',msgBox.minimumSize())
    msgBox.resize(200,200)
    msgBox.move(200,200)

    print('pos=',msgBox.pos())
    print('visible=',msgBox.isVisible())
    msgBox.setVisible(True)
    print('visible=',msgBox.isVisible())
    print('enabled=',msgBox.isEnabled())
    msgBox.setUpdatesEnabled(True)
    

    
    returnValue = msgBox.exec()
    
    if int(qVersion().split('.')[0])>=6:
        sys.exit( app.exec() )
    else:
        sys.exit( app.exec_() )

"""
