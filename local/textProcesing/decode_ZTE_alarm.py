# a = '\\123'
# print(a)
# print(type(a))  # '\\123'
# a = repr(a)
# print(a)
# print(type(a))

# s = '\u5220\u5221'  # \u后面跟四个十六进制数代表一个字符
# print(s)          # \x 表示后面是2位16进制  \u 则表示后面是4位16进制


# d6d0d0cb6943616368653dd6d0d0cbbbbab4e6bcd3cbd9cdf8c2e7

# x = '49:50:54:56:c9:e8:b1:b8:d6:b1:b2:a5:d4:b4:d2:ec:b3:a3:b8:e6:be:af'
x = input('Type the string you wanna decode here: ')
x = x.replace(':', '')

s = ''
count = 0
for item in x:
    if count % 2 == 0:
        s = s + r'\x'
        s = s + item
    else:
        s = s + item
    count += 1

print(s, type(s))
# print(repr(s))
exec('''s = %s''' % '\'' + s + '\'')    # 动态的创造Python代码 eval 类似python shell中打命令
# 这里这个原理我已经搞不懂了。用的是他print出来时的格式。

# a = '\\xd6\\xd0\\xd0\\xcb\\x69\\x43\\x61\\x63\\x68\\x65\\x3d\\xd6\\xd0\\xd0\\xcb\\xbb\\xba\\xb4\\xe6\\xbc\\xd3\\xcb\\xd9\\xcd\\xf8\\xc2\\xe7'
# print(s)


# s = '\xd6\xd0\xb9\xfa'
# s = input()
print(s, type(s))
S = s.encode('raw_unicode_escape').decode('gbk')    # raw 就是r'xxx'那个raw 无视一切转义
print(S, type(S))
input('Press any key to exit.')
# s = '\xd6\xd0\xb9\xfa'
# S = s.encode('unicode-escape')
# print(S, type(S))
#
# s = '\xd6\xd0\xb9\xfa'
# print(s, type(s))
# S = s.encode('unicode-escape').decode()
# print(S, type(S))

# s = input()
# print(s)

