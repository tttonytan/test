import cv2
import numpy as np
import os
for img in os.listdir(r'C:\Users\16561\Desktop\MODNet-master\input\test'):
    user_im = cv2.imread(os.path.join(r'C:\Users\16561\Desktop\MODNet-master\input\test', img), 1)
    mask = cv2.imread(os.path.join(r'C:\Users\16561\Desktop\MODNet-master\output', img), 0)
    kernel = np.ones((10, 10), np.uint8)
    mask2 = cv2.erode(mask, kernel, iterations=1)
    cv2.imwrite(os.path.join(r'C:\Users\16561\Desktop\MODNet-master\mask_erode', img), mask2)
    cv2.imwrite(os.path.join(r'C:\Users\16561\Desktop\MODNet-master\mask', img), mask)
    cv2.imshow("erode", mask2)
    cv2.imshow("org", mask)
    b_bg = 255 * np.zeros((user_im.shape[0], user_im.shape[1]))
    # print(b_bg.shape)
    g_bg = 255 * np.zeros((user_im.shape[0], user_im.shape[1]))
    r_bg = 255 * np.ones((user_im.shape[0], user_im.shape[1]))
    bg = cv2.merge((b_bg, g_bg, r_bg))
    np.set_printoptions(threshold=np.inf)

    b_user, g_user, r_user = cv2.split(user_im)
    final_b = b_user * (mask2/255) + (1-mask2/255)*b_bg
    # print(final_b)
    final_g = g_user * (mask2/255) + (1-mask2/255)*g_bg
    final_r = r_user * (mask2/255) + (1-mask2/255)*r_bg
    finale = cv2.merge((final_b, final_g, final_r))
    # cv2.imshow(" ", finale)
    cv2.imwrite(os.path.join(r'C:\Users\16561\Desktop\MODNet-master\changebg_result\red', img), finale)
    # cv2.waitKey(0)