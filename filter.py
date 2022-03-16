import cv2
import numpy as np

img = cv2.imread('./homework/namin.jpg', 0)
(w, h) = img.shape
f = np.ones((3,3))
img2 = np.zeros((w,h), dtype="uint8")

print(np.mean(f * img[0:3,0:3]))
for x in range(1, w):
    for y in range(1, h):
        if(x == 0 or y == 0 or x == w - 1 or y == h - 1):
            pass
            # img2[x][y] = int(np.mean(f[0:2,0:2] * img[x:x+2, y:y+2]))
        else:
            img2[x][y] = int(np.mean(f * img[x-1:x+2, y-1:y+2]))
cv2.imshow("SRC",img)
cv2.imshow("Namin",img2)
cv2.waitKey()