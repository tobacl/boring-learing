import os
import random
import shutil
from shutil import copy2
import pandas as pd
import csv

def data_set_split(src_data_folder, target_data_folder, train_scale=0.8, val_scale=0.1, test_scale=0.1):
    '''
    读取源数据文件夹，生成划分好的文件夹，分为trian、val、test三个文件夹进行
    :param src_data_folder: 源文件夹 E:/biye/gogogo/note_book/torch_note/data/utils_test/data_split/src_data
    :param target_data_folder: 目标文件夹 E:/biye/gogogo/note_book/torch_note/data/utils_test/data_split/target_data
    :param train_scale: 训练集比例
    :param val_scale: 验证集比例
    :param test_scale: 测试集比例
    :return:
    '''
    print("开始数据集划分")
    class_names = os.listdir(src_data_folder)  #1,2，3,4....
    ori_csv = 'E:/yarn_twist_new/csv/new_csv.csv'
    csv_file = 'E:/yarn_twist_new/csv/final_csv.csv'
    df = pd.read_csv(ori_csv)
    s1 = df.iloc[:, 1]


    # 在目标目录下创建文件夹
    split_names = ['train', 'val', 'test']
    for split_name in split_names:
        split_path = os.path.join(target_data_folder, split_name)   #dataset-train,val,test
        if os.path.isdir(split_path):
            pass
        else:
            os.mkdir(split_path)
        # 然后在split_path的目录下创建类别文件夹
        for class_name in class_names:
            class_split_path = os.path.join(split_path, class_name)  #dataset-train,val,test-1,2,3,4,5....
            if os.path.isdir(class_split_path):
                pass
            else:
                os.mkdir(class_split_path)

    # 按照比例划分数据集，并进行数据图片的复制
    # 首先进行分类遍历
    for class_name in class_names:
        current_class_data_path = os.path.join(src_data_folder, class_name)
        current_all_data = os.listdir(current_class_data_path)          #所有文件名
        current_data_length = len(current_all_data)
        current_data_index_list = list(range(current_data_length))     #[0,1,.....,n] n个文件

        train_folder = os.path.join(os.path.join(target_data_folder, 'train'), class_name)
        val_folder = os.path.join(os.path.join(target_data_folder, 'val'), class_name)
        test_folder = os.path.join(os.path.join(target_data_folder, 'test'), class_name)
        train_stop_flag = current_data_length * train_scale
        val_stop_flag = current_data_length * (train_scale + val_scale)
        current_idx = 0
        train_num = 0
        val_num = 0
        test_num = 0
        for i in current_data_index_list:  #current_data_index_list是一个列表[0,1,.....,n] ，里面有n个文件
            src_img_path = os.path.join(current_class_data_path, current_all_data[i])  #current_all_data[i]是图片名字
            file_index = s1[s1 == current_all_data[i]].index  # 取出某一行，file_index即为某一行
            label = df.iloc[file_index, 2].values[0]  # 找出对应label
            img_name =current_all_data[i]
            dir_name = df.iloc[file_index, 0].values[0]


            if current_idx <= train_stop_flag:
                copy2(src_img_path, train_folder)
                # print("{}复制到了{}".format(src_img_path, train_folder))
                with open(csv_file , 'a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow((dir_name, img_name, label, 'train'))
                train_num = train_num + 1
            elif (current_idx > train_stop_flag) and (current_idx <= val_stop_flag):
                copy2(src_img_path, val_folder)
                with open(csv_file , 'a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow((dir_name, img_name, label, 'valid'))
                # print("{}复制到了{}".format(src_img_path, val_folder))
                val_num = val_num + 1
            else:
                copy2(src_img_path, test_folder)
                # print("{}复制到了{}".format(src_img_path, test_folder))
                with open(csv_file , 'a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow((dir_name, img_name, label, 'test'))
                test_num = test_num + 1

            current_idx = current_idx + 1

        print("*********************************{}*************************************".format(class_name))
        print(
            "{}类按照{}：{}：{}的比例划分完成，一共{}张图片".format(class_name, train_scale, val_scale, test_scale, current_data_length))
        print("训练集{}：{}张".format(train_folder, train_num))
        print("验证集{}：{}张".format(val_folder, val_num))
        print("测试集{}：{}张".format(test_folder, test_num))


if __name__ == '__main__':
    src_data_folder = "E:/yarn_twist_new/448_dataset"
    target_data_folder = "E:/yarn_twist_new/newnewnew_dataset"
    data_set_split(src_data_folder, target_data_folder)
