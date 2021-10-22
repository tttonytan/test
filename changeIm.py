import cv2
import numpy as np
im = cv2.imread(r'C:\Users\16561\Desktop\50b482fccc6290deaf234f865d8b5ab.jpg')
b_, g_, r_ = cv2.split(im)
#g_ = 255*np.ones((g_.shape[0], g_.shape[1]),dtype=np.uint8)
b_ = b_-50
r_ = r_-50
g_ = g_-50
im_ = cv2.merge((b_, g_, r_))
cv2.imshow(' ', im_)
cv2.imwrite('./re.png', im_)
cv2.waitKey(0)