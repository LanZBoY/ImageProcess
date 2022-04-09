import cv2
import numpy as np
from utils import *

img_name = '9112'
img = cv2.imread(f'./homework_2/{img_name}.jpg')
img = cv2.resize(img,(250, 500))
print('rgb hand extraction...')
rgb_hand_extraction_img = rgb_hand_extraction(img)
print('OK')
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
print('hsv hand extraction...')
hsv_hand_extraction_img = hsv_hand_extraction(hsv_img)
print('OK')
print('boundary_extraction...')
boundary_extraction_img = boundary_extraction(hsv_hand_extraction_img)
print('OK')
print('convex_hull...')
convex_hull_img = convex_hull(hsv_hand_extraction_img)
print('OK')
cv2.imwrite(f"./homework_2/{img_name}_rgb_1.jpg", img)
rgb_hand_extraction_img = rgb_hand_extraction_img * 255.
cv2.imwrite(f"./homework_2/{img_name}_rgb_hand_extraction_1.jpg", rgb_hand_extraction_img)
cv2.imwrite(f"./homework_2/{img_name}_hsv_1.jpg", hsv_img)
hsv_hand_extraction_img = hsv_hand_extraction_img * 255.
cv2.imwrite(f"./homework_2/{img_name}_hsv_hand_extraction_version_img_1.jpg", hsv_hand_extraction_img)
boundary_extraction_img = boundary_extraction_img * 255.
cv2.imwrite(f"./homework_2/{img_name}_boundary_extraction_img_1.jpg", boundary_extraction_img)
convex_hull_img = convex_hull_img * 255.
cv2.imwrite(f"./homework_2/{img_name}_convex_hull_img_1.jpg", convex_hull_img)