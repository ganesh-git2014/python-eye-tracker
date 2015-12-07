'''
Created on Nov 30, 2015

@author: rcbyron
'''
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
import cv2

CASCADE_PATH = "haarcascades/haarcascade_eye.xml"

def frame_to_pixmap(f):
    mimage = QImage(f, f.shape[1], f.shape[0], f.strides[0], QImage.Format_RGB888).rgbSwapped()
    return QPixmap.fromImage(mimage)

class FrameUpdater(QObject):
    frame_ready = pyqtSignal(QPixmap, int)
    
    def __init__(self):
        super().__init__()
        self.eye_cam = None
        self.seeing_cam = None
        self.cap_eye = False
        self.cap_seeing = False



    def process(self): # A slot takes no params
        while(self.cap_eye or self.cap_seeing):
            if self.cap_eye:
                ret, f = self.eye_cam.read()
                if ret:
                    self.eye_frame_ready.emit(frame_to_pixmap(f), 1)
            
            if self.cap_seeing:
                ret, f = self.seeing_cam.read()
                if ret:
                    self.seeing_frame_ready.emit(frame_to_pixmap(f), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
