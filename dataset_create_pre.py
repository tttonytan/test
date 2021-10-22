import cv2
import os
from scipy.ndimage import grey_dilation, grey_erosion
import random
import numpy as np
from scipy.ndimage import morphology
"""
image (torch.autograd.Variable): input RGB image
                                          its pixel values should be normalized
trimap (torch.autograd.Variable): trimap used to calculate the losses
                                          its pixel values can be 0, 0.5, or 1
                                          (foreground=1, background=0, unknown=0.5)
gt_matte (torch.autograd.Variable): ground truth alpha matte
                                        its pixel values are between [0, 1]
                                        
红色底照片265张

"""


"""
关于trimap制作
from scipy.ndimage import grey_dilation, grey_erosion

trimap = (matte >= 0.9).astype('float32')
not_bg = (matte > 0).astype('float32')

d_size = self.im_size // 256 * random.randint(10, 20)
e_size = self.im_size // 256 * random.randint(10, 20)

trimap[np.where((grey_dilation(not_bg, size=(d_size, d_size))
    - grey_erosion(trimap, size=(e_size, e_size))) != 0)] = 0.5
where matte is the ground truth alpha normalized to [0, 1], d_size and e_size are the hyper-params.
"""
# input_file_dir = r'F:\HighVision_Data\dataset_withbg'
# input_file_dir = r'F:\HighVision_Data\user_img\DATASET\user_img_3w_matting_final'
# input_file_dir = r'F:\HighVision_Data\user_img\DATASET\matting_resize'
input_file_dir = r'F:\HighVision_Data\user_img\DATASET\dataset\rgb_dataset'
# alpha_file_dir = r'C:\Users\16561\Desktop\MODNet-master\MODNet-master\MattingDataset\alpha_img'
alpha_file_dir = r'F:\HighVision_Data\user_img\DATASET\Alpha_dataset'
# trimap_file_dir = r'C:\Users\16561\Desktop\MODNet-master\MODNet-master\MattingDataset\trimap_img'
trimap_file_dir = r'F:\HighVision_Data\user_img\DATASET\Trimap_dataset2'
# rgbimg_org_file_dir = r'C:\Users\16561\Desktop\MODNet-master\MODNet-master\MattingDataset\data_before\rgborg_img'
rgbimg_org_file_dir = r'F:\HighVision_Data\user_img\DATASET\user_img_3w_rgb_final'
rgbimg_resize_file_dir = r'F:\HighVision_Data\user_img\DATASET\rgb_resize'
mattingimg_resize_file_dir = r'F:\HighVision_Data\user_img\DATASET\matting_resize'
for img in os.listdir(input_file_dir):
    user_img = cv2.imread(os.path.join(input_file_dir, img), -1)
    b, g, r, a = cv2.split(user_img)
    # print(b.shape)
    # a_resize = cv2.resize(a, (512, 512))
    a_scale_resize = a/255
    trimap = (a_scale_resize >= 0.95).astype('float32')
    not_bg = (a_scale_resize > 0).astype('float32')
    d_size = a.shape[0] // 256 * random.randint(10, 20)
    e_size = a.shape[0] // 256 * random.randint(10, 20)
    trimap[np.where((grey_dilation(not_bg, size=(d_size, d_size))
                     - grey_erosion(trimap, size=(e_size, e_size))) != 0)] = 0.5
    cv2.imwrite(os.path.join(trimap_file_dir, img), trimap*255)
    # cv2.imwrite(os.path.join(alpha_file_dir, img), a_resize)
    # cv2.imwrite(os.path.join(alpha_file_dir, img), a)



# for img in os.listdir(input_file_dir):
#     user_rgbimg = cv2.imread(os.path.join(input_file_dir, img), -1)
#     b_rgb, g_rgb, r_rgb, a_rgb = cv2.split(user_rgbimg)
#     b_rgb_resize = cv2.resize(b_rgb, (512, 512))
#     g_rgb_resize = cv2.resize(g_rgb, (512, 512))
#     r_rgb_resize = cv2.resize(r_rgb, (512, 512))
#     a_rgb_resize = cv2.resize(a_rgb, (512, 512))
#     matting_resize = cv2.merge((b_rgb_resize, g_rgb_resize, r_rgb_resize, a_rgb_resize))
#     # print(rgb_resize.shape)
#     cv2.imwrite(os.path.join(mattingimg_resize_file_dir, img), matting_resize)


# alpha = cv2.imread(r'C:\Users\16561\Desktop\MODNet-master\MODNet-master\MattingDataset\alpha_img\oxD0h5a0vtIkhBSAVX8FeVo7l6Tw-1623940144-3522.png')
# fg = np.array(np.equal(alpha, 255).astype(np.float32))
# unknown = np.array(np.not_equal(alpha, 0).astype(np.float32))  # unknown = alpha > 0
# unknown = unknown - fg
# unknown = morphology.distance_transform_edt(unknown == 0) <= np.random.randint(1, 20)
# trimap = fg
# trimap[unknown] = 0.5
# print(trimap[:, :, :1].shape)
#trimap_ = trimap[:, :, :1]
#cv2.imwrite('./trimap.png', trimap_*255)

# user_img = cv2.imread(os.path.join(input_file_dir, r'oxD0h5bxkQmVakTOniIJ4OWwMgww-1624592855-3648.png'), -1)
# b, g, r, a = cv2.split(user_img)
# a_scale = cv2.resize(a, (512, 512))
# a_scale = a_scale/255
# cv2.imshow('a', a_scale)
# cv2.imwrite('./a.png', a_scale)
# print(a_scale)
# print(a_scale.shape)


# trimap = cv2.imread(r'C:\Users\16561\Desktop\MODNet-master\MODNet-master\MattingDataset\trimap_img\oxD0h5a0vtIkhBSAVX8FeVo7l6Tw-1623940144-3522.png', 0)
# # np.set_printoptions(threshold=np.inf)
# trimap_ = np.reshape(trimap, (512, 512, 1))
# print(trimap_.shape)
# cv2.waitKey(0)