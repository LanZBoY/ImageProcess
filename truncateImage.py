import cv2 
import numpy as np
# (15, 118) (471, 584)
def focusWindow(event, x, y, flags, param):
    x,y = y, x
    if img.ndim != 3:
        print(f'(x,y) = ({x},{y})')
        print(f'gray-level = ' + '%d' % img[x][y])        
    else:
        print(f'(x,y) = ({x},{y})')
        print(f'(B,G,R) = ({img[x][y][0]}, {img[x][y][1]}, {img[x][y][2]})')

img = cv2.imread('img\WXZEGID.jpg')
truncate_img = img[15:471, 118:584, :]
# cv2.imshow('Namin', img)
cv2.imshow('New_Namin', truncate_img)
cv2.setMouseCallback("New_Namin", focusWindow)
cv2.waitKey()
cv2.imwrite('./output/new_Naming.jpg', truncate_img)