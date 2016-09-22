import cv2, imutils, time, numpy

camera = cv2.VideoCapture(0)
time.sleep(0.25)

min_area = 500

referenceFrame = None

while True:
  (grabbed, frame) = camera.read()

  if not grabbed:
    break

  frame = imutils.resize(frame, width=500)

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (21, 21), 0)

  if referenceFrame is None:
    avg1 = numpy.float32(gray)

  cv2.accumulateWeighted(gray, avg1, 0.02)
  referenceFrame = cv2.convertScaleAbs(avg1)

  frameDelta = cv2.absdiff(referenceFrame, gray)
  thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

  thresh = cv2.dilate(thresh, None, iterations=2)
  (contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # for c in contours:
  #   if cv2.contourArea(c) < min_area:
  #     continue

  #   (x, y, w, h) = cv2.boundingRect(c)

  #   cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

  boundingBoxes = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) < min_area]
  boundingBoxes = [(x, y, x + w, y + h) for (x, y, w, h) in boundingBoxes]
  if len(boundingBoxes) > 0:
      (mx1, my1, mx2, my2) = zip(*boundingBoxes)
      cv2.rectangle(frame, (numpy.min(mx1), numpy.min(my1)), (numpy.max(mx2), numpy.max(my2)), (0, 255, 0), 2)

  cv2.imshow("Labdo - Video 3", frame)
  cv2.imshow("Labdo - Video 3 - reference", referenceFrame)
  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()