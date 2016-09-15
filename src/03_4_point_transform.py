import cv2, imutils, numpy, time
from imutils import perspective

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
  (grabbed, frame) = camera.read()

  if not grabbed:
    break

  frame = imutils.resize(frame, width=500)

  clone = frame.copy()
  pts = numpy.array([(50, 50), (100, 50), (100, 100), (50, 100)])

  for (x, y) in pts:
      cv2.circle(clone, (x, y), 5, (0, 255, 0), -1)

  warped = perspective.four_point_transform(frame, pts)

  cv2.imshow("Original", clone)
  cv2.imshow("Warped", warped)

  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()