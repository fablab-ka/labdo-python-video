import cv2, imutils, time
import numpy as np

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
  (grabbed, frame) = camera.read()

  if not grabbed:
    break

  frame = imutils.resize(frame, width=400)
  h, w, _ = frame.shape

  blank_image = np.zeros((h*2, w*2, 3), np.uint8)

  blank_image[0:h, 0:w, 0] = frame[:,:, 0]
  blank_image[0:h, 0:w, 1] = frame[:,:, 1]
  blank_image[0:h, 0:w, 2] = frame[:,:, 2]

  blank_image[h: , 0:w, 1] = frame[:,:, 1]
  blank_image[0:h, w: , 2] = frame[:,:, 2]

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  blank_image[h:, w:, 0] = gray[:,:]
  blank_image[h:, w:, 1] = gray[:,:]
  blank_image[h:, w:, 2] = gray[:,:]

  cv2.imshow("Labdo - Video 2", blank_image)

  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()