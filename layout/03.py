import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("button1")   # button
        btn2 = QPushButton("button2")

        layout = QVBoxLayout()          # QVBoxLayout
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        widget = QWidget()              # QWidget
        widget.setLayout(layout)        # layout을 widget 안으로 배치
        self.setCentralWidget(widget)   # widget을 윈도우 안으로 배치


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()