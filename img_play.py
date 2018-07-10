import numpy
import cv2

img = cv2.imread("./ball.jpg")

# point1 = 200, 370

# point2 = 270, 460

ball = img[370:460, 200:270]
img[270:360, 100:170] = ball

cv2.imwrite("ball_modified.jpg", img)

