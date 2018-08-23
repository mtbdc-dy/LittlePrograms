# -*- coding: UTF-8 -*-
import csv

filename = '号段信息.txt'
output_filename = '省份—号段对应信息表.csv'
f = open(filename, 'r', encoding='utf-8')
reader = f.readlines()

g = open(output_filename, 'w', newline='')
writer = csv.writer(g)


def process(string):
    sublist = []
    if ',' in string:
        list_1 = string.split(',')
        for part in list_1:
            if '-' in part:
                list_2 = part.split('-')
                a = int(list_2[0])
                b = int(list_2[1])
                for n in range(a, b+1):
                    sublist.append(str(n))
            else:
                sublist.append(part)
    elif '-' in string:
        list_2 = string.split('-')
        a = int(list_2[0])
        b = int(list_2[1])
        for n in range(a, b + 1):

            sublist.append(str(n))
    else:
        sublist.append(string)
    return sublist


if __name__ == '__main__':

    list_province = []
    haoduan =[]
    output = [[] for i in range(31)]
    for i, item in enumerate(reader):

        if i == 0:
            haoduan += item.split()[2:]
        if 1 < len(item.split()[0]) < 4:
            list_province.append(item.split()[0])
            # print(len(list_province[i-1]))
    # print(haoduan)
    # print(list_province)
    # print(len(list_province))

    # for i, item in enumerate(reader):
    #     print((item.split()))
    #     print(len(item.split()))

    for i in range(0, len(list_province)):
        output[i].append(list_province[i])
        list_reader = reader[i+1].split()
        for j, item in enumerate(list_reader):
            if j == 0:
                continue
            list2 = process(item)
            print(list2)
            for l in list2:
                # print(l)

                output[i].append(haoduan[j-1][:-6]+l)

    for rows in output:
        writer.writerow(rows)

