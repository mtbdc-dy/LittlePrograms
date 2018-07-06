import csv
import codecs

# 还是csv转txt

filename = 'input_cname' + '.csv'
filename_output = 'output_cname' + '.txt'
filename_output_fixed = 'output_cname2.0' + '.txt'
f = open(filename, 'r')  # utf8   gb2312
reader = csv.reader(f)


g = open(filename_output, 'w')

list_a = []

flag = True
for row in reader:

    if flag:    #标题行忽略
        print(row[9])
        flag = False
    else:
        tmp = row[9]
        # print(tmp)
        list_a.append(tmp + '\n')
        # g.write(tmp)
        # list_a.append(tmp)
        # list_a.append('.\',\'.')

# print(list_a)

for line in list_a:
    # print(line)
    g.write(line)
g.close()

g_i = open(filename_output , 'r')

g_o = open(filename_output_fixed , 'w')

for i in g_i:
    g_o.write(i[0:-1]+'.\',\'.')


