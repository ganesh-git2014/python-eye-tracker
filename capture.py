# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rcbyron\Documents\Workspace\py\python-eye-tracker\capture.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 663)
        MainWindow.setMinimumSize(QtCore.QSize(720, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cam_view = QtWidgets.QLabel(self.centralwidget)
        self.cam_view.setMinimumSize(QtCore.QSize(720, 480))
        self.cam_view.setAlignment(QtCore.Qt.AlignCenter)
        self.cam_view.setObjectName("cam_view")
        self.horizontalLayout.addWidget(self.cam_view)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 274, 602))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_cap_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.start_cap_btn.setObjectName("start_cap_btn")
        self.verticalLayout.addWidget(self.start_cap_btn)
        self.stop_cap_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_cap_btn.sizePolicy().hasHeightForWidth())
        self.stop_cap_btn.setSizePolicy(sizePolicy)
        self.stop_cap_btn.setObjectName("stop_cap_btn")
        self.verticalLayout.addWidget(self.stop_cap_btn)
        self.calibrate_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.calibrate_btn.setObjectName("calibrate_btn")
        self.verticalLayout.addWidget(self.calibrate_btn)
        self.cam_view_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.cam_view_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.cam_view_label.setObjectName("cam_view_label")
        self.verticalLayout.addWidget(self.cam_view_label)
        self.cam_view_combo_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.cam_view_combo_box.setObjectName("cam_view_combo_box")
        self.verticalLayout.addWidget(self.cam_view_combo_box)
        self.seeing_cam_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.seeing_cam_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.seeing_cam_label.setObjectName("seeing_cam_label")
        self.verticalLayout.addWidget(self.seeing_cam_label)
        self.seeing_cam_combo_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.seeing_cam_combo_box.setObjectName("seeing_cam_combo_box")
        self.verticalLayout.addWidget(self.seeing_cam_combo_box)
        self.seeing_res_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seeing_res_label.sizePolicy().hasHeightForWidth())
        self.seeing_res_label.setSizePolicy(sizePolicy)
        self.seeing_res_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.seeing_res_label.setObjectName("seeing_res_label")
        self.verticalLayout.addWidget(self.seeing_res_label)
        self.seeing_res_combo_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.seeing_res_combo_box.setObjectName("seeing_res_combo_box")
        self.verticalLayout.addWidget(self.seeing_res_combo_box)
        self.eye_cam_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.eye_cam_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.eye_cam_label.setObjectName("eye_cam_label")
        self.verticalLayout.addWidget(self.eye_cam_label)
        self.eye_cam_combo_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.eye_cam_combo_box.setObjectName("eye_cam_combo_box")
        self.verticalLayout.addWidget(self.eye_cam_combo_box)
        self.eye_res_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.eye_res_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.eye_res_label.setWordWrap(False)
        self.eye_res_label.setObjectName("eye_res_label")
        self.verticalLayout.addWidget(self.eye_res_label)
        self.eye_res_combo_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.eye_res_combo_box.setObjectName("eye_res_combo_box")
        self.verticalLayout.addWidget(self.eye_res_combo_box)
        self.spacer_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.spacer_label.setText("")
        self.spacer_label.setObjectName("spacer_label")
        self.verticalLayout.addWidget(self.spacer_label)
        self.toggle_gui_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.toggle_gui_btn.setObjectName("toggle_gui_btn")
        self.verticalLayout.addWidget(self.toggle_gui_btn)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_coming_soon = QtWidgets.QAction(MainWindow)
        self.action_coming_soon.setObjectName("action_coming_soon")
        self.action_coming_soon_2 = QtWidgets.QAction(MainWindow)
        self.action_coming_soon_2.setObjectName("action_coming_soon_2")
        self.menuFile.addAction(self.action_coming_soon)
        self.menuAbout.addAction(self.action_coming_soon_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.start_cap_btn.released.connect(self.cam_view.show)
        self.stop_cap_btn.pressed.connect(self.cam_view.hide)
        self.cam_view_combo_box.activated['int'].connect(self.cam_view.update)
        self.seeing_cam_combo_box.activated['int'].connect(self.cam_view.update)
        self.eye_cam_combo_box.activated['int'].connect(self.cam_view.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Eye Capture"))
        self.cam_view.setText(_translate("MainWindow", "(camera view)"))
        self.start_cap_btn.setText(_translate("MainWindow", "Start Capture (F5)"))
        self.stop_cap_btn.setText(_translate("MainWindow", "Stop Capture (F6)"))
        self.calibrate_btn.setText(_translate("MainWindow", "Calibrate Eye Camera"))
        self.cam_view_label.setText(_translate("MainWindow", "Camera View:"))
        self.seeing_cam_label.setText(_translate("MainWindow", "Seeing Camera:"))
        self.seeing_res_label.setText(_translate("MainWindow", "Seeing Camera Resolution:"))
        self.eye_cam_label.setText(_translate("MainWindow", "Eye Camera:"))
        self.eye_res_label.setText(_translate("MainWindow", "Eye Camera Resolution:"))
        self.toggle_gui_btn.setText(_translate("MainWindow", "Toggle GUI (F7)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_coming_soon.setText(_translate("MainWindow", "(coming soon!)"))
        self.action_coming_soon_2.setText(_translate("MainWindow", "(coming soon!)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
