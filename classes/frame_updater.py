'''
Created on Nov 30, 2015

@author: rcbyron
'''
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
import cv2

import PyET

CASCADE_PATH = "haarcascades/haarcascade_eye.xml"

def frame_to_pixmap(f):
    mimage = QImage(f, f.shape[1], f.shape[0], f.strides[0], QImage.Format_RGB888).rgbSwapped()
    return QPixmap.fromImage(mimage)

class FrameUpdater(QObject):
    eye_frame_ready = pyqtSignal(QPixmap, int)
    seeing_frame_ready = pyqtSignal(QPixmap, int)

    def process(self): # A slot takes no params
        while(PyET.inst.is_show_eye or PyET.inst.is_show_seeing):
            if PyET.inst.is_show_eye:
                ret, f = PyET.inst.eye_cam.read()
                if ret:
                    self.eye_frame_ready.emit(frame_to_pixmap(f), 1)
            
            if PyET.inst.is_show_seeing:
                ret, f = PyET.inst.seeing_cam.read()
                if ret:
                    self.seeing_frame_ready.emit(frame_to_pixmap(f), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
