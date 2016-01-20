'''
Created on Dec 7, 2015

@author: rcbyron
'''
from PyQt5 import QtCore
from PyQt5.QtCore import QThread


from ui.main_window import Ui_MainWindow as MainUi
from classes.frame_updater import FrameUpdater
import PyET

class TrackerGui(MainUi):
 
    def update_cam_list(self):
        cam_list = [cam.__str__() for cam in PyET.inst.cameras.values()]
        self.eye_cam_combo_box.clear()
        self.seeing_cam_combo_box.clear()
        self.eye_cam_combo_box.addItems(cam_list)
        self.seeing_cam_combo_box.addItems(cam_list)
        
    def update_res_list(self):
        self.eye_res_combo_box.clear()
        self.seeing_res_combo_box.clear()
        if PyET.inst.eye_cam:
            r_list = [str(res[0]) + ' x ' + str(res[1]) for res in PyET.inst.eye_cam.get_available_resolutions()]
            self.eye_res_combo_box.addItems(r_list)
        if PyET.inst.seeing_cam:
            r_list = [str(res[0]) + ' x ' + str(res[1]) for res in PyET.inst.seeing_cam.get_available_resolutions()]
            self.seeing_res_combo_box.addItems(r_list)
    
    def show_eye(self):
        print('Showing eye!')
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
        
        self.start_cap_btn.released.connect(lambda: print('recording!'))
        self.stop_cap_btn.released.connect(lambda: print('stopped recording!'))
        self.eye_cam_btn.pressed.connect(PyET.inst.show_eye)
        self.seeing_cam_btn.pressed.connect(PyET.inst.show_seeing)

    def on_frame_ready(self, pixmap, cam_type):
        if cam_type is 1:
            self.cam_view.setPixmap(pixmap)
        elif cam_type is 2:
            self.cam_view.setPixmap(pixmap)
        app = QtCore.QCoreApplication.instance()
        app.processEvents()