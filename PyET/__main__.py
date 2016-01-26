import sys

from PyET import PyET

from PyQt5 import QtWidgets

from main_ui import TrackerGui

PyET.PyET.init()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

gui = TrackerGui()
gui.setup_ui(MainWindow)

MainWindow.show()
sys.exit(app.exec_())