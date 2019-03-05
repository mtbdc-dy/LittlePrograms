# -*- coding: utf-8 -*-
# @Time : 2019/3/5,005 9:34
# @Author : 徐缘
# @FileName: dahuizhan.py
# @Software: PyCharm


"""
大会战指标统计
从dahuizhan.xlsx上次记录至昨日。
三部分：
    1、SQM
    2、ELK
    3、普天拨测
"""

import web.webCrawler.webcrawler as ww
import urllib.request
import urllib.parse
import json
import xlrd
import xlwt
import datetime
from xlutils.copy import copy
import time
import web.webCrawler.login as wl


# Constant
filename = 'dahuizhan.xlsx'         # 文件名

companies = ['huawei', 'hy']        # 平面
query_curl = {                          # elk_search query中语句
    "2xx": {"wildcard": {"httpstatus": "2??"}},
    "3xx": {"wildcard": {"httpstatus": "3??"}},
    "4xx": {"wildcard": {"httpstatus": "4??"}},
    "all": {"match_all": {}}
}


def sqm_nei(cookie, day_sqm):
    startTime = day_sqm.strftime('%Y-%m-%d')
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnMiguData.action'
    form = {
        'paramData': '{\"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"location\"'
                     ': 4, \"dimension\": \"platform\", \"platform\": \"\", \"tType\": 2, \"isMigu\": false, \"isMiguShanxi'
                     '\": false, \"bIncludeShanxi\": false}'
    }
    f = ww.post_web_page(url, form, cookie)
    tmp_dict = json.loads(f)
    sqm_dict = json.loads(tmp_dict['resultData'])
    # print(sqm_dict.keys())
    fault = {0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 15}
    list_count = list()
    list_total = list()
    for i in fault:
        count_tmp = 0
        total_tmp = 0
        for item in sqm_dict['vod']:
            if item['FaultID'] == i:
                count_tmp += item['Count']
                total_tmp += item['Total']
        list_count.append(count_tmp)
        list_total.append(total_tmp)
    # print(list_total)
    # print(list_count)

    # 卡顿时间占比 = 卡顿时长 / 下载时长
    lag_duration = list_total[2] / 1000000
    total_duration = list_total[6]
    print('卡顿时间占比:', round(lag_duration / total_duration * 100, 2))

    # 卡顿次数占比 = 15 / 7 * 100
    lag_times = list_total[10]
    total_times = list_total[7]  # 播放节目数
    print('卡顿次数占比:', round(lag_times / total_times * 100, 2))

    # 首帧缓冲时长
    print('首帧缓冲时长(S):', round(list_total[4] / list_count[4] / 1000000, 2))  # 秒

    # 电视播放成功率
    print('电视播放成功率', round(list_total[8] / list_total[7] * 100, 2))

    # EPG加载成功率 加载成功率 和 登录成功率
    # print(sqm_dict['epg'])
    # print(sqm_dict['epgSuc'])
    print('EPG加载成功率', round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))

    # 卡顿时间占比, 首帧缓冲时长, 电视播放成功率, EPG加载成功率
    return (round(lag_duration / total_duration * 100, 2),
            round(list_total[4] / list_count[4] / 1000000, 2), round(list_total[8] / list_total[7] * 100, 2),
            round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))


def elk_query(day_elk):

    def requ_post(u, form):
        json_info = bytes(json.dumps(form), 'utf8')
        header = {
            'Content-Type': 'application/json',
            'kbn-version': '6.4.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        request = urllib.request.Request(u, headers=header, data=json_info)
        response = urllib.request.urlopen(request)
        f = response.read().decode("utf8")
        return json.loads(f)

    yesterday = day_elk.strftime('%Y.%m.%d')
    tmp_content = list()
    for cj in companies:    # 厂家
        url = 'http://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_count&method=POST'.format(cj, yesterday)
        for status in query_curl.keys():
            my_form = {
                "query": query_curl[status]
            }
            dict_tmp = requ_post(url, my_form)
            tmp_content.append(dict_tmp['count'])
    return tmp_content


if __name__ == '__main__':
    # 读excel
    oldWb = xlrd.open_workbook(filename)
    table = oldWb.sheet_by_name("Sheet1")
    n_rows = table.nrows  # number of rows
    if n_rows == 1 or n_rows == 0:
        print("Error: NO EXCEL FOUND.")
        exit()
    newWb = copy(oldWb)  # 复制
    newWs = newWb.get_sheet(0)  # 取sheet表

    # 日期
    now = datetime.datetime.now()
    pre_update_day = datetime.datetime.strptime(table.col_values(0)[-1], '%Y-%m-%d')
    delta = now - pre_update_day - datetime.timedelta(days=1)       # 要查多少天
    if delta.days == 0:
        print("All data is up-to-date.")
        exit()
    elif delta.days < 0:
        print("Date Error")
        exit()
    print('待查询的天数：', delta.days)

    # 查询准备
    cookie_sqm = wl.sqm_117()   # 登录SQM

    # 开始查询
    for i in range(delta.days):
        csv_content = list()
        day_query = pre_update_day + datetime.timedelta(days=i + 1)
        csv_content.append(day_query.strftime('%Y-%m-%d'))
        print('i:', i)
        print('Date:', csv_content[0])

        # sqm
        result = sqm_nei(cookie_sqm, day_query)
        for item in result:
            csv_content.append(item)

        # elk
        result = elk_query(day_query)
        for item in result:
            csv_content.append(item)

        for j, item in enumerate(csv_content):
            newWs.write(n_rows + i, j, item)
        print()
    newWb.save(filename)  # 保存至result路径







