# -*- coding: utf-8 -*-
# @Time : 2019/4/7,007 23:06
# @Author : 徐缘
# @FileName: inspect_hello.py
# @Software: PyCharm


import inspect
import math

params = inspect.signature(math.isclose).parameters    # Get a signature object for the passed callable.

print(params['rel_tol'].default)

print(params['abs_tol'].default)


