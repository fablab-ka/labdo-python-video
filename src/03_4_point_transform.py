import cv2, imutils, numpy, time
from imutils import perspective

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
  (grabbed, frame) = camera.read()

  if not grabbed:
    break

  frame = imutils.resize(frame, width=800)

  pts = numpy.array([(100, 80), (300, 50), (300, 200), (50, 180)])

  warped = perspective.four_point_transform(frame, pts)

  for (x, y) in pts:
    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

  cv2.imshow("Original", frame)
  cv2.imshow("Warped", warped)

  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()