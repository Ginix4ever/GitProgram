import   cv2
import  numpy as np
import os
from matplotlib import pyplot as plt


print ("***获取当前目录***")
print (os.getcwd())
print (os.path.abspath(os.path.dirname(__file__)))

imgR=cv2.imread(r'/Users/gaoyuhang/GitProgram/opencv/boat1_resize.jpg') 

print (cv2.__version__)
cv2.imshow("image",imgR)


# 读取图片
img = cv2.imread(r'/Users/gaoyuhang/GitProgram/opencv/boat1_resize.jpg', cv2.IMREAD_UNCHANGED)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((3,5),np.float32)/15

task1=np.array(([1,1,1,1,1],
         [1,1,1,1,1],
         [1,1,1,1,1]),dtype="float32")/15

dst = cv2.filter2D(rgb_img, -1, task1)

titles = ['filter2D Image']
images = [dst]

cv2.imwrite(r'/Users/gaoyuhang/GitProgram/opencv/demo1.jpg',dst)

#for i in range(1):
    #plt.subplot(1, 2, i + 1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([]), plt.yticks([])

plt.show()











cv2.waitKey(0)
cv2.destoryAllWindows()

