import numpy as np
import cv2

sourceImg = cv2.imread('./img/WXZEGID.jpg', -1)
# Mean Filter 做影像的霧化處裡
meanFilterImg = cv2.blur(sourceImg, (3,3))
medianFilterImg = cv2.medianBlur(sourceImg, 5)
cv2.imshow("MeanFilterNamin", meanFilterImg)
cv2.imshow("MedianFilterImg", medianFilterImg)
cv2.waitKey()