import sys

from PyET import settings

from PyQt5 import QtWidgets

from main_ui import TrackerGui

settings.init()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

gui = TrackerGui()
gui.setup_ui(MainWindow)

MainWindow.show()
sys.exit(app.exec_())