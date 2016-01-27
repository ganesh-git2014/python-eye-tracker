import sys

import PyET.PyETCore as PyETCore

from PyET.main_ui import TrackerGui

from PyQt5 import QtWidgets

PyETCore.init()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

gui = TrackerGui()
gui.setup_ui(MainWindow)

MainWindow.show()
sys.exit(app.exec_())