import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# count of intersections of black and white squares in chess board
nx = 9
ny = 6

# file for calibration camera
fname = "/home/afomin/projects/mj/camera_calibration/images/calibration_test.jpg"
img = cv2.imread(fname)
# print("img: %s" % (img, ))
# convert to gray scale:
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
while(1):
    k = cv2.waitKey(1)
    if k == ord('a'):    # Esc key to stop
        break
cv2.destroyAllWindows()

# find chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

# print("corners: %s" % (corners,))
# print("ret: %s" % (ret,))

if ret is True:
    # draw and display corners
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    cv2.imshow("img", img)
        while(1):
            k = cv2.waitKey(1)
            if k == ord('a'):    # Esc key to stop
                break
        cv2.destroyAllWindows()
