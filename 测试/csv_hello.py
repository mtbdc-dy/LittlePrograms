import csv

'''
    测试CSV文件读取
'''
filename = 'output.csv'
file_output = 'output.csv'
g = open(file_output, 'r', encoding='utf-8')
f = open(filename, 'r')
reader = csv.reader(g)
print(type(reader))
for item in list(reader):
    print(item[0])
    break
f.close()

print('1 2')
print('3 4')

'''
    测试CSV文件写入
'''

g = open('output/o.csv', 'w', newline='')
writer = csv.writer(g)
tmp = ['你好', '啊']
writer.writerow(tmp)


