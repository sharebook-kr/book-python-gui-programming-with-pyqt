import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)     # macOS
        menu_file = menubar.addMenu("File")
        menu_help = menubar.addMenu("Help")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()