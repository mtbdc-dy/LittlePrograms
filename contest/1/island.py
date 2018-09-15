global list_a
list_a = []
# 输出文件
g = open('201809100108徐缘.txt', 'w')


def find_near_point(r, c, l):
    if r+1 == len(l):
        return
    if c+1 == len(l[0]):
        return
    if l[r+1][c] == '1':
        list_a.append([r+1, c])
        find_near_point(r+1, c, l)
    if l[r][c+1] == '1':
        list_a.append([r, c+1])
        find_near_point(r, c+1, l)
    return


filename = 'islands.txt'
f = open(filename, 'r')
lines = f.readlines()

# print(lines)
count_row = 0
list_rowcount = []
for item in lines:
    if item[0:1] == '-':
        # print(count_row)
        list_rowcount.append(count_row)
        count_row = 0
        continue
    count_row += 1

print(list_rowcount)


index_row = 0
row = [],[]
darray = []
for item in lines:
    if item[0:1] == '-':
        count = 1
        index_row += 1
        # print(darray)
        # 求值
        for i in range(len(darray)):
            for j in range(len(darray[0])):
                if darray[i][j] == '1':
                    find_near_point(i, j, darray)
                    for p in list_a:
                        darray[p[0]][p[1]] = count
                    darray[i][j] = count
                    count += 1
                    # print(darray)
                    list_a = []
        sss = 0
        for bbb in darray:
            for aaa in bbb:
                # print(aaa)
                if aaa == '1' and aaa == '0':
                    c = 1
                elif int(aaa) > int(sss):
                    sss = aaa

        g.writelines(str(sss))
        g.writelines('\n')
        # g.writelines('\n')
        print(darray)
        darray = []

        continue
    row = []
    length = len(item)
    for j in range(length-1):
        row.append(item[j:j+1])
    darray.append(row)






