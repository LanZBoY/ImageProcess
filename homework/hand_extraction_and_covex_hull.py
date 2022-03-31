import cv2
import numpy as np
from utils import *

img = cv2.imread('./homework/9112.jpg')
img = cv2.resize(img,(250, 500))
# cv2.imshow('rgb',img)
# cv2.setMouseCallback('rgb',focusWindow, param = img)
rgb_hand_extraction_img = rgb_hand_extraction(img)
# cv2.imshow('rgb_hand_extraction',rgb_hand_extraction_img)
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# cv2.imshow('hsv',hsv_img)
# cv2.setMouseCallback('hsv',focusWindow, param = hsv_img)
hsv_hand_extraction_img = hsv_hand_extraction(hsv_img)
# cv2.imshow('hsv_hand_extraction_version_img', hsv_hand_extraction_img)
boundary_extraction_img = boundary_extraction(hsv_hand_extraction_img)
cv2.imshow('Boundary Extraction', boundary_extraction_img)
cv2.waitKey()
