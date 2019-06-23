# -*- coding: utf-8 -*-
# @Time : 2019-06-21 20:35
# @Author : 徐缘
# @FileName: file_combination.py
# @Software: PyCharm


import csv
import os
import re


files = os.listdir(r'.')
print(files)
files.sort(key=lambda i: int(re.search(r'[0-9]', i).group()))
print(files)

g = open('title_vector_34.csv', 'w')
writer = csv.writer(g)
tmp = list()
for item in files:
    with open(item, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp.append(row)

print(len(tmp))

for item in tmp:
    writer.writerow(item)

