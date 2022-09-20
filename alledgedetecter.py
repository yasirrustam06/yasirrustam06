import cv2

import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("HALma.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

canny=cv2.Canny(gray,100,200,apertureSize=3)
cv2.imshow("image",img)
cv2.imshow("sobel",sobelx)
cv2.imshow("sobel",sobely)
cv2.imshow("canny",canny)

cv2.waitKey()
cv2.destroyAllWindows()













