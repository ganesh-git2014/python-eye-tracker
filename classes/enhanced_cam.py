'''
Created on Nov 30, 2015

@author: rcbyron
'''
import cv2

RESOLUTIONS = {(480, 360),
               (640, 480),
               (720, 480),
               (800, 600),
               (1280, 720),
               (1920, 1080)}

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
        
        RESOLUTIONS.add(self.res())
        self.resolutions = self.get_available_resolutions()
        self.str_resolutions = [str(res[0])+" x "+str(res[1]) for res in self.resolutions]
        
    def set_resolution(self, res):
        orig_res = self.res()
        
        flag_1 = self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, res[0])
        flag_2 = self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, res[1])
        
        if flag_1 and flag_2:
            print("Successfully updated resolution:", res)
            return True
        else:
            print("Setting resolution failed. Reverting to original resolution.")
            self.try_resolution(orig_res)
            return False
    
    def get_available_resolutions(self):
        orig_res = self.res()
        available_res_set = {res for res in RESOLUTIONS if self.set_resolution(res)}
        available_res_set.add(orig_res)
        self.set_resolution(orig_res)
        return available_res_set

    def list(self):
        print("- Resolution:", self.res())
        print("- FPS:", self.fps())
        
    def __str__(self):
        return "Device " + str(self.id)