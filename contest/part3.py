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

# for item in link:
    # print(item)


def find_circle(c):
    global flag
    global second
    global seen
    global link

    for i in link:
        if c != current and (c == i[0] or c == i[1]) and(current == i[0] or current == i[1]) and i[0] != second and i[1] != second and second != '':
            if flag:
                huiju.append(c)
                return True
            flag = True
            seen = set()
            return False
        if c == i[0] and i[1] not in seen:
            if c == current:
                second = i[1]
            tmp_seen = seen
            seen.add(c)
            if find_circle(i[1]):
                huiju.append(c)
                return True
            else:
                seen = tmp_seen
        if c == i[1] and i[0] not in seen:
            if c == current:
                second = i[0]
            tmp_seen = seen
            seen.add(c)
            if find_circle(i[0]):
                huiju.append(c)
                return True
            else:
                seen = tmp_seen
    return False

# ['滑县', '白条河', '汤阴', '黄河路东环', '黄河路西环', '中华路西环', '东风路西环', '柏庄西环', '铜冶', '姚村', '林州', '桂林', '水冶', '中华路东环', '东风路东环', '内黄', '留固', '慈周寨']

# ['水冶', '中华路东环']
# ['中华路东环', '东风路东环']
# ['东风路东环', '内黄', '留固', '慈周寨', '滑县', '白条河', '汤阴', '黄河路东环',
#  '黄河路西环', '中华路西环', '东风路西环', '柏庄西环', '铜冶', '姚村', '林州',
# '桂林', '水冶', '中华路东环']

# 100011500601775|白条河   8
# 100011500601792|水冶    10
# 100011500603402|林州
# 100011500603621|内黄    13
# 100011500605981|铜冶    9
# 100011500606026|汤阴
# 100011500631332|姚村
# 100011500632534|滑县
# 100011500708900|中华路东环
# 100011500709001|留固
# 100011500709228|桂林
# 100011500709348|东风路东环
# 100011500709585|中华路西环
# 100011500709749|东风路西环
# 100011500764960|黄河路西环
# 100011500824208|黄河路东环
# 100011500983870|柏庄西环
# 100011501001815|慈周寨
flag = True
huiju = list()
seen = set()
second = ''
current = '中华路东环'
find_circle(current)
print(huiju)

nodes = dict()
for node in reader_node:
    if node[1] in huiju:
        nodes[node[0]] = node[1]

keys = list()
for k in nodes.keys():
    keys.append(int(k))
keys.sort()
print(keys)

for k in keys:
    print(k, end='|')
    print(nodes[str(k)])

g = open('3_2.txt', 'w', encoding='gbk')


for k in keys:
    g.write(str(k))
    g.write('|')
    g.write(nodes[str(k)]+'\n')

baitiaohe = set(['井店', '南高固', '赵七级', '裴村', '南野庄', '后化村', '刘邢固', '白条河'])
shuizhi = set(['曲沟', '曲沟新镇', '曲沟一中', '寨子', '槐树屯', '洪河屯崔巍炉', '成人中专（VIP）', '曲沟三中（VIP）', '水冶东关', '水冶'])
neihuang = set(['内黄北街（VIP）', '马上', '西四牌', '新沟村', '内黄菜园', '宋村', '来宋村', '宋村小屯', '楚旺（VIP）', '楚旺东街', '楚旺王庄', '林字', '内黄'])
print(len(huiju))


