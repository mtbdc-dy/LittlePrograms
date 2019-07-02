# -*- coding: utf-8 -*-
# @Time : 2019-06-27 14:27
# @Author : 徐缘
# @FileName: bras_ip_transformer.py
# @Software: PyCharm


import ipaddress
import xlrd
from IPy import IP
import myPackages.ip as mi
import csv


fi = xlrd.open_workbook('现网家宽地址池.xlsx')
table = fi.sheet_by_index(0)   # 打开sheet
nrows = table.nrows     # sheet的行数
print(nrows)

filename_output = 'bras地址_hw.csv'
g = open(filename_output, 'w', newline='')
writer_hw = csv.writer(g)
filename_output = 'bras地址_zte.csv'
h = open(filename_output, 'w', newline='')
writer_zte = csv.writer(h)

# 表头
writer_zte.writerow(['bras', 'unshared_ip', 'shared_ip'])

bras_dict = dict()

# # 浏览全表
# for i in range(nrows):
#     print(table.row_values(i))
# exit()

bras = None
ip_shared = None
ip_unique = None
for i in range(nrows):
    if i < 35:
        continue

    row = table.row_values(i)
    if row[0] != '':
        print(row)
        bras = row[1]
        try:
            ip_unique = IP(row[3])
        except ValueError:
            ip_unique = IP('0.0.0.0')
        ip_shared = IP(row[6])
        if 'BNG' in bras:
            writer_zte.writerow([bras, ip_unique.strNormal(3), ip_shared.strNormal(3)])
    else:
        print(row)
        ip_shared_sec = IP(row[6])
        try:
            ip_shared = ip_shared + ip_shared_sec
            # print(ip_shared)
            writer_hw.writerow([bras, ip_shared.strNormal(2)])
            writer_zte.writerow([bras, ip_unique.strNormal(3), ip_shared.strNormal(3)])
        except ValueError:
            writer_hw.writerow([bras, ip_shared.strNormal(2), ip_shared_sec.strNormal(2)])
            # 如果首位相同，则合并
            if mi.add_one_on_ip(str(ip_shared[-1])) == str(ip_shared_sec[0]):
                writer_zte.writerow([bras, ip_unique.strNormal(3), str(ip_shared[0]) + '-' + str(ip_shared_sec[-1])])
            # 如果尾首相同，则合并
            elif str(ip_shared[0]) == mi.add_one_on_ip(str(ip_shared_sec[-1])):
                writer_zte.writerow([bras, ip_unique.strNormal(3), str(ip_shared_sec[0]) + '-' + str(ip_shared[-1])])
            # 不同则全部写上
            else:
                writer_zte.writerow([bras, ip_unique.strNormal(3), ip_shared.strNormal(3), ip_shared_sec.strNormal(3)])

