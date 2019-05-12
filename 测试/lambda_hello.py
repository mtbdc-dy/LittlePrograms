# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 10:20 PM
# @Author  : 徐缘
# @File    : lambda_hello.py
# @Software: PyCharm


#  lambda argument_list: expression

a = range(10)
y = lambda x: a[x]
print(y(0))