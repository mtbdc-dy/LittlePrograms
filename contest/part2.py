import csv

f = open('ALARM.csv', 'r')  # utf8   gb2312
reader_alarm = csv.reader(f)
f = open('NODE.csv', 'r')
reader_node = csv.reader(f)

nodes = dict()
for item in reader_node:
    nodes[item[1]] = 0  # 把网元名称作为key值加入字典

dict_1 = dict()
for item in reader_alarm:
    # item = item.rstrip()    # 括号里什么都不写，默认消除空格和换行符
    # print(item.split(','))
    # row = item.split(',')
    # if row[0] not in dict_1.keys():
    #     dict_1[item[0]] = [row[1], row[2], row[3]]
    # else:
    #     dict_1[item[0]][0] += row[1]
    #     dict_1[item[0]][1] += row[2]
    #     dict_1[item[0]][2] += row[3]
    if item[-1] in nodes.keys() and item[1] == '208-060-00-999999':
        nodes[item[-1]] += 1

m1 = 0
tmp_i = 0
for i in nodes.keys():
    if nodes[i] > m1:
        m1 = nodes[i]
        tmp_i = i

print(m1)
nodes.pop(tmp_i)
m1 = 0
tmp_i = 0
for i in nodes.keys():
    if nodes[i] > m1:
        m1 = nodes[i]
        tmp_i = i

print(m1)
nodes.pop(tmp_i)
m1 = 0
tmp_i = 0
for i in nodes.keys():
    if nodes[i] > m1:
        m1 = nodes[i]
        tmp_i = i

print(m1)
nodes.pop(tmp_i)
# s = 0
# for i in nodes.keys():
#     s += nodes[i]
# print(s)