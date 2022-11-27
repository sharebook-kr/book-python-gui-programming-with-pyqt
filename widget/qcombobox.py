import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        combo_box = QComboBox()
        combo_box.addItem("Python 3.9")
        combo_box.addItem("Python 3.10")
        combo_box.addItem("Python 3.11")

        self.setCentralWidget(combo_box)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()