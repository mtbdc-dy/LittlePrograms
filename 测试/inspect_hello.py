# -*- coding: utf-8 -*-
# @Time : 2019/4/7,007 23:06
# @Author : 徐缘
# @FileName: inspect_hello.py
# @Software: PyCharm


import inspect
import math

"""
inspect模块用于收集python对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等等
"""

params = inspect.signature(math.isclose).parameters    # Get a signature object for the passed callable.

print(params['rel_tol'].default)

print(params['abs_tol'].default)


