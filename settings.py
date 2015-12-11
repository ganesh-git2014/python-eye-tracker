'''
Created on Dec 7, 2015

@author: rcbyron
'''
import os, cv2
from classes.enhanced_cam import EnhancedCam

RECORDING_DIR = "recordings"

def ensure_dir(f):
    d = os.path.join(os.getcwd(), os.path.dirname(f))
    if not os.path.exists(d):
        os.mkdir(d)

inst = None

class Settings():
    def __init__(self):
        self.cameras = {}
        self.eye_cam = None
        self.seeing_cam = None
        self.is_show_eye = False
        self.is_show_seeing = False
        self.is_cap_eye = False
        self.is_cap_seeing = False
        
        ensure_dir(RECORDING_DIR)
        
        self.find_cameras()
        
        if len(self.cameras.items()) >= 2:
            self.eye_cam = self.cameras[0]
            self.seeing_cam = self.cameras[1]
        elif len(self.cameras.items()) == 1:
            self.eye_cam = self.cameras[0]
    
    def find_cameras(self):
        self.cameras = {}
        for i in range(10):
            temp_cam = cv2.VideoCapture(i)
            if temp_cam.isOpened():
                self.cameras[i] = EnhancedCam(i, temp_cam)
                print("Found", self.cameras[i])
                temp_cam.release()
    
    def show_eye(self):
        if self.eye_cam:
            self.is_show_eye = self.eye_cam.open()
    
    def show_seeing(self):
        if self.seeing_cam:
            self.is_show_seeing = self.seeing_cam.open()
            
    def close_eye(self):
        self.is_cap_eye = False
        self.is_show_eye = False
        if self.eye_cam:
            self.eye_cam.release()
    
    def close_seeing(self):
        self.is_cap_seeing = False
        self.is_show_seeing = False
        if self.seeing_cam:
            self.seeing_cam.release()
    