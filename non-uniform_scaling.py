import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2, math
import numpy as np
import csv
import random


def scaling(image, scale):
    return cv2.resize(image, None, fx=1, fy=scale, interpolation=cv2.INTER_LANCZOS4)


def TestOneDir():
    root_path = 'E:/yarn_twist_new/ori_yarn_twist'
    save_path = 'E:/yarn_twist_new/resizeyarn_dataset'
    label_csv = 'E:/yarn_twist_new/data/ori_label.csv'
    csv_file = 'E:/yarn_twist_new/data/new_csv.csv'


    labels = pd.read_csv(label_csv)

    for dir_name in os.listdir(root_path):  # dir_name是1,2,3,4,5，...9
        s1 = labels.loc[:, 'filename']  # 取filename的所有行
        file_index = s1[s1 == int(dir_name)].index
        ori_label = labels.iloc[file_index, 1].values[0]

        # 创建存储文件夹，如果不存在则创建
        save_file_path = os.path.join(save_path, dir_name)
        if not os.path.exists(save_file_path):
            os.makedirs(save_file_path)

        for img_name in os.listdir(root_path + '\\' + dir_name):
            img_path = os.path.join(root_path, dir_name, img_name)
            img_i = cv2.imread(img_path)


            for i in range(4):
                if ori_label < 0.51:
                    rd1 = random.uniform(1, 1.25)
                    img_scale1 = scaling(img_i, rd1)
                    new_img_name1 = img_name[:-4] + '_' + str(i) + "_scale_" + ".bmp"
                    cv2.imwrite(os.path.join(save_file_path, new_img_name1), img_scale1)
                    label1 = ori_label * rd1
                    with open(csv_file, 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow((dir_name, new_img_name1, label1))
                else:
                    rd2 = random.uniform(0.8, 1)  # 随机产生数字,但是每一次迭代rand都会变，必须让他不变才行
                    img_scale2 = scaling(img_i, rd2)
                    new_img_name2 = img_name[:-4] + '-' + str(i) + "_scale_" + ".bmp"
                    cv2.imwrite(os.path.join(save_file_path,  new_img_name2), img_scale2)  # 在名字这里做标注
                    label2 = ori_label * rd2
                    with open(csv_file, 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow((dir_name, new_img_name2, label2))


if __name__ == '__main__':
    TestOneDir()
