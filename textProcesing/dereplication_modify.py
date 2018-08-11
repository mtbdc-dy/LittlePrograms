import csv
import codecs
import re

# 去重的同时 修改以数字为结尾的字段

filename = 'output_cname' + '.txt'
filename_output = 'output_cname_dere' + '.txt'

list = []
with open(filename) as f:

    reader = f.readline()
    list.append(reader)
    while(reader):
        # print(reader)
        reader = f.readline()
        list.append(reader)

f.close()

print(list)

list_dere = []

####
a = re.compile(r'.*\d$',re.I)
b = re.compile(r'.*:$',re.I)
c = re.compile(r'.*\.$',re.I)
flag2 = False

for line in list:
    if line not in list_dere:

        # 修改
        print(line[0:-1])
        matchObj = a.match(line[0:-1])
        matchObj_2 = b.match(line[0:-1])

        print(matchObj_2)

        while(matchObj or matchObj_2):
            print(1)
            flag2 = True
            line = line[0:-2] + line[-1:]

            # line = line[0:2]
            matchObj = a.match(line[0:-1])
            matchObj_2 = b.match(line[0:-1])
        if(flag2):
            matchObj_3 = c.match(line[0:-1])
            if(not matchObj_3):
                list_dere.append(line)

            flag2 = False

# 逻辑问题，修改过后的域名又有可能会重复


print(list_dere)
g =open(filename_output, 'w')


for line in list_dere:
    # print(line)
    g.write(line)



