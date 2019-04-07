# -*- coding: utf-8 -*-
# @Time : 2019/4/7,007 22:32
# @Author : 徐缘
# @FileName: math.hello.py
# @Software: PyCharm


import math
import inspect
import math

_isclose_params = inspect.signature(math.isclose).parameters
a = 2.000000001
b = 2.0

# Determine whether two floating point numbers are close in value.
print(math.isclose(a, b))


def c(a, b, **kwarg):
    print(a)
    print(b)
    print(kwarg)
    return


c(1, 2, e=1)





