import cv2
from utils import houghCircle

img = cv2.imread('./hw_3/sample.jpg')
result = houghCircle(img = img, dp= 0.5, low_threshold = 50)
cv2.imshow("result", result)
cv2.waitKey()