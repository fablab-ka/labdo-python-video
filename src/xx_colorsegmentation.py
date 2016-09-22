import cv2, imutils, time
import numpy

###  http://docs.opencv.org/trunk/df/d9d/tutorial_py_colorspaces.html

camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    frame = imutils.resize(frame, width=400)

    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = numpy.array([90,50,50])
    upper_blue = numpy.array([120,255,255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    
    # Bitwise-AND mask and original image
    cutout = cv2.bitwise_and(frame,frame, mask= mask)
   
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('cutout',cutout)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()