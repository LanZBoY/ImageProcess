import cv2
from utils import houghCircle

img = cv2.imread('./hw_3/sample.jpg')
houghCircle(img = img)