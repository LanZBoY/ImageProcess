import numpy as np
import cv2
from math import sin, cos, pi


def houghCircle(img, method = None, dp = None, minDist = None, high_threshold = 360, low_threshold = 200, minRadius = 10, maxRadius = 15):
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(img_g.shape)
    if(dp != None):
        pass
    (h, w) = img_g.shape
    gaussianImg = cv2.GaussianBlur(img_g, (3, 3), 0)
    cannyImg = cv2.Canny(gaussianImg, 30, 150)
    for r in range(minRadius, maxRadius + 1):
        vote_map = np.zeros((h, w), dtype=np.uint8)
        candidate_set = set()
        for y in range(r, h - r):
            for x in range(r, w - r):
                if(cannyImg[y,x] != 0):
                    for t in range(0, 360):
                        b = y - int(r * sin(t * pi / 180))
                        a = x - int(r * cos(t * pi / 180))
                        vote_map[b,a] += 1
                        if(((a,b) not in candidate_set) and vote_map[b, a] < high_threshold and vote_map[b,a] >= low_threshold):
                            candidate_set.add((a, b))
        for (a,b) in candidate_set:
            cv2.circle(img,(b,a), r, (255, 0, 0), 1)
    cv2.imshow("Result", img)
    cv2.waitKey()
                        
                        