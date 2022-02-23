# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:23:00 2022

@author: user
"""

import cv2
import numpy as np

img = cv2.imread('./img/WXZEGID.jpg', -1)

def focusWindow(event, x, y, flags, param):
    x,y = y,x
    if img.ndim != 3:
        print(f'(x,y) = ({x},{y})')
        print(f'gray-level = ' + '%d' % img[x][y])        
    else:
        print(f'(x,y) = ({x},{y})')
        print(f'R =  '+ '%d' % img[x][y][2])
        print(f'G =  '+ '%d' % img[x][y][1])
        print(f'B =  '+ '%d' % img[x][y][0])



cv2.imshow("onWindow", img)
cv2.setMouseCallback("onWindow", focusWindow)
cv2.waitKey()