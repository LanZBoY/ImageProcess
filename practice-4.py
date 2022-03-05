import numpy


import numpy as np
import cv2

sourceImg = cv2.imread('./img/WXZEGID.jpg', -1)

grayImg = cv2.cvtColor(sourceImg, cv2.COLOR_BGR2GRAY)

gaussianImg = cv2.GaussianBlur(sourceImg, (5, 5), 0)

ret, thresholdImg = cv2.threshold(grayImg, 120, 180, cv2.THRESH_BINARY)

cv2.imshow("thresholdImg", thresholdImg)
cv2.imshow('gaussianNamin' ,gaussianImg)
cv2.imshow("sourceImg", sourceImg)
cv2.waitKey()