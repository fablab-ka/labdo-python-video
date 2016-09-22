import cv2, imutils, time
import numpy

camera = cv2.VideoCapture(0)
time.sleep(0.25)

hist_channels = 64
hist_size = (300, 400, 3)
hist_plot = numpy.zeros(hist_size, dtype=numpy.uint8)

while True:
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    frame = imutils.resize(frame, width=800)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist([gray], [0], None, [hist_channels], [0, 256])
    hist = cv2.normalize(hist)

    hist_plot[...] = 0
    for i in range(1, hist_channels):
        x1, y1 = ((hist_size[1] // hist_channels) * (i -1), hist_size[0] * (1 - hist[i-1]))
        x2, y2 = ((hist_size[1] // hist_channels) * i, hist_size[0] * (1 - hist[i]))
        cv2.line(hist_plot, (x1, y1), (x2, y2), (0,255,0))

    cv2.imshow("Labdo - Image", gray)
    cv2.imshow("Labdo - Histogram", hist_plot)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()