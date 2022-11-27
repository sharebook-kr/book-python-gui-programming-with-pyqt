import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QWidget
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("Name")
        line_edit = QLineEdit()

        # vbox
        vbox = QHBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(line_edit)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()