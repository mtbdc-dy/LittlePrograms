import random

print("双色球 红色球33选6 蓝色球16选1")

# print("输入上期蓝色号码")
# b = n = int(input())
# if n not in range(1,17):
#     exit(print("wrong number"))
# while n == b:
#    b = random.randint(1, 16)

b = random.randint(1, 16)

red = [0, 0, 0, 0, 0, 0]

flag = 0
i = 0
while i < 6:
    while flag == 0:
        flag = 1
        r = random.randint(1, 33)
        if r in red :
            flag = 0
    flag = 0
    red[i] = r
    i += 1
red.sort()
#print(red, end='')
#print(" + ", end='')
#print(b)
#print('This is a \033[0;31mtest\033[0m!')
#print('This is a \033[0;36mtest\033[0m!')

print('[', end='')
time1 = 0
for i in red:
    if time1 == 0:
        time1 += 1
    else:
        print(', ', end='')
    colored = '\033[1;31m' + str(i) + '\033[0m'
    print(colored, end='')
print(']', end='')

print(' + [', end='')
colorBlue = '\033[1;34m' + str(b) + '\033[0m'
print(colorBlue, end='')
print(']', end='')