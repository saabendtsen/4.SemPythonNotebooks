import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bluemana.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

tmp1 = cv2.imread('blue.png',0)



res = cv2.matchTemplate(img_grey,tmp1,cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res >= threshold)

print(loc)


for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + 1, pt[1] + 1), (0,255,255), 2)

#cv2.imshow('Detected',img)

plt.show()
