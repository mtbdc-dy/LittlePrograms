# -*- coding: utf-8 -*-
# @Time : 2019/5/7,007 10:50
# @Author : 徐缘
# @FileName: speed_test_analysis.py.py
# @Software: PyCharm


import xlrd
import datetime
import pandas
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

filename = 'cesu.xlsx'
# filename = 'test.xlsx'
f = xlrd.open_workbook(filename)  # 打开excel
table = f.sheet_by_name("Sheet1")   # 打开sheet
nrows = table.nrows     # sheet的行数
print(nrows)

t = list()
d = list()


for i in range(nrows):
    if i == 0:
        continue

    tmp = [datetime.datetime.strptime(table.row_values(i)[1], '%Y-%m-%d %H:%M:%S'), table.row_values(i)[7], table.row_values(i)[8]]
    t.append(datetime.datetime.strptime(table.row_values(i)[1], '%Y-%m-%d %H:%M:%S'))
    d.append(float(table.row_values(i)[13]))
    # d.append(1)


# print(d)
a = Series(d, index=t)     # 自定义索引
# print(a)
b = a.resample("1T").sum()
c = b.resample("1d").max()
# print(b)
print(c)

plt.plot(c.index, c.values, color="red", linewidth=1)
# plt.bar(c.index, c.values, 0.01)
# plt.axis([0, 6, 0, 20])
# plt.plot(Z)
plt.ylabel('count')
plt.show()
c.to_csv('speed_test_count.csv')
