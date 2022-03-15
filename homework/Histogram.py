from re import L
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./homework/namin.jpg', 0)
imgBGR = cv2.imread('./homework/namin.jpg', -1)
cv2.imshow("SRC", imgBGR)
cv2.waitKey()
list = [0] * 256

(w, h, c) = imgBGR.shape
for x in range(w):
    for y in range(h):
        list[img[x][y]] += 1

plt.subplot(3, 1, 1)
plt.plot(range(len(list)), list)

cdf = 0
addList = [0] * 256
for i, number in enumerate(list):
    cdf += number
    addList[i] = cdf

plt.subplot(3, 1, 2)
plt.plot(range(len(addList)), addList)



for x in range(w):
    for y in range(h):
        img[x][y] = addList[img[x][y]] / cdf * 255

afterList = [0] * 256
for x in range(w):
    for y in range(h):
        afterList[img[x][y]] += 1

plt.subplot(3, 1, 3)
plt.plot(range(len(afterList)), afterList)

for x in range(w):
    for y in range(h):
        for z in range(c):
            imgBGR[x][y][z] = imgBGR[x][y][z] * addList[img[x][y]] / cdf

plt.show()
cv2.imshow("naminGray", img)
cv2.imshow("naminBGR", imgBGR)
cv2.waitKey()