# -*- coding: utf-8 -*-
# @Time : 2019/3/13,013 11:16
# @Author : 徐缘
# @FileName: debugggg.py
# @Software: PyCharm
import web.webCrawler.webcrawler as ww
import urllib.request
import urllib.parse
import json
import xlrd
import xlwt
import datetime
from xlutils.copy import copy
import time

url = 'http://117.144.106.34:5601/api/console/proxy?path=%2Fhuawei_sh2019.03.07%2F_count&method=POST'

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


form = {'query': {'wildcard': {'httpstatus': '2??'}}}
print(requ_post(url, form))