import csv

# 打开原始CSV文件并创建三个输出文件
with open('E:/yarn_twist_new/csv/final_csv.csv', 'r', newline='') as infile, \
     open('E:/yarn_twist_new/csv/train_csv.csv', 'w', newline='') as outfile1, \
     open('E:/yarn_twist_new/csv/valid_csv.csv', 'w', newline='') as outfile2, \
     open('E:/yarn_twist_new/csv/test_csv.csv', 'w', newline='') as outfile3:

    # 创建CSV读写器和写入器
    reader = csv.reader(infile)
    writer1 = csv.writer(outfile1)
    writer2 = csv.writer(outfile2)
    writer3 = csv.writer(outfile3)

    # 写入CSV文件的表头
    header = next(reader)      #"pathname		"	filename	label	dirname
    writer1.writerow(header)
    writer2.writerow(header)
    writer3.writerow(header)

    # 遍历CSV文件的每一行
    for row in reader:
        # if row[0]!= 8:
        # else:none
        # 根据第四列的不同元素，写入不同的输出文件
        if row[3] == 'train':
            writer1.writerow(row)
        elif row[3] == 'valid':
            writer2.writerow(row)
        elif row[3] == 'test':
            writer3.writerow(row)