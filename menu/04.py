import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QAction
)
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.toolbar = self.addToolBar('toolbar')

        self.action1 = QAction(QIcon("home.png"), 'home')
        self.action2 = QAction(QIcon("settings.png"), 'setting')
        self.action3 = QAction(QIcon("envelope.png"), 'envelope')

        self.toolbar.addAction(self.action1)
        self.toolbar.addAction(self.action2)
        self.toolbar.addAction(self.action3)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()