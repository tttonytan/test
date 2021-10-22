import cv2
import numpy as np


def makeEdgeMask(mask, width):
    kernel = np.ones((width, width), np.uint8)

    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    return dilation - erosion

def makeTrimap(mask, width = 5):
   edgeMask = makeEdgeMask(mask, width)
   trimap = mask.astype(np.float)
   trimap[edgeMask == 1] = 0.5
   return trimap

mask = cv2.imread(r'F:\HighVision_Data\user_img\DATASET\matting_resize\1630222039553.png')

trimap = makeTrimap(mask, 512)
cv2.imshow(' asd', trimap)
cv2.waitKey(0)
cv2.imwrite('./trimap_.jpg', trimap)