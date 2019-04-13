# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 11:08 PM
# @Author  : 徐缘
# @File    : 264. Ugly Number II.py
# @Software: PyCharm


# res = set('ni hao')
import math
res = [1]
done = list()
n = 10
flag = True
while flag:
    if len(done) >= n:
        flag = False
    for item in {2, 3, 5}:
        if item * min(res) not in res:
            res.append(min(res)*item)
    done.append(min(res))
    res.remove(min(res))
    print(done)

k = 5
cash, asset = [float('-inf')] * (k+1), [0] * (k+1)
print(cash)
print(asset)
