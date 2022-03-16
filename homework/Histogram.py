from re import L
import cv2
import matplotlib.pyplot as plt

# 讀取圖片
img = cv2.imread('./homework/namin2.png', 0)
imgBGR = cv2.imread('./homework/namin2.png', -1)
# 顯示原本的圖片
cv2.imshow("SRCBGR", imgBGR)
cv2.imshow("SRCGRAY",img)
cv2.waitKey()
# 初始化List
list = [0] * 256

(w, h, c) = imgBGR.shape

# 計算灰階數目
for x in range(w):
    for y in range(h):
        list[img[x][y]] += 1
# 畫出灰階0~255各個數目的統計
plt.subplot(3, 1, 1)
plt.plot(range(len(list)), list)

# 宣告累加數
cdf = 0
addList = [0] * 256
# 計算到i個的累加數
for i, number in enumerate(list):
    cdf += number
    addList[i] = cdf

# 畫出累加圖
plt.subplot(3, 1, 2)
plt.plot(range(len(addList)), addList)

# 直方圖均化計算
for x in range(w):
    for y in range(h):
        img[x][y] = addList[img[x][y]] / cdf * 255

# 計算均化後各個灰階值的數目
afterList = [0] * 256
for x in range(w):
    for y in range(h):
        afterList[img[x][y]] += 1

plt.subplot(3, 1, 3)
plt.plot(range(len(afterList)), afterList)

# RGB版本直方圖均化
for x in range(w):
    for y in range(h):
        for z in range(c):
            imgBGR[x][y][z] = imgBGR[x][y][z] * addList[img[x][y]] / cdf

plt.show()
cv2.imshow("naminGray", img)
cv2.imshow("naminBGR", imgBGR)
cv2.waitKey()