import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QWidget
)
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel()
        pixmap = QPixmap("qt_logo.png")
        label.setPixmap(pixmap)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()