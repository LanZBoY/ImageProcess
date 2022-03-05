from re import T
import time
import numpy as np
import cv2
import os

base_path = 'C:\\Users\\user\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data'
file_face = 'haarcascade_frontalface_default.xml'
file_eyes = 'haarcascade_eye.xml'

faceDectection = cv2.CascadeClassifier(os.path.join(base_path, file_face))

sTime = time.time()

img = cv2.imread('./img/image.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = faceDectection.detectMultiScale(grayimg, 1.01, 1)
for (x, y, w, h) in face:
    img = cv2.rectangle(img, (x, y) , (w, h), (255, 0, 0), 2)

eTime = time.time()

cv2.imshow("result", img)
cv2.waitKey()