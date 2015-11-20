'''
Created on Nov 10, 2015

@author: rcbyron
'''

import sys, cv2, time
from PyQt5.QtWidgets import (QWidget, QToolTip, QMessageBox, QPushButton, QApplication, QLabel, QGridLayout)
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap, qRgb
from PyQt5.QtCore import QCoreApplication

GUI_TITLE = "Python Eye Tracker 6000 GUI"

import numpy as np

gray_color_table = [qRgb(i, i, i) for i in range(256)]

def toQImage(im, copy=False):
    if im is None:
        print("image passed is none yo")
        return QImage()

    if im.dtype == np.uint8:
        if len(im.shape) == 2:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim.copy() if copy else qim

        elif len(im.shape) == 3:
            if im.shape[2] == 3:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888);
                return qim.copy() if copy else qim
            elif im.shape[2] == 4:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32);
                return qim.copy() if copy else qim

    raise Exception


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.webcam_display_label = QtWidgets.QLabel(self.centralwidget)
        self.webcam_display_label.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.webcam_display_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.webcam_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.webcam_display_label.setObjectName("webcam_display_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Webcam = QtWidgets.QAction(MainWindow)
        self.actionOpen_Webcam.setCheckable(True)
        self.actionOpen_Webcam.setChecked(True)
        self.actionOpen_Webcam.setObjectName("actionOpen_Webcam")
        self.menuFile.addAction(self.actionOpen_Webcam)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpen_Webcam.toggled.connect(self.show_movie)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Eye Capture 6000"))
        self.webcam_display_label.setText(_translate("MainWindow", "(Webcam Display)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Webcam.setText(_translate("MainWindow", "Open Webcam"))
        
    def show_movie(self):
        print("SHOWING MOVIE!")
        frame = cv2.imread('Koala.jpg',0)
        
        #height, width = frame.shape
        #byteValue = byteValue * width
    
        #reg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        #cv2.imshow('frame',reg)
        #mimage = QImage(frame.tostring(), width, height, QImage.Format_RGB888).rgbSwapped()
        
        
        #image = QImage(frame, frame.width, frame.height, QImage.Format_RGB888).rgbSwapped()
        #mimage = toQImage(frame, False)
        #pixmap = QPixmap.fromImage(mimage) # This line causes error (found out by running in console)
        #self.movie_screen.setPixmap(pixmap)
        

        cap = cv2.VideoCapture('Wildlife.wmv')
        while(cap.isOpened()):
            #print("lagggg")
            ret, frame = cap.read()
            app.processEvents()
            #mimage = toQImage(frame, False).rgbSwapped()
            mimage = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_Grayscale8).rgbSwapped()
            pixmap = QPixmap.fromImage(mimage) # This line causes error (found out by running in console)
            self.webcam_display_label.setPixmap(pixmap)
            #cv2.imshow('image',img)
            
            #height, width, byteValue = frame.shape
            #byteValue = byteValue * width
    
            #reg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
            #cv2.imshow('frame',reg)
            #mimage = QImage(frame, width, height, byteValue, QImage.Format_RGB888)

            
            #image = QImage(frame, frame.width, frame.height, QImage.Format_RGB888).rgbSwapped()
            #pixmap = QPixmap.fromImage(mimage)
            #self.movie_screen.setPixmap(pixmap)
            
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            time.sleep(0.001)
            
            #cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        #cap.release()
        #cv2.destroyAllWindows()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
