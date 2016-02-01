import sys

import PyET.PyETCore as PyETCore

from PyET.main_ui import TrackerGui

from PyQt5 import QtWidgets

PyETCore.init()

MainWindow = QtWidgets.QMainWindow()

gui = TrackerGui()
gui.setup_ui(MainWindow)

MainWindow.show()
sys.exit(PyETCore.inst.app.exec_())