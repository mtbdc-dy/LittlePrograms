# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 3:56 PM
# @Author  : 徐缘
# @File    : collections_hello.py
# @Software: PyCharm


import collections


a = collections.deque()
for i in range(10):
    a.append(i ** 2)
    print(a)

