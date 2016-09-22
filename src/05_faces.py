import cv2, imutils, time

faceCascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
    grabbed, frame = camera.read()

    if not grabbed:
      break

    frame = imutils.resize(frame, width=800)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Labdo - Video 4", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()