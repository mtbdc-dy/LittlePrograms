
f = 1
header = {

    'a': 'b',
    'c': 'd',
    'e': f

}

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