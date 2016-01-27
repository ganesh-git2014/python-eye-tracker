'''
Created on Nov 30, 2015

@author: rcbyron
'''
import cv2

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

from PyET import PyETCore

def frame_to_pixmap(f):
    mimage = QImage(f, f.shape[1], f.shape[0], f.strides[0], QImage.Format_RGB888).rgbSwapped()
    return QPixmap.fromImage(mimage)

class FrameUpdater(QObject):
    eye_frame_ready = pyqtSignal(QPixmap, int)
    seeing_frame_ready = pyqtSignal(QPixmap, int)

    def process(self): # A slot takes no params
        print('Processing frames...')
        
        if (PyETCore.inst.is_show_eye or PyETCore.inst.is_cap_eye) and not PyETCore.inst.eye_cam.is_open():
            PyETCore.inst.eye_cam.open()

        if (PyETCore.inst.is_show_seeing or PyETCore.inst.is_cap_seeing) and not PyETCore.inst.seeing_cam.is_open():
            PyETCore.inst.seeing_cam.open()
        
        while True:
            if PyETCore.inst.eye_cam:
                if PyETCore.inst.is_show_eye:
                    ret, f = PyETCore.inst.eye_cam.read()
                    if ret:
                        f = cv2.flip(f, 0)
                        if PyETCore.inst.eye_cam.recording:
                            PyETCore.inst.eye_cam.record(f)
                        self.eye_frame_ready.emit(frame_to_pixmap(f), 1)
            if PyETCore.inst.seeing_cam:
                if PyETCore.inst.is_show_seeing:
                    ret, f = PyETCore.inst.seeing_cam.read()
                    if ret:
                        if PyETCore.inst.seeing_cam.recording:
                            PyETCore.inst.seeing_cam.record(f)
                        self.eye_frame_ready.emit(frame_to_pixmap(f), 2)