# -*- coding: utf-8 -*-
# @Time : 2019/3/5,005 10:36
# @Author : 徐缘
# @FileName: datetime_hello.py
# @Software: PyCharm


import datetime

now = datetime.datetime.now()
pre_update_day = datetime.datetime.strptime('2019-03-04', '%Y-%m-%d')
print(pre_update_day)
delta = now - pre_update_day
print(delta.days)

