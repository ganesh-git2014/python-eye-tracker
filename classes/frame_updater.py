'''
Created on Nov 30, 2015

@author: rcbyron
'''
import cv2

import PyET

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

def frame_to_pixmap(f):
    mimage = QImage(f, f.shape[1], f.shape[0], f.strides[0], QImage.Format_RGB888).rgbSwapped()
    return QPixmap.fromImage(mimage)

class FrameUpdater(QObject):
    eye_frame_ready = pyqtSignal(QPixmap, int)
    seeing_frame_ready = pyqtSignal(QPixmap, int)

    def process(self): # A slot takes no params
        print("YOOO")
        while True:#(PyET.inst.is_show_eye or PyET.inst.is_show_seeing):
            print('MADE IT TO FRAME UPDATER', PyET.inst.is_show_eye)
            
            if PyET.inst.is_show_eye:
                #PyET.inst.eye_cam.cam.imshow()
                #if not PyET.inst.eye_cam.cam.isOpened():
                #    PyET.inst.eye_cam.cam.open()
                ret, f = PyET.inst.eye_cam.cam.read()
                if ret:
                    self.eye_frame_ready.emit(frame_to_pixmap(f), 1)
            
            if PyET.inst.is_show_seeing:
                ret, f = PyET.inst.seeing_cam.cam.read()
                if ret:
                    self.seeing_frame_ready.emit(frame_to_pixmap(f), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
