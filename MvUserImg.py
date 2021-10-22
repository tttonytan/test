import os
import shutil
root = r'F:\HighVision_Data\HeadMattingTest\result_image'
# root = r'F:\HighVision_Data\HeadMattingTest\ali_output'
# root = r'F:\HighVision_Data\headMatting_dataset'
# usrimg_save_dir = r'F:\HighVision_Data\user_img\user_img_headmatting'
usrimg_save_dir = r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics_same'
# for dir_1 in os.listdir(root):
#     for dir_2 in os.listdir(os.path.join(root, dir_1)):
#         path_oldimg_dir = root+'\\'+dir_1+'\\'+'new-image'
#         if os.path.exists(path_oldimg_dir):
#             for img in os.listdir(path_oldimg_dir):
#                 if not os.path.exists(os.path.join(path_oldimg_dir, img)):
#                     shutil.move(os.path.join(path_oldimg_dir, img), usrimg_save_dir)

# for dir_1 in os.listdir(root):
#     for dir_2 in os.listdir(os.path.join(root, dir_1)):
#         path_oldimg_dir = root+'\\'+dir_1+'\\'+'old-image'
#         # print(path_oldimg_dir)
#         if os.path.exists(path_oldimg_dir):
#             for img in os.listdir(path_oldimg_dir):
#                 if not os.path.exists(os.path.join(path_oldimg_dir, img)):
#                     shutil.move(os.path.join(path_oldimg_dir, img), usrimg_save_dir)

for img in os.listdir(root):
    img_jpeg = img.split('.')[0] + '.jpeg'
    img_jpg = img.split('.')[0] + '.jpg'
    # print(img)
    # path_oldimg_dir = root+'\\'+'old-image'
    # print(path_oldimg_dir)
    if os.path.exists(os.path.join(r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics', img)):
        # print(os.path.join(r'F:\HighVision_Data\user_img\DATASET\rgb_dataset_same', img))
        shutil.move(os.path.join(r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics', img), usrimg_save_dir)
    if os.path.exists(os.path.join(r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics', img_jpeg)):
        # print(os.path.join(r'F:\HighVision_Data\user_img\DATASET\rgb_dataset_same', img))
        shutil.move(os.path.join(r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics', img_jpeg), usrimg_save_dir)
    if os.path.exists(os.path.join(r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics', img_jpg)):
        # print(os.path.join(r'F:\HighVision_Data\user_img\DATASET\rgb_dataset_same', img))
        shutil.move(os.path.join(r'F:\HighVision_Data\head_matting_dataset\org_rgb_pics', img_jpg), usrimg_save_dir)

