#! /usr/bin/python3

# Script showing how to update a qt from a non-main thread using signals
# From chatgpt

import sys
import time
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

# 1. Define a worker thread that handles calculations/background tasks
class WorkerThread(QThread):
    # Create signals to pass data back to the main thread
    # The types inside the brackets specify what data types the signal transmits
    progress_updated = pyqtSignal(int)
    task_finished = pyqtSignal(str)

    def run(self):
        """This method runs entirely in the background thread."""
        for i in range(1, 6):
            time.sleep(1) # Simulate a long-running computation or I/O task
            
            # WRONG: self.label.setText(f"Progress: {i}") <- Will crash!
            # RIGHT: Emit a signal with the data instead
            self.progress_updated.emit(i * 20)
            
        self.task_finished.emit("Background task completed successfully!")

# 2. Define the main window running on the main (GUI) thread
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thread-Safe GUI Update")
        self.resize(300, 150)

        # UI Setup
        layout = QVBoxLayout()
        self.label = QLabel("Thread idle...", self)
        self.button = QPushButton("Start Background Task", self)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect button click to launch the thread
        self.button.clicked.connect(self.start_background_thread)

    def start_background_thread(self):
        self.button.setEnabled(False)
        self.label.setText("Starting thread...")

        # Initialize the worker thread
        self.worker = WorkerThread()

        # Connect worker signals to main thread slots (methods)
        self.worker.progress_updated.connect(self.update_gui_progress)
        self.worker.task_finished.connect(self.handle_thread_finished)

        # Start the background execution
        self.worker.start()

    # 3. Main thread slots that safely touch GUI components
    def update_gui_progress(self, percentage):
        """Safely updates the GUI because it's executed by the main thread event loop."""
        self.label.setText(f"Progress: {percentage}%")

    def handle_thread_finished(self, message):
        """Safely finalizes the state and clears the thread."""
        self.label.setText(message)
        self.button.setEnabled(True)
        self.worker.deleteLater() # Clean up thread memory safely

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
