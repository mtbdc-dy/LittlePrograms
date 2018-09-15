
filename = 'jump.txt'
filename_output = ''

f = open(filename, 'r')
lines = f.readlines()

# g = open(filename_output, 'w')


def jump(l, value, asd):
    if len(l) == 1:
        count = 0
        l_count.append(count + 1)
        return

    for i in range(1, int(value)+1):
        print(l[i:])
        jump(l[i:], i, len(l[i:]))
        l_count[-1] += 1
        if len(l) == asd:
            continue
        else:
            print()
            return

    return


for item in lines:
    l_num = []
    # for num in item:
    #     l_num.append(num)
    l_num = item.split(',')
    l_num[-1] = l_num[-1][0]
    print(l_num)

    l_count = []
    jump(l_num, l_num[0], len(l_num))
    m = 1000000000000000
    print(l_count)

    for a in l_count:
        if a < m:
            m = a
    print(m)




