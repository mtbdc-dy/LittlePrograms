import re
import collections


Line = '123ge-11/2/9asd'
m = re.search(r'[A-Za-z]*-\d*/\d*/\d*', Line)
# \w
# 匹配包括下划线的任何单词字符。类似但不等价于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集
print(m.group(0))

words = re.findall(r'\w+', 'asdk;\'..12e3qw'.lower())
ban = ['a']

'''
List the n most common elements and their counts from the most
common to the least.  If n is None, then list all element counts.

>>> Counter('abcdeabcdabcaba').most_common(3)
[('a', 5), ('b', 4), ('c', 3)]

'''
res = collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
print(res)
