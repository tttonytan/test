import cv2
import os
import shutil

matting_dataset_path = r'F:\HighVision_Data\user_img\DATASET\matting_resize'
rgb_dataset_path = r'F:\HighVision_Data\user_img\DATASET\rgb_resize'
rgb_dataset_path_final = r'F:\HighVision_Data\user_img\DATASET\Alpha_dataset_rest'
matting_dataset_path_final = r'F:\HighVision_Data\user_img\DATASET\Alpha_dataset'
i=0
for img in os.listdir(rgb_dataset_path):
    img_rgb = img.split('.')[0]
    #print(os.path.join(rgb_dataset_path, img_rgb, '.jpeg'))
    if os.path.exists(os.path.join(rgb_dataset_path_final, img_rgb + '.png')):
        # print(1)
        shutil.move(os.path.join(rgb_dataset_path_final, img_rgb + '.png'), matting_dataset_path_final)

    # if not os.path.exists(os.path.join(rgb_dataset_path, img)):




