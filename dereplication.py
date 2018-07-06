import csv
import codecs
import re

# 去重的同时 修改以数字为结尾的字段

filename = 'output_cname' + '.txt'
filename_output = 'output_cname_dere' + '.txt'
n = 1
list = []
with open(filename) as f:

    reader = f.readline()
    list.append(reader)
    while(reader):
        n += 1
        # print(reader)
        reader = f.readline()
        list.append(reader)

f.close()
print(n)
print(list)

list_dere = []

####
a = re.compile(r'.*\d$',re.I)
b = re.compile(r'.*:$',re.I)
c = re.compile(r'.*\.$',re.I)
flag2 = False

n = 1
for line in list:

    if line not in list_dere:
        n += 1
        # 修改
        list_dere.append(line)

# 逻辑问题，修改过后的域名又有可能会重复

print(n)
print(list_dere)
g =open(filename_output, 'w')


for line in list_dere:
    # print(line)
    g.write(line)



