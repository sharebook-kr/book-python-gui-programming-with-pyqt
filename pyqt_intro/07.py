import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        icon = QIcon("icon.png")
        self.setWindowIcon(icon)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()