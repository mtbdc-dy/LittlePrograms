import csv

f = open('ALARM.csv', 'r')  # utf8   gb2312
reader_alarm = csv.reader(f)
f = open('NODE.csv', 'r')
reader_node = csv.reader(f)

nodes = set()
for item in reader_node:
    nodes.add(item[1])  # 把网元名称加入集合

dict_1 = dict()
count_alarm = 0
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
    if item[-1] in nodes:
        count_alarm += 1
    # print(item)

# print(dict_1)
print(count_alarm)
