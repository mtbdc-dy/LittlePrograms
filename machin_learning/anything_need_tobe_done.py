# -*- coding: utf-8 -*-
# @Time : 2019-06-21 23:13
# @Author : 徐缘
# @FileName: anything_need_tobe_done.py
# @Software: PyCharm


import csv


with open('title.csv', 'r') as f:
    reader = csv.reader(f)
    a = [len(x[0]) for x in reader]
    print(a)
    print(sum(a)/len(a))
