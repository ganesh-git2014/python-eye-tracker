'''
Created on Feb 1, 2016

@author: rcbyron
'''
import logging, os, cv2

from PyET import settings

class Recorder():
    def __init__(self, res):
        print('wow')
        self.id = 0
        self.vid_file = lambda: 'output-'+str(self.id)+'.avi'
        self.log_file = lambda: 'output-'+str(self.id)+'.csv'
        while os.path.isfile(self.vid_file()) or os.path.isfile(self.log_file()):
            self.id += 1
        print('got new id')
        print(self.vid_file())
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.vw = cv2.VideoWriter(self.vid_file(), fourcc, settings.DEFAULT_RECORDING_FPS, res)
        print('cool make the logger now')
        self.log = logging.getLogger(self.log_file())
        self.log.setLevel(logging.INFO)
        fh = logging.FileHandler(self.log_file())
        fh.setLevel(logging.INFO)
        self.log.addHandler(fh)
    
        self.wrap_vw()
    
    def wrap_vw(self):
        self.is_open = lambda: self.writer.isOpened()
        self.open = lambda: self.writer.open(self.id)
        self.write = lambda: self.writer.write()
        self.release = lambda: self.writer.release()