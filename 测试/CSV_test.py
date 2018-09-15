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
for item in reader:
    print(item[0])
    break
f.close()

print('1 2')
print('3 4')

