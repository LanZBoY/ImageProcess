from trace import Trace
from typing import Tuple
import cv2
import numpy as np

def focusWindow(event, x, y, flags, param):  
    x,y = y,x
    print(f'(x,y) = ({x},{y})')
    print(f'({param[x][y][0]}, {param[x][y][1]}, {param[x][y][2]})')

def rgb_hand_extraction(img):
    new_img = img.copy()
    hand_extraction_img = np.full((new_img.shape[0], new_img.shape[1]), fill_value = 0., dtype = np.float32)
    for x in range(new_img.shape[0]):
        for y in range(new_img.shape[1]):
            if(new_img[x][y][0] >= 71 and new_img[x][y][0] <= 193) and (new_img[x][y][1] >= 84 and new_img[x][y][1] <= 148) and (new_img[x][y][2] >= 110 and new_img[x][y][2] <= 190):
                hand_extraction_img[x][y] = 1.
    return hand_extraction_img

def hsv_hand_extraction(img):
    new_img = img.copy()
    hand_extraction_img = np.full((new_img.shape[0], new_img.shape[1]), fill_value = 0., dtype = np.float32)
    for x in range(new_img.shape[0]):
        for y in range(new_img.shape[1]):
            if(new_img[x][y][0] >= 80 and new_img[x][y][0] <= 130):
                hand_extraction_img[x][y] = 1.
    return hand_extraction_img

def Dilation(img):
    border_img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REFLECT)
    result_img = np.zeros((border_img.shape[0] - 2, border_img.shape[1] - 2), dtype=np.float32)
    for x in range(1, border_img.shape[0] - 1):
        for y in range(1, border_img.shape[1] - 1):
            result_img[x-1, y-1] = np.max(border_img[x-1:x+2, y-1:y+2])
    return result_img

def Erosion(img):
    border_img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REFLECT)
    result_img = np.zeros((border_img.shape[0] - 2, border_img.shape[1] - 2), dtype=np.float32)
    for x in range(1, border_img.shape[0] - 1):
        for y in range(1, border_img.shape[1] - 1):
            result_img[x-1, y-1] = np.min(border_img[x-1:x+2, y-1:y+2])
    return result_img

def Opening(img):
    y = Erosion(img)
    y = Dilation(y)
    return y

def Closing(img):
    y = Dilation(img)
    y = Erosion(y)
    return y

def boundary_extraction(img):
    copy_img = img.copy()
    erosion_img = Erosion(copy_img)
    resutl_img = copy_img - erosion_img
    return resutl_img

def match_line(img, bx = 0,by = 0):
    border_img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0.)
    (border_h, border_w) = border_img.shape
    for y in range(1, border_h - 1):
        for x in range(1, border_w - 1):
            if((border_img[y - 1: y + 2, x] == [1.,1.,1.]).all()):
                border_img[y + by , x + bx] = 1.
            if((border_img[y, x - 1: x + 2] == [1.,1.,1.]).all()):
                border_img[y + by , x + bx] = 1.
    return border_img[1:border_h-1, 1:border_w-1]

def convex_hull(img):
    prev_img = img.copy()
    print('convex_hull - 0/4')
    while(True):
        current = match_line(prev_img, bx = 1)
        if((current == prev_img).all()):
            break
        prev_img = current
    print('convex_hull - 1/4')
    while(True):
        current = match_line(prev_img, bx = -1)
        if((current == prev_img).all()):
            break
        prev_img = current
    print('convex_hull - 2/4')
    while(True):
        current = match_line(prev_img, by = 1)
        if((current == prev_img).all()):
            break
        prev_img = current
    print('convex_hull - 3/4')
    while(True):
        current = match_line(prev_img, by = -1)
        if((current == prev_img).all()):
            break
        prev_img = current
    print('convex_hull - 4/4')