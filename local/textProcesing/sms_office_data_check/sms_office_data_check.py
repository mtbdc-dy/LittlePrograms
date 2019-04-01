# -*- coding: utf-8 -*-
# @Time : 2019/4/1,001 14:27
# @Author : 徐缘
# @FileName: sms_office_data_check.py
# @Software: PyCharm


import xlrd
import xlwt
import os
from xlutils.copy import copy


def analyze():
    filename = '来电提醒本省本网号段表.xlsx'
    oldWb = xlrd.open_workbook(filename)
    table = oldWb.sheet_by_name("Sheet1")
    n_rows = table.nrows  # number of rows
    number_header = list()
    for i in range(n_rows):
        if i == 0:
            continue
        # print(table.row_values(i))
        number_header.append(str(int(table.row_values(i)[0])))

    print(number_header)


    # print(os.listdir('./data'))
    for file in os.listdir('./data'):
        print(file)
        oldWb = xlrd.open_workbook('data\\' + file)
        table = oldWb.sheet_by_index(0)

        newWb = copy(oldWb)  # 复制
        newWs = newWb.get_sheet(0)

        n_rows = table.nrows  # number of rows

        for i in range(n_rows):
            if i == 0:
                continue

            if table.row_values(i)[0] != '上海':
                continue
            # 检查
            tmp = str(table.row_values(i)[3])
            for item in number_header:
                if len(item) > len(tmp):
                    continue
                if tmp[0:len(item)] == item:
                    newWs.write(i, 10, '完成')
                    break
                newWs.write(i, 10, '未完成')

        newWb.save('output\\' + file)

# filename = 'data\中国移动已网内启用BOSS账号用户13X号段汇总表.xls'
# oldWb = xlrd.open_workbook(filename)
# table = oldWb.sheet_by_index(0)
# newWb = copy(oldWb)  # 复制
# newWs = newWb.get_sheet(0)
#
# n_rows = table.nrows  # number of rows
#
# for i in range(n_rows):
#     if i == 0:
#         continue
#
#     # 检查
#     tmp = str(table.row_values(i)[3])
#     for item in number_header:
#         if len(item) > len(tmp):
#             continue
#         if tmp[0:len(item)] == item:
#             newWs.write(i, 10, '完成')
#         else:
#             newWs.write(i, 10, '未完成')
# newWb.save(filename)


