import argparse
import datetime
import imutils
import time
import cv2
import numpy as np

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
  (grabbed, frame) = camera.read()

  if not grabbed:
    break

  frame = imutils.resize(frame, width=400)

  blank_image = np.zeros((225*2, 400*2, 3), np.uint8)

  blank_image[0:225, 0:400, 0] = frame[:,:, 0]
  blank_image[225:, 0:400, 1] = frame[:,:, 1]
  blank_image[0:225, 400:, 2] = frame[:,:, 2]

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  blank_image[225:, 400:, 0] = gray[:,:]
  blank_image[225:, 400:, 1] = gray[:,:]
  blank_image[225:, 400:, 2] = gray[:,:]

  cv2.imshow("Labdo - Video 2", blank_image)

  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()