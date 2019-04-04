# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 9:48 PM
# @Author  : 徐缘
# @File    : 303. 区域和检索 - 数组不可变.py
# @Software: PyCharm


class NumArray:

    def __init__(self, nums: List[int]):
        self.res = nums
        for i in range(1, len(nums)):
            self.res[i] += self.res[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.res[j]
        else:
            return self.res[j] - self.res[i-1]


nums = [0, 1, 2, 3, 4, 5]
obj = NumArray(nums)

i, j = 1, 2
param_1 = obj.sumRange(i,j)
