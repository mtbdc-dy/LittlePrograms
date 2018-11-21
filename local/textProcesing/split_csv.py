import csv

f = open('zhanghao.csv', 'r')
reader = csv.reader(f)
lines = f.readlines()

for row in lines:
    print(row)
