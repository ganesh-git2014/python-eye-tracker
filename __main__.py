import sys, cv2

from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap

from ui.main_window import Ui_MainWindow as MainUi
from ui.secondary_window import Ui_SecondaryWindow as SecondUi
from ui.editor_dialog import Ui_EditorDialog as EditorUi

from classes.enhanced_cam import EnhancedCam

CASCADE_PATH = "haarcascades/haarcascade_eye.xml"

RESOLUTIONS = {(480, 360),
               (640, 480),
               (720, 480),
               (800, 600),
               (1280, 720),
               (1920, 1080)}

def get_cameras():
    cameras = {}
    for i in range(10):
        temp_cam = cv2.VideoCapture(i)
        if temp_cam.isOpened():
            cameras[i] = EnhancedCam(i, temp_cam)
            
            print("Found camera", i, " with properties: ")
            cameras[i].list()
            
            temp_cam.release()
    return cameras

def show_movie():
    print("SHOWING MOVIE!")
    cap = cv2.VideoCapture(1)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            print("fail")
        app.processEvents()
        mimage = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(mimage) # This line causes error (found out by running in console)
        ui.cam_view.setPixmap(pixmap)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MainUi()
ui.setupUi(MainWindow)
ui.start_cap_btn.released.connect(show_movie)
MainWindow.show()
sys.exit(app.exec_())

cameras = get_cameras()

if len(cameras.items()) >= 2:
    seeing_camera = cameras[0]
    eye_camera = cameras[1]
elif len(cameras.items()) == 1:
    seeing_camera = cameras[0]
