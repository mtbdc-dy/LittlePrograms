# -*- coding: utf-8 -*-
# @Time : 2019/4/15,015 13:12
# @Author : 徐缘
# @FileName: 901. Online Stock Span.py
# @Software: PyCharm


# class StockSpanner:
#
#     def __init__(self):
#         self.stock = list()  # 存储股票价格
#         self.ans = list()  # 存储Span
#
#     def next(self, price: int) -> int:
#         if len(self.stock) == 0:
#             self.stock.append(price)
#             self.ans.append(1)
#             return 1
#
#         count = 1
#         j = -1
#         for i, item in enumerate(self.stock):
#             if price >= self.stock[j]:
#                 count += self.ans[j]
#                 j += -self.ans[j]
#                 if len(self.stock) + j < 0:
#                     break
#             else:
#                 self.stock.append(price)
#                 self.ans.append(count)
#                 return count
#         self.stock.append(price)
#         self.ans.append(count)
#         return count

class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        print(self.stack)
        return weight


obj = StockSpanner()
price = [[31], [41], [48], [59], [79]]
for item in price:
    param_1 = obj.next(item[0])
    print(param_1)

