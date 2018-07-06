# 玄学
# 玄不救非，氪不改命
# 随机数，列表， 不同颜色输出

import random

print("\033[1;31m双\033[0m\033[1;34m色\033[0m球 红色球1~33选6个 蓝色球1~16选1个" + "\n")

#print("\033[4m请输入上期中奖号码：\033[0m" + "\n")

# 显示上期中奖号码
lastAnswer = [21,22,23,24,25,32]

lastBlue = 6
preTime = 0
print("上期中奖号码为：[",end='')
for i in lastAnswer:
    if preTime == 0:
        preTime += 1
    else:
        print(', ',end='')
    print(i,end='')
print('] + [',end='')


print(str(lastBlue) + ']')

#预测本期号码
difference = 1
number = 1
while difference:
    print(number)
    number += 1
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

    print(red, end='')
    print(' + ',end ='')
    print(b)

    count = 0
    for i in red:
        if int(i) == int(lastAnswer[red.index(i)]):
            count += 1

    if int(lastBlue) == int(b):
        count += 1

    print(count)
    if count >= 6:
        break
    if number >= 300000:
        break

b = random.randint(1, 16)
red = [0, 0, 0, 0, 0, 0]
flag = 0
i = 0
while i < 6:
    while flag == 0:
        flag = 1
        r = random.randint(1, 33)
        if r in red:
            flag = 0
    flag = 0
    red[i] = r
    i += 1
red.sort()

print('本期预测号码为: [', end='')
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