import cv2
import numpy as np

img = cv2.imread('./img/Pic/doraemon.jpg', -1)

cv2.imshow("doraemon", img)
# cv2.waitKey()

cv2.imwrite('./output/outputTest.bmp', img)
cv2.imwrite('./output/outputTest.jpg', img)
cv2.destroyAllWindows()