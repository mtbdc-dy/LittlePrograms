# -*- coding: utf-8 -*-
# @Time : 2019/3/6,006 11:17
# @Author : 徐缘
# @FileName: dahuizhan_statistics.py
# @Software: PyCharm


"""
大会战 统计部分

流程:
    判断是否为周三：否退出
    判断月份
    从一号开始汇总，并将汇总的值写入dahuizhan.xls
"""


import urllib.request
import urllib.parse
import json
import xlrd
import xlwt
import datetime
from xlutils.copy import copy
import time


# Constant
filename = 'dahuizhan.xls'         # 文件名
parameter = [1, 2, 3, 4, 5]


def get_row_of_1st_day():
    global table
    global first_day_of_the_month
    for index in range(nrows):
        if table.row_values(index)[0] == first_day_of_the_month:  # 读第i行
            return index
    return False


if __name__ == '__main__':
    now = datetime.datetime.now()
    if now.strftime("%w") != '3':
        print("Error: 不是礼拜三")
        exit()

    first_day_of_the_month = now.strftime("%Y-%m") + "-01"
    # print(first_day_of_the_month)

    f = xlrd.open_workbook(filename, formatting_info=True)    # 打开excel
    table = f.sheet_by_name("Sheet1")   # 打开sheet
    nrows = table.nrows     # sheet的行数
    first_day_row = get_row_of_1st_day()

    result = dict()
    for j in parameter:
        result[j] = list()

    for i in range(first_day_row, nrows):
        tmp_list = table.row_values(i)
        for j in range(1, 5):
            result[j].append(float(tmp_list[j]))

        result[5].append(round((tmp_list[5]+tmp_list[6]+tmp_list[9]+tmp_list[10]) /
                               (tmp_list[8]-tmp_list[7]+tmp_list[12]-tmp_list[11]) * 100, 2))

    # print(result)
    content = list()
    content.append(now.strftime('%Y-%m-%d, %W'))
    for i in parameter:
        content.append(round(sum(result[i])/len(result[i]), 2))

    newWb = copy(f)  # 复制
    newWs = newWb.get_sheet(1)  # 取sheet1

    for j, item in enumerate(content):
        newWs.write(f.sheet_by_name("Sheet2").nrows, j, item)
    newWb.save(filename)






