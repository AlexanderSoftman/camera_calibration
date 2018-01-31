import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

# count of intersections of black and white squares in chess board
nx = 8
ny = 6

# file for calibration camera
obj_points = []
img_points = []

# need points in format (0, 0, 0) - original point,
# or (4, 2, 0). Z coordinate always zero
objp = np.zeros((ny * nx, 3), np.float32)
# print("objp: %s" % (objp,))
# x,y coordinates
objp[:, :2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)
# print("objp[:, :2]: %s" % (objp[:, :2],))

calib_images = glob.glob(
    "/home/afomin/projects/mj/camera_calibration/images/GOPR*.jpg")
test_image = "/home/afomin/projects/mj/camera_calibration/images/GOPR0032.jpg"

# create calibration
for fname in calib_images:
    img = cv2.imread(fname)
    # convert to gray scale:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    if ret is True:
        # draw and display corners
        img_points.append(corners)
        obj_points.append(objp)

test_img = cv2.imread(test_image)
# apply calibration
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
# cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
    obj_points,
    img_points,
    gray.shape[::-1],
    None,
    None)

cv2.imshow("initial image", test_img)
while(1):
    k = cv2.waitKey(0)
    if k == ord('a'):    # Esc key to stop
        break
    cv2.destroyAllWindows()

dst = cv2.undistort(
    test_img,
    mtx,
    dist,
    None,
    mtx)
cv2.imshow("undistorsed image", dst)
while(1):
    k = cv2.waitKey(0)
    if k == ord('a'):    # Esc key to stop
        break
    cv2.destroyAllWindows()
