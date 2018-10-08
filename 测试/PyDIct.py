# py dict测试
a = '1231312 123123123'
a.split()
print(a)
f = 1

print(a)
header = {
    'a': 'b',
    'c': 'd',
    'e': f
}

l = [1]
r = [1]
if l == r:
    print(l)
# if 'a' iin header.keys():
#     print('OK')
for item in header:
    print(type(item))
    print(header[item])

f = 2
header['a'] = header['a'] + ',e'

print(header)
print(header['a'])
header.popitem()
header.pop('c')
a = len(header)
print(header)
print(a)
