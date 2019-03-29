# -*- coding: utf-8 -*-
# @Time : 2019/3/29,029 14:27
# @Author : 徐缘
# @FileName: sqm_lag_count_ratio.py
# @Software: PyCharm


import os
import csv

# path = r'D:\ShayXU\TemporaryDir\JMMX\27'
path = r'D:\ShayXU\TemporaryDir\JMMX\28'
# print(os.listdir(path))

# ['20190327000000', '20190327010000', '20190327020000', '20190327030000', '20190327040000']
# ['20190328000000', '20190328010000', '20190328020000', '20190328030000', '20190328040000']
# ['20190329000000', '20190329010000', '20190329020000', '20190329030000', '20190329040000']

for date in ['20190329010000', '20190329020000', '20190329030000', '20190329040000']:
    lag_count = 0
    total = 0
    for file in ['1', '2', '4']:
        path = r'D:\ShayXU\TemporaryDir\JMMX\29'
        f = open(path + r'\STB_JMMX_' + date + '_' + file + '.CSV', 'r', encoding='utf8')
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            if i == 0:
                continue
            # print(line[0].split('\x7f')[17])
            # print(date, file, i, line[0].split('\x7f'))
            try:
                lag_count += int(line[0].split('\x7f')[17])
            except:
                print('mmm')
        f.close()

        # path = r'D:\ShayXU\TemporaryDir\ZXSB\在线设备20190327'
        path = r'D:\ShayXU\TemporaryDir\ZXSB\在线设备20190329'
        try:
            f = open(path + r'\STB_ZXSB_' + date + '_' + file + '.CSV', 'r', encoding='utf8')
            reader = csv.reader(f)
            for i, line in enumerate(reader):
                if i == 0:
                    continue
                # print(line[0].split('\x7f')[8])
                total += int(line[0].split('\x7f')[8])
        except:
            print('wrong')
    print(lag_count, total, round(lag_count/total*100, 2))


