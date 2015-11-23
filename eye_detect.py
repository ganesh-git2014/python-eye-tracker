import cv2
import sys

cv2.CAP_PROP_FRAME_WIDTH

FRAME_TITLE = "Python Eye Tracker 6000"
CASCADE_PATH = "haarcascades/haarcascade_eye.xml"

obj_cascade = cv2.CascadeClassifier(CASCADE_PATH)

resolutions = {(480, 360),
               (640, 480),
               (720, 480),
               (800, 600),
               (1280, 720),
               (1920, 1080)}
cameras = {}

def get_cameras():
    for i in range(10):
        temp_camera = cv2.VideoCapture(i)
        if temp_camera.isOpened():
            res = temp_camera.get(cv2.CAP_PROP_FRAME_WIDTH), temp_camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            resolutions.add(res)
            print(res, temp_camera.get(cv2.CAP_PROP_FPS))
            print(temp_camera)
            cameras[i] = temp_camera
        #temp_camera.release()
get_cameras()
print(cameras)
print(resolutions)

video_capture = cameras[0]
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        print("Frame could not be read :(")
        continue
    
    frame = cv2.flip(frame,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    detected_objs = obj_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(200, 200),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
   
    # Draw a rectangle around the faces
    for (x, y, w, h) in detected_objs:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
   
    # Display the resulting frame
    my_window = cv2.imshow(FRAME_TITLE, frame)
       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
