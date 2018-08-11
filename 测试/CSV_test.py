import csv

filename = 'output.csv'

# g = open(file_output, 'r', encoding='gb2312')
f = open(filename, 'r')
reader = csv.reader(f)
print(type(reader))
for item in reader:
    print(item[0])
    break
f.close()

print('1 2')
print('3 4')

