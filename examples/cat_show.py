import cv2
# TODO
# import matplotlib.pyplot as plt 
# import numpy as np

img = cv2.imread('images/cat.jpg')
print(type(img))

# 方案1:matplotlib可视化 TODO
# plt.imshow(img)
# plt.show()

# 方案2:cv2可视化
cv2.imshow('cat',img)
cv2.waitKey(3000) # [ms]
