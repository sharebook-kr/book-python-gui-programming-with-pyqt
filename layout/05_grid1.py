import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("button1")   # button
        btn2 = QPushButton("button2")
        btn3 = QPushButton("button3")
        btn4 = QPushButton("button4")

        layout = QGridLayout()
        layout.addWidget(btn1, 0, 0)
        layout.addWidget(btn2, 0, 1)
        layout.addWidget(btn3, 1, 0)
        layout.addWidget(btn4, 1, 1)

        widget = QWidget()              # QWidget
        widget.setLayout(layout)        # layout을 widget 안으로 배치
        self.setCentralWidget(widget)   # widget을 윈도우 안으로 배치

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()