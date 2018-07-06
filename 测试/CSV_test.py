import csv

filename = 'input_olt' + '.csv'
file_output = 'output_olt' + '.csv'
encoding = 'gb2312'  # 设定文件编码，这里文件要提供给windows用户
flag = True  # 不处理第一行

g = open(file_output, 'w', encoding='gb2312')
writer = csv.writer(g)