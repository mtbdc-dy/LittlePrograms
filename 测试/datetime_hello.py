# -*- coding: utf-8 -*-
# @Time : 2019/3/5,005 10:36
# @Author : 徐缘
# @FileName: datetime_hello.py
# @Software: PyCharm


import datetime

now = datetime.datetime.now()
pre_update_day = datetime.datetime.strptime('2015-01-01', '%Y-%m-%d')
delta = now - pre_update_day
print(delta.days)
print(now)

'''通过字符串生成datetime对象'''
pre_update_day = datetime.datetime.strptime('2019-03-04', '%Y-%m-%d')       # %Y-%m-%d %H:%M:%S
print(pre_update_day)
delta = now - pre_update_day
print(delta.days)

