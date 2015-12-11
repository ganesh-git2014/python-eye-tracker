'''
Created on Dec 7, 2015

@author: rcbyron
'''
from PyQt5 import QtCore
from PyQt5.QtCore import QThread


from ui.main_window import Ui_MainWindow as MainUi
from classes.frame_updater import FrameUpdater
import settings

class TrackerGui(MainUi):
 
    def update_cam_list(self):
        cam_list = [cam.__str__() for cam in settings.cameras.values()]
        self.eye_cam_combo_box.clear()
        self.seeing_cam_combo_box.clear()
        self.eye_cam_combo_box.addItems(cam_list)
        self.seeing_cam_combo_box.addItems(cam_list)
        
    def update_res_list(self):
        self.eye_res_combo_box.clear()
        self.seeing_res_combo_box.clear()
        if settings.eye_cam:
            self.eye_res_combo_box.addItems(settings.eye_cam.str_resolutions)
        if settings.seeing_cam:
            self.seeing_res_combo_box.addItems(settings.seeing_cam.str_resolutions)
    
    def show_eye(self):
        print("Showing eye!")
        app = QtCore.QCoreApplication.instance()
        app.processEvents()
    
    def setup_ui(self, MainWindow):
        super().setupUi(MainWindow)
        self.f_updater = FrameUpdater()
        self.thread = QThread()
        self.f_updater.eye_frame_ready.connect(self.on_frame_ready)
        self.f_updater.seeing_frame_ready.connect(self.on_frame_ready)
        self.f_updater.moveToThread(self.thread)
        self.thread.started.connect(self.f_updater.process)
        self.thread.start()
        
        self.update_cam_list()
        self.update_res_list()
        
        self.start_cap_btn.released.connect(lambda: print("recording!"))
        self.stop_cap_btn.released.connect(lambda: print("stopped recording!"))
        self.eye_cam_btn.pressed.connect(settings.show_eye)
        self.seeing_cam_btn.pressed.connect(settings.show_seeing)

    def on_frame_ready(self, pixmap, cam_type):
        if cam_type is 1:
            self.cam_view.setPixmap(pixmap)
        elif cam_type is 2:
            self.cam_view.setPixmap(pixmap)
        app = QtCore.QCoreApplication.instance()
        app.processEvents()