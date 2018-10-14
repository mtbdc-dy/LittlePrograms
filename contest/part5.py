import csv

f = open('ALARM.csv', 'r')  # utf8   gb2312
reader_alarm = csv.reader(f)
f = open('NODE.csv', 'r')
reader_node = csv.reader(f)
f = open('LINK.csv', 'r')
reader_link = csv.reader(f)

link = list()   # 所有连接
nodes_in_link_csv = set()
for item in reader_link:
    link.append([item[-3], item[-1]])
    nodes_in_link_csv.add(item[-3])
    nodes_in_link_csv.add(item[-1])

# print(link)

nodes = list()
for item in reader_node:
    nodes.append([item[1],0])



for node in nodes:
    for item in link:
        if node[0] in [item[0], item[1]]:
            node[1] += 1

for node in nodes:
    if node[1] > 2:
        print(node)


# ['东风路东环', '内黄', '留固', '慈周寨', '滑县', '白条河', '汤阴', '黄河路东环',
#  '黄河路西环', '中华路西环', '东风路西环', '柏庄西环', '铜冶', '姚村', '林州',
# '桂林', '水冶', '中华路东环']