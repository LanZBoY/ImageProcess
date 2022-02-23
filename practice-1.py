# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:36:28 2022

@author: user
"""
#(371, 207)(444, 359)
import cv2
import numpy as np


img = cv2.imread('./img/test1.jpg', -1)

def focusWindow(event, x, y, flags, param):
    x,y = y, x
    if img.ndim != 3:
        print(f'(x,y) = ({x},{y})')
        print(f'gray-level = ' + '%d' % img[x][y])        
    else:
        print(f'(x,y) = ({x},{y})')
        print(f'(B,G,R) = ({img[x][y][0]}, {img[x][y][1]}, {img[x][y][2]})')
        
cv2.rectangle(img, (152, 152), (228,306), (27,36,237), -1)
cv2.rectangle(img, (350, 200), (450,370), (255,255,255), -1)
cv2.imshow("Window", img)
cv2.setMouseCallback("Window", focusWindow)
cv2.waitKey()