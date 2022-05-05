import numpy as np
import cv2


def houghCircle(img, method = None, dp = None, minDist = None, high_threshold = None, low_threshold = None, minRadius = 10, maxRadius = 30):
    if(dp != None):
        pass
    (h, w) = img.shape
    gaussianImg = cv2.GaussianBlur(img, (3, 3), 0)
    cannyImg = cv2.Canny(gaussianImg, 30, 150)
    for radius in range(minRadius, maxRadius + 1):
        vote_map = np.zeros((h, w))
        for y in range(h):
            for x in range(w):
                if(img[y,x] != 0):
                    pass
