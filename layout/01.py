import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("button1", self)
        btn1.move(10, 10)

        btn2 = QPushButton("button2", self)
        btn2.move(10, 50)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()