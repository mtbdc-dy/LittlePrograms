"""
集合操作指南
"""

# 用set去重会使list排序
s = set()
s.add(3)
s.add(2)
s.add(1)
print(s)

x = set('spam')
y = {'h', 'a', 'm'}
print(x)
print(y)
print(x & y)
print(x - y)
print(x | y)

