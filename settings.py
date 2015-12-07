'''
Created on Dec 7, 2015

@author: rcbyron
'''
import os, cv2
from classes.enhanced_cam import EnhancedCam

recording_dir = "recordings"

cameras = {}
eye_cam = None
seeing_cam = None
cap_eye = False
cap_Seeing = False

def init():
    ensure_dir(recording_dir)
    
    find_cameras()
    
    if len(cameras.items()) >= 2:
        eye_cam = cameras[0]
        seeing_cam = cameras[1]
    elif len(cameras.items()) == 1:
        eye_cam = cameras[0]

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def find_cameras():
    global cameras
    cameras = {}
    for i in range(10):
        temp_cam = cv2.VideoCapture(i)
        if temp_cam.isOpened():
            cameras[i] = EnhancedCam(i, temp_cam)
            print("Found", cameras[i])
            temp_cam.release()

def show_eye():
    global cap_eye
    if eye_cam:
        cap_eye = eye_cam.open()

def show_seeing():
    global cap_seeing
    if seeing_cam:
        cap_seeing = seeing_cam.open()
        
def close_eye():
    global cap_eye
    cap_eye = False
    if eye_cam:
        eye_cam.release()

def close_seeing():
    global cap_seeing
    cap_seeing = False
    if seeing_cam:
        seeing_cam.release()
        
def toggle_eye():
    if eye_cam and eye_cam.isOpen():
        show_