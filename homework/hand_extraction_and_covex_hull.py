import cv2
import numpy as np

def focusWindow(event, x, y, flags, param):
    x,y = y, x
    print(f'(x,y) = ({x},{y})')
    
    print(f'(H,S,V) = ({img[x][y][0]}, {img[x][y][1]}, {img[x][y][2]})')

def hsv_hand_extraction_version(img):
    new_img = img.copy()
    cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    hand_extraction_img = np.full((new_img.shape[0], new_img.shape[1]), fill_value = 1., dtype = np.float32)
    for x in range(new_img.shape[0]):
        for y in range(new_img.shape[1]):
            if(new_img[x][y][0] >= 80 and new_img[x][y][0] <= 130):
                hand_extraction_img[x][y] = 0.
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

img = cv2.imread('./homework/9112.jpg')
img = cv2.resize(img,(250, 500))
cv2.imshow('rgb',img)
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imshow('hsv',hsv_img)
cv2.setMouseCallback('hsv',focusWindow)
hsv_hand_extraction_version_img = hsv_hand_extraction_version(hsv_img)
cv2.imshow('hsv_hand_extraction_version_img', hsv_hand_extraction_version_img)
# dilation_img = Dilation(hsv_hand_extraction_version_img)
opening_img = Opening(hsv_hand_extraction_version_img)
cv2.imshow('Opening',opening_img)
erosion_img = Erosion(opening_img)
boundary_extraction_img = opening_img - erosion_img
cv2.imshow('Boundary Extraction', boundary_extraction_img)
cv2.waitKey()
