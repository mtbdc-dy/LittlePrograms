"""
Pandas 里面定义了两种数据类型：Series 和 DataFrame
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import os


'''1、Series 就是“竖起来”的 list'''
s = Series([1, 'hello', {'key': 'world', 'hao': 'lian'}, 'zhouman'])    # 创建Series对象
s2 = Series([100, 'python', 'Soochow', 'qiwsir'], index=['mark', 'title', 'university', 'name'])     # 自定义索引
print(s, '\n', s2, sep='')
print(s.values)     # 返回数据值
print(s.index)      # 返回索引
print(type(s.values))   # <class 'numpy.ndarray'>
print(type(s.index))    # <class 'pandas.core.indexes.range.RangeIndex'>


'''2、DataFrame 接近于电子表格或者类似 mysql 数据库的形式'''
data = {"name": ["yahoo", "google", "facebook"], "marks": [200, 400, 800], "price": [9, 3, 7]}
f1 = DataFrame(data)    # 由字典转换过来
f2 = DataFrame(data, columns=['name', 'price', 'marks'])    # columns 的顺序可以被规定
f3 = DataFrame(data, columns=['name', 'price', 'marks', 'debt'], index=['a','b','c'])   # 自定义索引
newdata = {"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000}}   # 字典套字典方式定义
f4 = DataFrame(newdata)
print(f1)
print(f2)
print(f3)
print(f4)
print(f3.columns)
print(f3['name'])   # 显示某一列
f3['debt'] = 93     # 给一列赋一个值
sdebt = Series([2.2, 3.3], index=["a", "c"])     # 给一列赋值
f3['debt'] = sdebt
print(f3)

t = f3.loc[:, 'debt'].copy()    # 赋值而不是引用
t['a'] = 1
print(f3['debt'])

f3.loc['a', 'debt'] = 1
print(f3)
# exit()
# 一些建表方法
dfmi = pd.DataFrame([list('abcd'), list('efgh'), list('ijkl'), list('mnop')],
                    columns=pd.MultiIndex.from_product([['one','two'], ['first','second']]))
print(dfmi)


df1 = pd.DataFrame(np.random.random(20).reshape((10, 2)), columns=list('AB'))
print(df1.A < 0.3)
print(df1[df1.A < 0.3])     # 还有这种写法的啊??
print(df1[df1.A < 0.3].B)   # 链式操作

