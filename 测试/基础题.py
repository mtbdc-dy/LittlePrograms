# -*- coding: UTF-8 -*-
import csv
import xlrd
import time

time_start = time.time()

filename1 = 'IOT_subscriber 20180102.log'
filename2 = 'usernumber20170830.csv'
filename3 = '附件五、物联网HLR-ID（截至2018年2月）.xlsx'
filename_output = 'HLRlogoutput20180823.csv'
flag = False
list_hlr = []
dict_un = {}
list_al = []

#  打开三个输入文件
f1 = open(filename1, 'r')
reader1 = f1.readlines()
f2 = open(filename2, 'r')
reader2 = csv.reader(f2)
f3 = xlrd.open_workbook(filename3)
table = f3.sheet_by_name("Sheet1")
nrows = table.nrows
# 打开输出文件
g = open(filename_output, 'w', newline='')
writer = csv.writer(g)

# 标准化输出文件格式
dict_output = {
    '省份': ['NSUB', 'NSUBA', 'NSUBOCSI'],
    '西藏': [0,0,0],
    '安徽': [0,0,0],
    '物联网': [0,0,0],
    '天津': [0,0,0],
    '宁夏': [0,0,0],
    '吉林': [0,0,0],
    '重庆': [0,0,0],
    '山西': [0,0,0],
    '海南': [0,0,0],
    '云南': [0,0,0],
    '国际': [0,0,0],
    '江苏': [0,0,0],
    '未匹配': [0,0,0],
    '上海': [0,0,0],
    '甘肃': [0,0,0],
    '湖南': [0,0,0],
    '陕西': [0,0,0],
    '福建': [0,0,0],
    '湖北': [0,0,0],
    '青海': [0,0,0],
    '浙江': [0,0,0],
    '内蒙古': [0,0,0],
    '辽宁': [0,0,0],
    '北京': [0,0,0],
    '山东': [0,0,0],
    '贵州': [0,0,0],
    '江西': [0,0,0],
    '黑龙江': [0,0,0],
    '新疆': [0,0,0],
    '四川': [0,0,0],
    '河北': [0,0,0],
    '广东': [0,0,0],
    '河南': [0,0,0],
    '广西': [0,0,0]
}


def binary_search(lista, key):

    # 记录数组的最高位和最低位
    min = 0
    max = len(lista) - 1
    if key in lista:
        # 建立一个死循环，直到找到key
        while True:
            # 得到中位数
            mid = int((min + max + 1) / 2)  # 向上取整
            # key在数组左边
            if lista[mid] > key:
                max = mid - 1
            # key在数组右边
            elif lista[mid] < key:
                min = mid + 1
            # key在数组中间
            elif lista[mid] == key:
                return lista[mid]


def match_user_number(u_line):
    index = binary_search(list_al, int(u_line[4:12])) or binary_search(list_al, int(u_line[4:11]))
    if index:
        u_list = u_line.split()
        dict_output[dict_un[index]][0] += int(u_list[1])
        dict_output[dict_un[index]][1] += int(u_list[2])
        dict_output[dict_un[index]][2] += int(u_list[3])
    return index


def match_hlr_id(h_line):
    index = binary_search(list_hlr, int(h_line[4:15]))
    if index:
        list_h = h_line.split()
        dict_output['物联网'][0] += int(list_h[1])
        dict_output['物联网'][1] += int(list_h[2])
        dict_output['物联网'][2] += int(list_h[3])
    return index


if __name__ == '__main__':
    # 先处理附件五、物联网HLR-ID（截至2018年2月）.xlsx
    for i in range(nrows):
        row = table.row_values(i)
        if len(row) == 5:
            if row[4][0:1] == '8':
                list_hlr.append(int(row[4][2:].replace(' ', '')))

    # 再处理 usernumber20170830.csv
    for un in reader2:
        if un[0][0:1].isdigit():
            un_digit = int(un[0])
            dict_un[un_digit] = un[1]
            list_al.append(un_digit)
    f2.close()

    # IOT_subscriber 20180102.log逐条判断
    for item in reader1:
        index_space = 0
        # 是否HLRADDR字段内
        if not flag:
            if item[0:7] == 'HLRADDR':
                flag = True
            else:
                continue
        # 是否出了HLRADDR字段
        elif len(item) <= 1:
            flag = False
            continue
        ####
        # 匹配号段
        # 一、首位为1
        # 二、物联网HLR-ID 11位
        # 三、user number 1、非物联网卡 7~8位 2、 物联网卡 9位????

        # 首位为1
        if item[4] != '1':
            continue
        index_space = item.find(' ')  # 首个空格序号
        if index_space >= 11:
            signal_matched = match_user_number(item)
        if index_space >= 15:
            match_hlr_id(item)

    time_end = time.time()
    print(dict_output)
    print(time_start, time_end)
    for keys in dict_output.keys():
        row = [keys] + dict_output[keys]
        writer.writerow(row)
