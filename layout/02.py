import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("button1")
        btn2 = QPushButton("button2")

        layout = QVBoxLayout()      # QVBoxLayout
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()