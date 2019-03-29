# -*- coding: utf-8 -*-
# @Time : 2019/3/29,029 14:27
# @Author : 徐缘
# @FileName: sqm_lag_count_ratio.py
# @Software: PyCharm


import os
import csv

path = r'D:\ShayXU\TemporaryDir\JMMX\28'
# print(os.listdir(path))
lag_count = 0
date = '20190328020000'
lag = dict()
for file in ['1', '2', '4']:
    f = open(path + r'\STB_JMMX_' + date + '_' + file + '.CSV', 'r', encoding='utf8')
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        if i == 0:
            continue
        # print(line[0].split('\x7f')[17])
        # print(date, file, i, line[0].split('\x7f'))

        try:
            tmp_count = int(line[0].split('\x7f')[17])
            lag_count += tmp_count
            std = line[0].split('\x7f')[1]
            if std in lag.keys():
                lag[std] += tmp_count
            else:
                lag[std] = tmp_count
        except:
            print()
            # print(i)
            # print(line)
            # print(len(line), line[0].split('\x7f'))
    f.close()
print(lag_count)

# print(lag)
a = sorted(lag, key=lambda num: lag[num])


# print(lag[a[-1]])
print(len(a))
for item in a:
    print(item, lag[item])



