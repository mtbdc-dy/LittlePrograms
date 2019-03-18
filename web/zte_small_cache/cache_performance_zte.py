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


filename = 'output.csv'


def get_httpstatus():

    return


def hit_ratio():

    return


if __name__ == '__main__':
    # 打开输出文件，查看日期
    # f = open(filename, 'r')
    # print(f)
    # print(f.readlines()[-1])
    # exit()

    # 写文件
    g = open(filename, 'a')
    writer = csv.writer(g)

    # 日期
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)

    begin = yesterday.strftime('%Y-%m-%d')
    end = now.strftime('%Y-%m-%d')

    cookie = wl.zte_cdn_omc()
    print(cookie)
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
    print(f)
    tmp_dict = json.loads(f)

    "EDIT SCRIPT FROM HERE"
    tmp_dict = tmp_dict['message']
    print(len(tmp_dict))
    print(tmp_dict[0]['errormessage'][0]['errornum'])

    httpstatus = list()
    for i in range(5):
        httpstatus.append(0)

    for item in tmp_dict:
        if isinstance(item, dict):
            print(item)
            for i in range(5):
                httpstatus[i] += int(item['errormessage'][i]['errornum'])

    # print(httpstatus)
    writer.write(httpstatus())







