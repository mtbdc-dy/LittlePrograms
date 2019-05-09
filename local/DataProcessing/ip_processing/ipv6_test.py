# -*- coding: utf-8 -*-
# @Time : 2019/5/9,009 11:22
# @Author : 徐缘
# @FileName: ipv6_test.py
# @Software: PyCharm


from IPy import IP
import csv


print(IP('2409:8A1E:8F01::/48') + IP('2409:8A1E:8F00::/48'))
exit()


filename = 'ipv6.csv'
f = open(filename)
content = csv.reader(f)

tmp = IP('0.0.0.0')
for i, item in enumerate(content):
    if i == 0:
        tmp = IP(item[0])
        continue

    print(IP(item[0]), tmp)
    tmp = IP(item[0]) + tmp

print(tmp)
