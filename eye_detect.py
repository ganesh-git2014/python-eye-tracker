import cv2

FRAME_TITLE = "Python Eye Tracker 6000"
CASCADE_PATH = "haarcascades/haarcascade_righteye_2splits.xml"
CAMERA_DEVICE = 0

obj_cascade = cv2.CascadeClassifier(CASCADE_PATH)
video_capture = cv2.VideoCapture(CAMERA_DEVICE)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        print("Error loading camera:", CAMERA_DEVICE)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_objs = obj_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(30, 30),
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
