# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 3:41 PM
# @Author  : 徐缘
# @File    : 32bits.py
# @Software: PyCharm


n = bin(12313123)
print(n)
n = 0b00000010100101000001111010011100
a = int(str('{0:032b}'.format(n)[::-1]), 2)     # 不足32位补0？
print(a)


