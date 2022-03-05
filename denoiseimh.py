import numpy as np
import cv2

sourceImg = cv2.imread('./img/paper.png', -1)
denosieImg = cv2.medianBlur(sourceImg, 5)

cv2.imshow("Temp", denosieImg)
cv2.waitKey()