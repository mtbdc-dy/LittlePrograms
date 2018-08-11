import csv
import codecs

filename = 'input_cname' + '.csv'
filename_output = 'output_cname' + '.txt'

f = open(filename, 'r')  # utf8   gb2312
reader = csv.reader(f)


g = open(filename_output, 'w')
writer = csv.writer(g)

flag = True
for row in reader:

    if flag:    # 标题行忽略
        print(row[1])
        flag = False
    else:
        tmp = [row[1]]
        print(tmp)
        writer.writerow(tmp)
