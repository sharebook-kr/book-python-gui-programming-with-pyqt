import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("button1")
        btn2 = QPushButton("button2")
        btn3 = QPushButton("button3")
        btn4 = QPushButton("button4")
        btn5 = QPushButton("button5")

        # left vbox
        left_vbox = QVBoxLayout()
        left_vbox.addWidget(btn1)
        left_vbox.addWidget(btn2)
        left_vbox.addWidget(btn3)

        # right vbox
        right_vbox = QVBoxLayout()
        right_vbox.addWidget(btn4)
        right_vbox.addWidget(btn5)

        # outer hbox
        hbox = QHBoxLayout()
        hbox.addLayout(left_vbox)
        hbox.addLayout(right_vbox)

        widget = QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()