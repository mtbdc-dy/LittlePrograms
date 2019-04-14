# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 3:10 PM
# @Author  : 徐缘
# @File    : 188. Best Time to Buy and Sell Stock IV.py
# @Software: PyCharm


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        # 如果购买次数超过天数的一半，就相当于每天都可以交易
        if k > len(prices) >> 1:
            return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] > prices[i])

        # 通过交易次数来简化问题
        cash, asset = [float('-inf')] * (k + 1), [0] * (k + 1)
        print('cash:', cash)
        print('asset:', asset)
        for price in prices:  # 每天股价
            for i in range(1, k + 1):  # 每次交易
                # 前一次交易后所剩的所有资产 - 当天的股价，也就是当天买入；或者不买入，就是没钱呗
                print(i, ':', cash[i], asset[i])
                cash[i] = max(cash[i], asset[i - 1] - price)
                print(cash[i])
                # 资产等于这天的现金和这天股价的相加，也就是这天卖出；或者不卖出，也就是
                asset[i] = max(asset[i], cash[i] + price)
                print(asset[i])
        return asset[k]

a = Solution()
print(a.maxProfit(3, [2, 4, 1, 6, 7, 10, 23, 1]))

