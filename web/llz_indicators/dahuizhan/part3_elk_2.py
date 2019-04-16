# -*- coding: utf-8 -*-
# @Time : 2019/3/4,004 10:25
# @Author : 徐缘
# @FileName: part3_elk.py
# @Software: PyCharm


"""
查询ELk
查询当天中兴/华为/杭研平面2xx/3xx/4xx/all 总数
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


# Constant
filename = 'dahuizhan.xlsx'         # 文件名
companies = ['huawei', 'hy', 'zte', 'fonsview']        # 平面
# companies = []


# 日期相关
now = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday = now.strftime('%Y.%m.%d')
print(yesterday)


# ELK POST 请求 特殊在于kbn-version
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
    print(f)
    exit()
    return json.loads(f)


for cj in companies:
    url = 'http://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_search%3Fsize%3D0&method=POST'\
        .format(cj, yesterday)

    my_form = {
        "aggs": {
            "group_by_time": {
                "date_histogram": {
                    "field": "@timestamp",
                    "interval": "5m",
                    "format": "yyyy-MM-dd HH:mm"
                },
                "aggs": {
                    "data_rate": {
                        "sum": {
                            "field": "filesize"
                        }
                    }
                }
            }
        }
    }

    print(url, my_form)

    dict_tmp = requ_post(url, my_form)
    print(dict_tmp)




