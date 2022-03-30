import cv2 as cv
import numpy as np
img = cv.imread("./homework/Beautiful-Hands.jpg")
img2 = cv.imread("./homework/Beautiful-Hands.jpg")
img3 = cv.imread("./homework/Beautiful-Hands.jpg")
def nothing(x):
    pass

cv.namedWindow('Color Track Bar')

cv.createTrackbar("ri", "Color Track Bar",0,255,nothing)
cv.createTrackbar("rh", "Color Track Bar",0,255,nothing)
cv.createTrackbar("gi", "Color Track Bar",0,255,nothing)
cv.createTrackbar("gh", "Color Track Bar",0,255,nothing)
cv.createTrackbar("bi", "Color Track Bar",0,255,nothing)
cv.createTrackbar("bh", "Color Track Bar",0,255,nothing)

cv.namedWindow('HSV Track Bar')
cv.createTrackbar("hi", "HSV Track Bar",0,179,nothing)
cv.createTrackbar("hh", "HSV Track Bar",0,179,nothing)
cv.createTrackbar("si", "HSV Track Bar",0,255,nothing)
cv.createTrackbar("sh", "HSV Track Bar",0,255,nothing)
cv.createTrackbar("vi", "HSV Track Bar",0,255,nothing)
cv.createTrackbar("vh", "HSV Track Bar",0,255,nothing)

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r and g >= b:
        h = (60 * ((g-b) / df) + 0) / 360
    elif mx == r and g < b:
        h = (60 * ((g-b) / df) + 360) / 360
    elif mx == g:
        h = (60 * ((b-r) / df) + 120) / 360
    elif mx == b:
        h = (60 * ((r-g) / df) + 240) / 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

def Cvtcolor(img):
    height,width,channels = img.shape
    nimg=np.zeros((height,width,channels),np.uint8) 
    rgbv = [0,0,0]
    for i in range(height):
        for j in range(width):
            rgbv = rgb_to_hsv(img[i,j,0],img[i,j,1],img[i,j,2])
            #print(rgbv)
            nimg[i,j] = (rgbv[0], rgbv[1], rgbv[2])
    return nimg

def Erosion(img):
    height,width = 800,800
    bdlen = 1
    img = cv.copyMakeBorder(img,bdlen,bdlen,bdlen,bdlen,cv.BORDER_REFLECT)
    imgc = img.copy()
    for i in range(bdlen, height-bdlen):
        for j in range(bdlen, width-bdlen):
            minv = img[i,j]
            for m in range(-bdlen,bdlen+1):
                for n in range(-bdlen,bdlen+1):
                    if(img[i+m,j+n] < minv):
                        minv = img[i+m,j+n]
            imgc[i,j] = minv
    return imgc

def Dilation(img):
    height,width = 800,800
    bdlen = 1
    img = cv.copyMakeBorder(img,bdlen,bdlen,bdlen,bdlen,cv.BORDER_REFLECT)
    imgc = img.copy()
    for i in range(bdlen, height-bdlen):
        for j in range(bdlen, width-bdlen):
            maxv = img[i,j]
            for m in range(-bdlen,bdlen+1):
                for n in range(-bdlen,bdlen+1):
                    if(img[i+m,j+n] > maxv):
                        maxv = img[i+m,j+n]
            imgc[i,j] = maxv
    return imgc

def opening(img):
    img = Erosion(img)
    img = Dilation(img)
    return img

def closeing(img):
    img = Dilation(img)
    img = Erosion(img)
    return img

hsv = Cvtcolor(img)
hsv2 = Cvtcolor(img2)
hsv3 = Cvtcolor(img3)
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
while(1):
   ri=cv.getTrackbarPos("ri", "Color Track Bar")
   rh=cv.getTrackbarPos("rh", "Color Track Bar")
   gi=cv.getTrackbarPos("gi", "Color Track Bar")
   gh=cv.getTrackbarPos("gh", "Color Track Bar")
   bi=cv.getTrackbarPos("bi", "Color Track Bar")
   bh=cv.getTrackbarPos("bh", "Color Track Bar")
   
   hi=cv.getTrackbarPos("hi", "HSV Track Bar")
   hh=cv.getTrackbarPos("hh", "HSV Track Bar")
   si=cv.getTrackbarPos("si", "HSV Track Bar")
   sh=cv.getTrackbarPos("sh", "HSV Track Bar")
   vi=cv.getTrackbarPos("vi", "HSV Track Bar")
   vh=cv.getTrackbarPos("vh", "HSV Track Bar")  
   
   skinmask = cv.inRange(img,(ri, gi, bi), (rh, gh, bh))
   skinmask2 = cv.inRange(img2,(ri, gi, bi), (rh, gh, bh))
   skinmask3 = cv.inRange(img3,(ri, gi, bi), (rh, gh, bh))
   
   skinmask4 = cv.inRange(hsv,(hi, si, vi), (hh, sh, vh))
   skinmask5 = cv.inRange(hsv2,(hi, si, vi), (hh, sh, vh))
   skinmask6 = cv.inRange(hsv3,(hi, si, vi), (hh, sh, vh))
   
   
   cv.imshow('rgb1',skinmask)
   cv.imshow('rgb2',skinmask2)
   cv.imshow('rgb3',skinmask3)
   #171.137.255
   #cv.imshow('hsv',hsv)
   cv.imshow('hsv1',skinmask4)
   cv.imshow('hsv2',skinmask5)
   cv.imshow('hsv3',skinmask6)
   #cv.imshow('rgb2',skinmask)
   #cv.imshow("ero",Erosion(skinmask))
   #cv.imshow('rgb3',skinmask2)
   #cv.imshow('rgb4',skinmask3)
   #cv.imshow('rgb',img)
   if cv.waitKey(1) == 27:
      break
#skinmask = cv.inRange(img,(0, 0, 0), (170, 150, 140))
#cv.imshow('rgb',img)
#cv.imshow('rgb2',skinmask)
#hsv = Cvtcolor(img)
cv.imwrite("hsvc1.jpg",hsv)
cv.imwrite("hsvc2.jpg",hsv2)
cv.imwrite("hsvc3.jpg",hsv3)

cv.imwrite("rgbr.jpg",skinmask)
cv.imwrite("rgbr2.jpg",skinmask2)
cv.imwrite("rgbr3.jpg",skinmask3)

#cv.imshow('hsv',hsv)
#skinmask2 = cv.inRange(hsv,(140, 70, 70), (190, 130, 255))
#cv.imshow('hs2v',skinmask2)
print("start")
cv.imwrite("rgbo.jpg",opening(skinmask))
cv.imwrite("rgbc.jpg",closeing(skinmask))
cv.imwrite("rgb2o.jpg",opening(skinmask2))
cv.imwrite("rgb2c.jpg",closeing(skinmask2))
cv.imwrite("rgb3o.jpg",opening(skinmask3))
cv.imwrite("rgb3c.jpg",closeing(skinmask3))
cv.imwrite("hsvo.jpg",opening(skinmask4))
cv.imwrite("hsvc.jpg",closeing(skinmask4))
cv.imwrite("hsv2o.jpg",opening(skinmask5))
cv.imwrite("hsv2c.jpg",closeing(skinmask5))
cv.imwrite("hsv3o.jpg",opening(skinmask6))
cv.imwrite("hsv3c.jpg",closeing(skinmask6))
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows()