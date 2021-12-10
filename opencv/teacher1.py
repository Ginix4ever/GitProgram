# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:33:28 2021

@author: NEdzv
"""

import numpy as np
import cv2 as cv
img=cv.imread(r'/Users/gaoyuhang/GitProgram/opencv/boat1_resize.jpg',0)
kernel1=np.array([[1,1,1],
                [1,1,1],
                [0,0,-0],
                [-1,-1,-1],
                [-1,-1,-1]])
img=cv.copyMakeBorder(img,1,1,2,2,cv.BORDER_REPLICATE)
for i in range(0,321,1):
    for j in range(0,492,1):
        img[i+1,j+2]=np.sum(np.multiply(img[i:i+3,j:j+5],kernel1))

img=img[1:323,2:495]
cv.imshow("1",img)
cv.waitKey(0)
#cv.destroyAllWindows()
#cv.imwrite(r'/Users/gaoyuhang/GitProgram/opencv/demo4.jpg',img)


