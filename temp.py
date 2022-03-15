import cv2
import numpy as np

img = cv2.imread('./homework/namin.jpg', 0)
(w, h) = img.shape
f = np.ones((3,3), dtype=np.int32)

img2 = np.zeros((w,h))

# print(np.mean(f * img[0:3,0:3]))
for x in range(w):
    for y in range(h):
        if(x == 0 or y == 0 or x == w - 1 or y == h -1):
            img2[x][y] = np.mean(f[0:2,0:2] * img[x:x+2, y:y+2])
        else:
            img2[x][y] = np.mean(f * img[x-1:x+2, y-1:y+2])

cv2.imshow("Namin",img2)
cv2.waitKey()