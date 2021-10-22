import cv2
import os
from scipy.ndimage import grey_dilation, grey_erosion
import random
import numpy as np
from scipy.ndimage import morphology

input_file_dir = r'F:\HighVision_Data\user_img\third_time'
save_dir = r'F:\HighVision_Data\dataset_withbg\fourthtime_BR_bg'
bg_dict = {0:[255, 217, 123], 1: [49, 72, 224], 2:[185, 106, 3], 3:[198, 248, 254], 4:[218, 142, 66], 5:[221, 239, 210], 6:[0, 0, 255], 7:[243, 214, 229], 8:[106, 96, 89], 9:[231, 232, 192], 10:[117, 117, 117], 11:[245, 221, 209], 12:[255, 255, 255], 13:[106, 96, 79], 14:[172, 147, 127], 15:[140, 155, 171]}

for img in os.listdir(input_file_dir):
    seed = random.randint(0, 1)
    user_img = cv2.imread(os.path.join(input_file_dir, img), -1)
    b_usr, g_usr, r_usr, a_usr = cv2.split(user_img)
    a_resize = cv2.resize(a_usr, (512, 512))
    b_resize = cv2.resize(b_usr, (512, 512))
    g_resize = cv2.resize(g_usr, (512, 512))
    r_resize = cv2.resize(r_usr, (512, 512))
    bg = np.ones((a_resize.shape[0], a_resize.shape[1]), dtype=np.uint8)
    b = np.zeros((a_resize.shape[0], a_resize.shape[1]), dtype=np.uint8)
    g = np.zeros((a_resize.shape[0], a_resize.shape[1]), dtype=np.uint8)
    r = np.zeros((a_resize.shape[0], a_resize.shape[1]), dtype=np.uint8)
    if seed == 0:
        b = bg_dict[0][0]
        g = bg_dict[0][1]
        r = bg_dict[0][2]
    if seed == 1:
        b = bg_dict[1][0]
        g = bg_dict[1][1]
        r = bg_dict[1][2]

    b_final = b_resize * (a_resize / 255) + b * (1 - a_resize / 255)
    g_final = g_resize * (a_resize / 255) + g * (1 - a_resize / 255)
    r_final = r_resize * (a_resize / 255) + r * (1 - a_resize / 255)
    # print(a_resize)
    result = cv2.merge((b_final, g_final, r_final))
    # cv2.imshow(' ', result)
    # cv2.waitKey(0)
    cv2.imwrite(os.path.join(save_dir, img), result)


