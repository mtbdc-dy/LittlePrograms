# -*- coding: utf-8 -*-
# @Time : 2019-08-11 14:35
# @Author : 徐缘
# @FileName: sys_hello.py
# @Software: PyCharm


import sys

print(sys.path)
# sys.modules里面有已经加载了的所有模块信息

p = 0
try:
    p = sys.argv[1]
    print(type(p))
except IndexError:
    print()

print("argv:")
print(p)

if not "1":
    print("1")
