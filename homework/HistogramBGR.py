import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./homework/namin.jpg', -1)

(w, h, c) = img.shape

# for x in range(w):
#     for y in range(h):
#         for i in range(c):
            