# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 10:23 AM
# @Author  : 徐缘
# @File    : sqm_api_csv.py
# @Software: PyCharm


import csv

filename = 'STB_JMMX_20190311210000_4.CSV'
filename_output = 'output_cname' + '.csv'

f = open(filename, 'r')  # utf8   gb2312
reader = csv.reader(f)

g = open(filename_output, 'w')
writer = csv.writer(g)

for row in reader:
    print(row[0].split('\x7f'))
    writer.writerow(row[0].split('\x7f'))

