import math
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
