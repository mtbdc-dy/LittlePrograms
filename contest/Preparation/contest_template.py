filename = '1' + '.txt'

f = open(filename, 'r')  # utf8   gb2312

reader = f.readlines()

dict_1 = dict()
for item in reader:
    item = item.rstrip()    # 括号里什么都不写，默认消除空格和换行符
    print(item.split(','))
    row = item.split(',')
    if row[0] not in dict_1.keys():
        dict_1[item[0]] = [row[1], row[2], row[3]]
    else:
        dict_1[item[0]][0] += row[1]
        dict_1[item[0]][1] += row[2]
        dict_1[item[0]][2] += row[3]

print(dict_1)

