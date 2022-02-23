# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('./img/WXZEGID.jpg', -1)

for w in range(img.shape[0]):
    for h in range(img.shape[1]):
        img[w][h][0] = 0
        img[w][h][1] = 0
        img[w][h][2] = 0

cv2.imshow("Namin", img)
cv2.waitKey()