import re
f = open('20190213 SHSW01BER', 'rb')
line = f.readlines()
for item in line:
    if b'interfaces' in item:
        print(item)
print(type(line))

exit()
Line = '123ge-11/2/9asd'
m = re.search(r'[A-Za-z]*-\d*/\d*/\d*', Line)
# \w
# 匹配包括下划线的任何单词字符。类似但不等价于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集
print(m.group(0))

