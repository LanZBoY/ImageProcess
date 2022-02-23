# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:58:27 2022

@author: user
"""

import cv2
import numpy as np

img = cv2.imread('./img/Pic/P2.png', -1)

def focusWindow(event, x, y, flags, param):
    x,y = y,x
    if img.ndim != 3:
        print(f'(x,y) = ({y},{x})')
        print(f'gray-level = ' + '%d' % img[x][y])        
    else:
        print(f'(x,y) = ({y},{x})')
        print(f'(B,G,R) = ({img[x][y][0]}, {img[x][y][1]}, {img[x][y][2]})')
        
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if img[y][x][0] == 36 and img[y][x][1] == 28 and img[y][x][2] == 237:
            img[y][x][2] = 0
            img[y][x][1] = 0
            img[y][x][0] = 255
        if img[y][x][0] == 88 and img[y][x][1] == 249 and img[y][x][2] == 11:
            img[y][x][2] = 0
            img[y][x][1] = 255
            img[y][x][0] = 255
        if img[y][x][0] == 204 and img[y][x][1] == 72 and img[y][x][2] == 63:
            img[y][x][2] = 255
            img[y][x][1] = 128
            img[y][x][0] = 0

cv2.imshow('Temp',img)
cv2.setMouseCallback('Temp', focusWindow)
cv2.waitKey()