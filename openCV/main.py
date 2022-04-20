import cv2
import numpy as np


img = cv2.imread('bluecard.jpg')

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

tmp1 = cv2.imread('blue.png',0)

res = cv2.matchTemplate(img_grey,tmp1,cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res >= threshold)


for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + 10, pt[1] + 10), (0,255,255), 2)

cv2.imshow('Detected',img)