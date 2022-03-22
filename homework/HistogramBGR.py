import cv2
import matplotlib.pyplot as plt

'''
這是三個通道個別計算均質化的結果
'''

img = cv2.imread("./homework/namin.jpg", -1)
cv2.imshow("Namin", img)
grayCount = [[0] * 256, [0] * 256, [0] * 256]
w,h,c = img.shape
if(c==4):
    c -= 1

for x in range(w):
    for y in range(h):
        for z in range(c):
            grayCount[z][img[x][y][z]] += 1

grayCDFList = [[0] * 256, [0] * 256, [0] * 256]

for i in range(c):
    sum = 0
    for j in range(256):
        sum += grayCount[i][j]
        grayCDFList[i][j] = sum

# 連續均質化

time = int(input("輸入均質化次數: "))
for i in range(time):
    for x in range(w):
        for y in range(h):
            for z in range(c):
                img[x][y][z] = grayCDFList[z][img[x][y][z]] / grayCDFList[z][-1] * 255

# for x in range(w):
#     for y in range(h):
#         for z in range(c):
#             img[x][y][z] = grayCDFList[z][img[x][y][z]] / grayCDFList[z][-1] * 255

cv2.imshow("NaminAFTER", img)
cv2.waitKey()