# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 9:46 PM
# @Author  : 徐缘
# @File    : binary_hello.py
# @Software: PyCharm


a = 1
b = 4
print(a ^ b)    # 按位异或运算符
print(bin(a ^ b).count('1'))

a = 1 if 'a' > 'b' else 0
print(a)

n = bin(12313123)
print(n)
n = 0b00000010100101000001111010011100
a = int(str('{0:032b}'.format(n)[::-1]), 2)     # 不足32位补0？
print(a)