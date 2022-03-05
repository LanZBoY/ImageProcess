import numpy as np
import cv2

video = cv2.VideoCapture('./video/video.mp4')

while(video.isOpened()):
    ret, frame = video.read()
    cv2.imshow('Video', frame)
    # ESC
    if(cv2.waitKey(30) == 27):
        break

video.release()
cv2.destroyAllWindows()