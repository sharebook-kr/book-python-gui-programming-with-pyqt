import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QAction
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)     # macOS
        menu_file = menubar.addMenu("File")
        menu_help = menubar.addMenu("Help")

        # submenu
        self.action1 = QAction("Close Window")
        self.action2 = QAction("Documentation")

        # insert submenu into the menu
        menu_file.addAction(self.action1)
        menu_help.addAction(self.action2)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()