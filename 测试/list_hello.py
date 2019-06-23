import math
a = [1, -2] * 10
square = lambda j: j * j
print(a)
a.sort(key=lambda x: x * x, reverse=True)
print(a)

a = ['aa', 'dc', 'c']
print(a)
print(a.sort())
exit()

a = [1]
b = [10]
print(a + b)

c = [1]
c = [2]
print(c)
exit()

lists = [x for x in range(5)]
length = len(lists)
n = 4
for i in range(n):
    one_list = lists[math.floor(i / n * length):math.floor((i + 1) / n * length)]
    print(one_list)
