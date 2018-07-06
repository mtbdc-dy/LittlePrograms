import random

print("游戏加点，一共十二个属性，加其中一个会使它的花费加一并且全部属性的花费加一。初始花费为5")

listLevel = [0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0]

listCost = [5, 5, 5, 5, 5,
            5, 5, 5, 5, 5,
            5, 5]

flag = 0
sum = 0
while flag != 12:
    i = random.randint(0, 11)
    #for i in range(12):
    sum += listCost[i]
    if listLevel[i] < 10:
        listLevel[i] += 1
        if listLevel[i] == 10:
            flag += 1
        print(i, listLevel[i], listCost[i])
        listCost[i] += 1
        for k in range(12):
            listCost[k] += 1



print("sum of cost = ", sum)
print(listLevel)
print(listCost)
