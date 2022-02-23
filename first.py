# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
img = np.zeros([500,500, 3], dtype = 'uint8')
"""
因為 np只開了兩維陣列，而RGB三個通道則是第三維的元素
(B, G, R)
所以無法調色
"""
cv2.rectangle(img, (100, 100), (400, 400), (255, 0, 0) , -1)
cv2.rectangle(img, (250, 250), (400, 100), (255, 255, 255) , -1)
cv2.rectangle(img, (325, 325), (400, 400), (0, 255 , 0), -1)
cv2.line(img, (325, 325), (375, 400), (255, 24, 225), thickness = 2)


(h, w, c) = img.shape

# for x in range(h):
#     for y in range(w):
#         img[x][y][0], img[x][y][1] = img[x][y][1], img[x][y][0]

cv2.imshow('temp',img)
cv2.waitKey()