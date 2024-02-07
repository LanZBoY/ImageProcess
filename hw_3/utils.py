import numpy as np
import cv2
from math import sin, cos, pi

def houghCircle(img, method = None, dp = 1.0, minDist = None, high_threshold = 360, low_threshold = 20, minRadius = 5, maxRadius = 5):
    (h, w, c) = img.shape
    if(dp!= 1.0):
        h = int(h * dp)
        w = int(w * dp)
        reuslt_img = cv2.resize(img, (w, h))
    else:
        reuslt_img = img.copy()
    img_g = cv2.cvtColor(reuslt_img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(img_g, (3, 3), 0)
    cannyImg = cv2.Canny(gaussianImg, 30, 150)
    for r in range(minRadius, maxRadius + 1):
        vote_map = np.zeros((h, w), dtype = np.uint8)
        candidate_set = set()
        for y in range(r, h - r):
            for x in range(r, w - r):
                if(cannyImg[y,x] != 0):
                    voted_set = set()
                    for t in range(0, 360):
                        b = y - int(r * sin(t * pi / 180))
                        a = x - int(r * cos(t * pi / 180))
                        if((a,b) not in voted_set):
                            vote_map[b,a] += 1
                            voted_set.add((a, b))
                        if(((a,b) not in candidate_set) and vote_map[b, a] < high_threshold and vote_map[b,a] >= low_threshold):
                            candidate_set.add((a, b))
        for (a,b) in candidate_set:
            cv2.circle(reuslt_img,(a,b), r, (0, 0, 255), 2)
    return reuslt_img
