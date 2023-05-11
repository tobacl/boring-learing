import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('original.csv')

# 根据第四列的不同元素，分成三个DataFrame
df1 = df[df['col4'] == 'element1']
df2 = df[df['col4'] == 'element2']
df3 = df[df['col4'] == 'element3']

# 分别将三个DataFrame输出为CSV文件
df1.to_csv('output1.csv', index=False)
df2.to_csv('output2.csv', index=False)
df3.to_csv('output3.csv', index=False)