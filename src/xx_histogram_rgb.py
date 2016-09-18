import cv2, imutils, time
import numpy

camera = cv2.VideoCapture(0)
time.sleep(0.25)

hist_channels = 64
hist_size = (300, 400, 3)
hist_plot = numpy.zeros(hist_size, dtype=numpy.uint8)

color_table = numpy.ones((hist_channels, 1, 3), dtype=numpy.uint8) *255
color_table[:,0,0] = numpy.linspace(0, 180, hist_channels)
color_table = cv2.cvtColor(color_table, cv2.COLOR_HSV2BGR)

while True:
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hist_plot[...] = 0
    for idx in (2, 1, 0):
        hist = cv2.calcHist([hsv_image[:,:,idx]], [0], None, [hist_channels], [0, 180] if idx==0 else [0, 256])
        hist = cv2.normalize(hist)
        for i in range(1, hist_channels):
            x1, y1 = ((hist_size[1] // hist_channels) * (i -1), hist_size[0] * (1 - hist[i-1]))
            x2, y2 = ((hist_size[1] // hist_channels) * i, hist_size[0] * (1 - hist[i]))
            color = (int(color_table[i, 0, 0]), int(color_table[i, 0, 1]), int(color_table[i, 0, 2])) if idx == 0 else (200, 200, 200)
            cv2.line(hist_plot, (x1, y1), (x2, y2), color)

    cv2.imshow("Labdo - Image", frame)
    cv2.imshow("Labdo - Histogram", hist_plot)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()