import os
import numpy as np
import cv2

def resize_image(root_path,save_path):
    for dir_name in os.listdir(root_path):  # dir_name是1,2,3,4,5，...9
        save_file_path = os.path.join(save_path, dir_name)
        if not os.path.exists(save_file_path):
            os.makedirs(save_file_path)
            for img_name in os.listdir(root_path + '//' + dir_name):
                img_path = os.path.join(root_path, dir_name, img_name)
                image = cv2.imread(img_path)
                cropped_image = image[0:448, 0:448]
                cv2.imwrite(os.path.join(save_file_path,img_name), cropped_image)

if __name__ == '__main__':
    resize_image('E:/yarn_twist_new/resizeyarn_dataset', 'E:/yarn_twist_new/448_dataset')

