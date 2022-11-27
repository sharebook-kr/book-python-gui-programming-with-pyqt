import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("button1")
        btn1.clicked.connect(self.btn_clicked)

        # vbox
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def btn_clicked(self):
        print("button is clicked")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()