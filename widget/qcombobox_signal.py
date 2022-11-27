import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QComboBox,
    QWidget
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        combo_box = QComboBox()
        combo_box.addItem("Python 3.9")
        combo_box.addItem("Python 3.10")
        combo_box.addItem("Python 3.11")
        combo_box.currentTextChanged.connect(self.combo_box_text_changed)

        self.setCentralWidget(combo_box)

    def combo_box_text_changed(self, text):
        print(text)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()