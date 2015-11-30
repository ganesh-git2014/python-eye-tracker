'''
Created on Nov 30, 2015

@author: rcbyron
'''
import cv2

class EnhancedCam():
    def __init__(self, cam_id, cam):
        self.id = cam_id
        self.cam = cam
        
        self.res =              lambda: (self.cam.get(cv2.CAP_PROP_FRAME_WIDTH),
                                         self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.aperture =         lambda: self.cam.get(cv2.CAP_PROP_APERTURE)
        self.auto_exposure =    lambda: self.cam.get(cv2.CAP_PROP_AUTO_EXPOSURE)
        self.backlight =        lambda: self.cam.get(cv2.CAP_PROP_BACKLIGHT)
        self.brightness =       lambda: self.cam.get(cv2.CAP_PROP_BRIGHTNESS)
        self.contrast =         lambda: self.cam.get(cv2.CAP_PROP_CONTRAST)
        self.exposure =         lambda: self.cam.get(cv2.CAP_PROP_EXPOSURE)
        self.focus =            lambda: self.cam.get(cv2.CAP_PROP_FOCUS)
        self.format =           lambda: self.cam.get(cv2.CAP_PROP_FORMAT)
        self.fps =              lambda: self.cam.get(cv2.CAP_PROP_FPS)
        self.frame_count =      lambda: self.cam.get(cv2.CAP_PROP_FRAME_COUNT)
        self.gain =             lambda: self.cam.get(cv2.CAP_PROP_GAIN)
        self.gamma =            lambda: self.cam.get(cv2.CAP_PROP_GAMMA)
        self.hue =              lambda: self.cam.get(cv2.CAP_PROP_HUE)
        self.saturation =       lambda: self.cam.get(cv2.CAP_PROP_SATURATION)
        self.sharpness =        lambda: self.cam.get(cv2.CAP_PROP_SHARPNESS)
        self.speed =            lambda: self.cam.get(cv2.CAP_PROP_SPEED)
        self.w_balance_u =      lambda: self.cam.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U)
        self.w_balance_v =      lambda: self.cam.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V)
        self.zoom =             lambda: self.cam.get(cv2.CAP_PROP_ZOOM)

    def list(self):
        print("- Resolution:", self.res())
        print("- FPS:", self.fps())
        
    def __str__(self):
        return "Device " + str(id)