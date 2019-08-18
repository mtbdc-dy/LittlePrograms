# -*- coding: utf-8 -*-
# @Time : 2019-08-18 11:10
# @Author : 徐缘
# @FileName: pandas_intro.py
# @Software: PyCharm


"""
    发现一个问题：Pycharm删除文件后，如果新建一个文件和删除的文件同名的话，
    会导致该文件的运行位置和之前的文件相同，从而导致使用相对位置出错。
    文件更改目录后,执行路径未更新的解决方法 https://www.jb51.net/article/165811.htm
    MAC OS:快捷键 command+alt+r会弹出
"""

# 导入
import pandas as pd

# 将CSV导入pd，第0行为索引行(表头)。
reviews = pd.read_csv("../input/winemag-data-130k-v2.csv", index_col=0)
# 设置最大行数为5 (前两行+末两行+一行信息)
# pd.set_option("display.max_rows", 5)
# print(reviews.head())

# pd对象
# print(reviews)

# 两句意义相同，打印country列
# print(reviews.country)
# print(reviews['country'])

# 显示特定列，第一个元素
# print(reviews['country'][0])

# 打印第一行
# print(reviews.iloc[0])
exit()
# 打印第一列
# print(reviews.iloc[:, 0]
# 选择数据的第一和第二行、第三行
print(reviews.iloc[:3, 0])
print(reviews.iloc[[0, 1, 2], 0])

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

pd.Series([1, 2, 3, 4, 5])

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

reviews.head().to_csv("wine_reviews.csv")
reviews.to_excel('wic.xlsx', sheet_name='Total Women')

# import sqlite3
# conn = sqlite3.connect("fires.sqlite")
# fires = pd.read_sql_query("SELECT * FROM fires", conn)
# fires.head(10).to_sql("fires", conn)


