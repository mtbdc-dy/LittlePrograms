import sys

# 得系统默认编码
print(sys.getdefaultencoding())

a = 'asdasd a'

print(a[1: 2])

for i in a:
    if i == 's':
        print(i)


print(a.find("d"))
