#! /usr/bin/python3

# Fun with the keyboard - how to capture key events in Qt

"""
Key Qt::Key Constants 
These are constants used within QKeyEvent or keyPressEvent to detect specific keys: 
Alphanumeric: Qt::Key_0 through Qt::Key_9, Qt::Key_A through Qt::Key_Z.
Navigation: Qt::Key_Up, Qt::Key_Down, Qt::Key_Left, Qt::Key_Right, Qt::Key_PageUp, Qt::Key_PageDown, Qt::Key_Home, Qt::Key_End.
Editing/Modifier Keys: Qt::Key_Escape, Qt::Key_Tab, Qt::Key_Backspace, Qt::Key_Return, Qt::Key_Enter, Qt::Key_Insert, Qt::Key_Delete, Qt::Key_Shift, Qt::Key_Control, Qt::Key_Alt, Qt::Key_Meta.
Function Keys: Qt::Key_F1 through Qt::Key_F35. 
Using Key Codes in Qt 
C++ (QKeyEvent): event->key() returns the Qt::Key enum, while event->modifiers() identifies Shift, Ctrl, or Alt.
Python (PySide/PyQt): Accessed similarly, e.g., if event.key() == Qt.Key_Escape:.
QML (Keys Type): Handled using attached properties like Keys.onPressed: { if (event.key === Qt.Key_A) ... }. 
Modifier Constants 
Keyboard modifiers are used alongside key codes to detect combinations: 
Qt::ControlModifier: Ctrl key.
Qt::AltModifier: Alt key.
Qt::ShiftModifier: Shift key.
Qt::MetaModifier: Meta/Windows key.
Qt::KeypadModifier: Keypad button. 
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

#from PySide6.QtWidgets import *
#from PySide6.QtCore import *
#from PySide6.QtGui import *

#from PyQt6.QtWidgets import *
#from PyQt6.QtCore import *
#from PyQt6.QtGui import *

"""

# This one works 
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        print('key=',e.key(),e.text())
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

"""   
"""

class Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout(self)
        self.label1 = QLabel("", self)
        self.label2 = QLabel("Key Pressed: ", self)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label1)
        self.resize(100,50)
        self.eventFilter = KeyPressFilter(parent=self)
        self.installEventFilter(self.eventFilter)

class KeyPressFilter(QObject):

    def eventFilter(self, widget, event):
        print('event=',event)
        if event.type() == QEvent.KeyPress:
            text = event.text()
            if event.modifiers():
                text = event.keyCombination().key().name.decode(encoding="utf-8")
            widget.label1.setText(text)
        return False

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

"""
"""
    
# This one also works!
class KeyboardEventApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keyboard Event Example")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.key_label = QLabel("Last Key Pressed: None", self.central_widget)
        self.key_label.setGeometry(10, 10, 200, 30)

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            self.key_label.setText(f"Last Key Pressed: {key_text}")

    def keyReleaseEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            self.key_label.setText(f"Key Released: {key_text}")

def main():
    app = QApplication(sys.argv)
    window = KeyboardEventApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

"""

# This one also works (after a bit of fiddling)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space.value:
            self.test_method('Space Bar')
        elif event.key() == Qt.Key.Key_Up.value:
            self.test_method('Up Arrow')
        elif event.key() == Qt.Key.Key_Down.value:
            self.test_method('Down Arrow')
        elif event.key() == Qt.Key.Key_Left.value:
            self.test_method('Left Arrow')
        elif event.key() == Qt.Key.Key_Right.value:
            self.test_method('Right Arrow')
        elif event.key() == Qt.Key.Key_Escape.value:
            self.test_method('Escape')
            self.close()
            
    def test_method(self,txt):
        print(txt,'was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    demo = MainWindow()
    demo.show()
    
    sys.exit(app.exec())

"""
"""
