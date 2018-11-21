"""二进制数整形和字符串之间转换"""
b = 0b111
a = '0b111'
c = int(a, 2)
print(c)
print(type(bin(c)))
print(bin(c))

# sort的效果
a = [1, 2, 0]
a.sort()
print(a)
