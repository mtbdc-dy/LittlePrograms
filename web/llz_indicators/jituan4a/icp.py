# -*- coding: utf-8 -*-
# @Time: 2019/8/9,009 10:41
# @Last Update: 2019/8/9,009 10:41
# @Author: 徐缘
# @FileName: icp.py
# @Software: PyCharm


import time
import xlrd
import random
import urllib.error     # 这个检查inspection 只是说这个Code在Python 2.7(你系统默认的Python环境)上不会运行
import urllib.request
import urllib.parse
import ssl
import datetime
import myPackages.getime as md
import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww
import myPackages.mailtools
import csv
import json


f = open('icp.csv', 'a', newline='')
writer = csv.writer(f)

url = "http://10.16.0.55/JSONRPC.do"
cookie = "JSESSIONID=DE8535E111512178F6554D1B2FB83FD8"
now = datetime.datetime.now()
n = int(input('你想取几天呀？'))

for i in range(n):
    delta = datetime.timedelta(days=n-i)
    date = (now - delta).strftime('%Y%m%d')
    form = {
        'params': r'[{"start":0,"fetchSize":15,"javaClass":"com.neteast.rmp.system.page.Criteria","data":{"map":{"etldate":"' + date + '","province":"200000"},"javaClass":"java.util.HashMap"}}]',
        'method': 'provinceDispatchAccuracyRateAction.getList'
    }
    f = ww.post_web_page(url, form, cookie)
    tmp_dict = json.loads(f)
    icp = tmp_dict['result']['list'][0]['icp_accuracy']
    # print(f)
    writer.writerow([date, icp])



