'''
Created on Nov 10, 2015

@author: rcbyron
'''

import sys, cv2, time
from PyQt5.QtWidgets import (QWidget, QToolTip, QMessageBox, QPushButton, QApplication, QLabel, QGridLayout)
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtCore import QCoreApplication

GUI_TITLE = "Python Eye Tracker 6000 GUI"

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Show Movie', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(self.show_movie)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.movie_screen = QLabel("Movie:")
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.movie_screen, 0, 0)
        mainLayout.addWidget(btn, 0, 1)

        self.setLayout(mainLayout)
        
        self.setGeometry(1920, 1080, 1920, 1080)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('data/tacc-icon.png'))
        
        self.show()
        self.center()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
            
    def show_movie(self):
        print("SHOWING MOVIE!")
        frame = cv2.imread('Koala.jpg',0)
        
        height, width = frame.shape
        #byteValue = byteValue * width
    
        #reg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        #cv2.imshow('frame',reg)
        mimage = QImage(frame, width, height, QImage.Format_RGB888)
    
        
        #image = QImage(frame, frame.width, frame.height, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(mimage) # This line causes error (found out by running in console)
        self.movie_screen.setPixmap(pixmap)
        

        #cap = cv2.VideoCapture('Wildlife.wmv')
        #while(cap.isOpened()):
            
            #cv2.imshow('image',img)
            
            #ret, frame = cap.read()
            
            #height, width, byteValue = frame.shape
            #byteValue = byteValue * width
    
            #reg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
            #cv2.imshow('frame',reg)
            #mimage = QImage(frame, width, height, byteValue, QImage.Format_RGB888)

            
            #image = QImage(frame, frame.width, frame.height, QImage.Format_RGB888).rgbSwapped()
            #pixmap = QPixmap.fromImage(mimage)
            #self.movie_screen.setPixmap(pixmap)
            
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #time.sleep(0.001)
            
            #cv2.waitKey(1)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
        
        #cap.release()
        #cv2.destroyAllWindows()
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
