import numpy as np
import cv2
from utils import houghCircle

img = cv2.imread('./hw_3/sample.jpg', 0)
houghCircle(img = img)