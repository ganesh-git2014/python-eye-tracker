'''
Created on Jan 27, 2016

@author: rcbyron
'''
import cv2

from PyET.classes.enhanced_cam import EnhancedCam

inst = None

def init():
    global inst
    inst = PyETCore()
    
def find_cameras():
    cameras = {}
    for i in range(10):
        temp_cam = cv2.VideoCapture(i)
        if temp_cam.isOpened():
            print('Found camera '+str(i)+'...')
            cameras[i] = EnhancedCam(i, temp_cam)
            print('Registered', cameras[i])
            cameras[i].release()
    return cameras

class PyETCore():
    def __init__(self):
        self.cameras = {}
        self.eye_cam = None
        self.seeing_cam = None
        self.is_show_eye = False
        self.is_show_seeing = False
        
        self.cameras = find_cameras()
        
        if len(self.cameras.items()) >= 2:
            self.eye_cam = self.cameras[0]
            self.seeing_cam = self.cameras[1]
            self.show_eye()
            self.show_seeing()
        elif len(self.cameras.items()) == 1:
            self.eye_cam = self.cameras[0]
            self.show_eye()
            
    def record_eye(self):
        if self.eye_cam:
            print('Recording eye camera...')
            self.eye_cam.start_recording()
        else:
            print('Eye cam not found!')
    
    def stop_record_eye(self):
        print('Recording stopped!')
        self.eye_cam.stop_recording()
    
    def show_eye(self):
        if self.eye_cam:
            print('Showing eye camera...')
            self.is_show_eye = True
        else:
            print('Eye cam not found!')
    
    def show_seeing(self):
        if self.seeing_cam:
            print('Showing seeing camera...')
            self.is_show_seeing = True
        else:
            print('Seeing cam not found!')
            
    def close_eye(self):
        self.is_show_eye = False
        if self.eye_cam:
            self.eye_cam.release()
    
    def close_seeing(self):
        self.is_show_seeing = False
        if self.seeing_cam:
            self.seeing_cam.release()