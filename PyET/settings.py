'''
Created on Dec 7, 2015

@author: rcbyron
'''
import os, cv2

from classes.enhanced_cam import EnhancedCam

def ensure_dir(f):
    d = os.path.join(os.getcwd(), os.path.dirname(f))
    if not os.path.exists(d):
        os.mkdir(d)

DEFAULT_RECORDING_FPS = 20.0
CLIENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CLIENT_DIR)
HAARCASCADES_DIR = os.path.join(CLIENT_DIR, 'haarcascades')
RECORDINGS_DIR = os.path.join(CLIENT_DIR, 'recordings')
LOGS_DIR = os.path.join(CLIENT_DIR, 'logs')
CASCADE_FILE = os.path.join(HAARCASCADES_DIR, 'haarcascade_eye.xml')

DIRS = [HAARCASCADES_DIR, LOGS_DIR, RECORDINGS_DIR]
for folder in DIRS:
    ensure_dir(folder)

inst = None

def init():
    global inst
    inst = PyETCore()

class PyETCore():
    def __init__(self):
        self.cameras = {}
        self.eye_cam = None
        self.seeing_cam = None
        self.is_show_eye = False
        self.is_show_seeing = False
        self.is_cap_eye = False
        self.is_cap_seeing = False
        
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
                self.cameras[i].release()
    
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
        self.is_cap_eye = False
        self.is_show_eye = False
        if self.eye_cam:
            self.eye_cam.release()
    
    def close_seeing(self):
        self.is_cap_seeing = False
        self.is_show_seeing = False
        if self.seeing_cam:
            self.seeing_cam.release()
    