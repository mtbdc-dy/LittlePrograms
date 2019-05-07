# -*- coding: utf-8 -*-
# @Time : 2019/5/7,007 14:47
# @Author : 徐缘
# @FileName: read_data.py
# @Software: PyCharm


import pandas as pd
import matplotlib.pyplot as plt


f = open('speed_test_count.csv')
c = pd.read_csv(f, header=None, index_col=0)

print(c.index)

plt.plot(c.index, c.values, color="red", linewidth=1)
# plt.bar(c.index, c.values, 0.01)
# plt.axis([0, 6, 0, 20])
# plt.plot(Z)
plt.xticks(c.index[::5], color='blue', rotation=60)
plt.ylabel('data rate(Mbps)')
plt.show()
