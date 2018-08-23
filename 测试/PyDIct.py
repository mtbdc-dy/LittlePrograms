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
for item in header:
    print(type(item))
    print(header[item])

f = 2
header['a'] = header['a'] + ',e'



print(header)
print(header['a'])

header.pop('a')
header.pop('c')
header.pop('e')
a = len(header)
print(header)
print(a)