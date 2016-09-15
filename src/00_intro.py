import cv2, imutils, time

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
  (grabbed, frame) = camera.read()

  if not grabbed:
    break

  frame = imutils.resize(frame, width=400)

  cv2.imshow("Labdo - Video 1", frame)

  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()