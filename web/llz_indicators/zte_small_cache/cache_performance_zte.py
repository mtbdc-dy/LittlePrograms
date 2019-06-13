# -*- coding: utf-8 -*-
# @Time : 2019/3/15,015 10:50
# @Author : 徐缘
# @FileName: cache_performance_zte.py
# @Software: PyCharm


import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww
import json

import csv
import datetime

"""
    账号：llz/Ll@shmc1
"""


filename = 'output.csv'


def get_httpstatus():
    # 节点状态码
    url = 'https://39.134.88.198:8443/stat/nodestatuscode_query.action'
    form = {
        'offset': '8',
        'beginDate': begin + ' 00:00:00',
        'endDate': end + ' 00:00:00',
        'areaid': '',
        'nodeid': 'SMALLcache',
        'deviceid': '',
        'servicemode': '',
        'cachetype': '',
        'inserttypeid': '',
        'terminalid': '',
        'ratetype': '',
        'domain': '',
    }
    f = ww.post_web_page_ssl(url, form, cookie)
    tmp_dict = json.loads(f)

    "EDIT SCRIPT FROM HERE"
    tmp_dict = tmp_dict['message']
    # print(len(tmp_dict))
    # print(tmp_dict[0]['errormessage'][0]['errornum'])

    httpstatus = list()
    for i in range(5):
        httpstatus.append(0)

    for item in tmp_dict:
        if isinstance(item, dict):
            # print(item)
            for i in range(5):
                httpstatus[i] += int(item['errormessage'][i]['errornum'])

    httpstatus.append(round(httpstatus[1]/sum(httpstatus)*100, 2))
    return httpstatus


def hit_ratio():
    # 节点状态码
    url = 'https://39.134.88.198:8443/stat/requesthit_query.action'
    form = {
        'offset': '8',
        'beginDate': begin + ' 00:00:00',
        'endDate': end + ' 00:00:00',
        'areaid': '',
        'nodeid': 'SMALLcache',
        'deviceid': '',
        'apptype': '',
        'servicemode': '',
        'cachetype': '',
        'inserttypeid': '',
        'terminalid': '',
        'domaintype': '1',
        'domain': '',
    }
    f = ww.post_web_page_ssl(url, form, cookie)
    print(f)
    tmp_dict = json.loads(f)

    "EDIT SCRIPT FROM HERE"
    tmp_dict = tmp_dict['message']

    hit = 0
    miss = 0

    for item in tmp_dict:
        hit += int(item['hitsnum'])
        miss += int(item['missnum'])

    return hit, miss, round(hit/(hit+miss)*100, 2)


if __name__ == '__main__':
    # 打开输出文件，查看日期
    f = open(filename, 'r')
    reader = csv.reader(f)
    rows = [row for row in reader]
    # print(rows)
    f.close()

    # 写文件
    g = open(filename, 'a', newline='')
    writer = csv.writer(g)

    # 日期
    now = datetime.datetime.now()
    pre_update_day = datetime.datetime.strptime(rows[-1][0], '%Y-%m-%d')
    delta = now - pre_update_day - datetime.timedelta(days=1)  # 要查多少天
    if delta.days == 0:
        print("All data is up-to-date.")
        exit()
    elif delta.days < 0:
        print("Date Error")
        exit()
    print(' nmb：', delta.days)

    cookie = wl.zte_cdn_omc()
    for i in range(delta.days):
        begin = (pre_update_day + datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
        end = (pre_update_day + datetime.timedelta(days=(i+2))).strftime('%Y-%m-%d')

        csv_content = [begin]

        for item in get_httpstatus():
            csv_content.append(item)

        for item in hit_ratio():
            csv_content.append(item)

        writer.writerow(csv_content)








