'''
Created on Nov 30, 2015

@author: rcbyron
'''
import cv2

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

from PyET import settings

def frame_to_pixmap(f):
    mimage = QImage(f, f.shape[1], f.shape[0], f.strides[0], QImage.Format_RGB888).rgbSwapped()
    return QPixmap.fromImage(mimage)

class FrameUpdater(QObject):
    eye_frame_ready = pyqtSignal(QPixmap, int)
    seeing_frame_ready = pyqtSignal(QPixmap, int)

    def process(self): # A slot takes no params
        print('Processing frames...')
        
        if (settings.inst.is_show_eye or settings.inst.is_cap_eye) and not settings.inst.eye_cam.is_open():
            settings.inst.eye_cam.open()

        if (settings.inst.is_show_seeing or settings.inst.is_cap_seeing) and not settings.inst.seeing_cam.is_open():
            settings.inst.seeing_cam.open()
        
        while True:
            if settings.inst.eye_cam:
                if settings.inst.is_show_eye:
                    ret, f = settings.inst.eye_cam.read()
                    if ret:
                        f = cv2.flip(f, 0)
                        settings.inst.eye_cam.record(f)
                        self.eye_frame_ready.emit(frame_to_pixmap(f), 1)
