import sys

from PyQt5 import QtWidgets
from main_ui import TrackerGui

import PyET

PyET.init()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

gui = TrackerGui()
gui.setup_ui(MainWindow)

MainWindow.show()
sys.exit(app.exec_())