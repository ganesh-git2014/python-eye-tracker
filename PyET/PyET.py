'''
Created on Dec 7, 2015

@author: rcbyron
'''
import os, cv2

from classes.enhanced_cam import EnhancedCam

RECORDING_DIR = 'recordings'
CASCADE_PATH = 'haarcascades/haarcascade_eye.xml'

inst = None

def init():
    global inst
    inst = PyETCore()

def ensure_dir(f):
    d = os.path.join(os.getcwd(), os.path.dirname(f))
    if not os.path.exists(d):
        os.mkdir(d)

class PyETCore():
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
                print('Found camera '+str(i)+'...')
                self.cameras[i] = EnhancedCam(i, temp_cam)
                print('Registered', self.cameras[i])
                self.cameras[i].cam.release()
    
    def show_eye(self):
        if self.eye_cam:
            print("showing eye bruh...")
            #print(dir(self.eye_cam.cam))
            #self.eye_cam.cam.imshow()
            self.is_show_eye = True#self.eye_cam.cam.open()
            print("k yo")
    
    def show_seeing(self):
        if self.seeing_cam:
            self.is_show_seeing = self.seeing_cam.cam.open()
            
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
    