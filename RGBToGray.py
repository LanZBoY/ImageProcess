import cv2
import numpy as np

srcimg = cv2.imread("./img/WXZEGID.jpg")
(h, w, c) = srcimg.shape
grayimg = np.zeros((h, w), dtype='uint8')

for y in range(h):
    for x in range(w):
        # [高][寬]
        grayimg[y][x] = int(0.1 * srcimg[y][x][0] + 0.6 * srcimg[y][x][1] + 0.3 * srcimg[y][x][2])

cv2.imshow("Result", grayimg)
cv2.waitKey()