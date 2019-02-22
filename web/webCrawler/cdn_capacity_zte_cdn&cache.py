import time
import xlrd
import random
import urllib.error
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

NODE_DICT = {
        'Cache': '1',
        'CDN': '2',
    }


def query_ottnode_zte(n, cookie):
    url = 'https://39.134.88.198:8443/stat/traffic_query.action'
    form = {
        'offset': '8',
        'beginDate': startTime + ' 00:00:00',
        'endDate': endTime + ' 00:00:00',
        'areaid': '',
        'deviceid': '',
        'apptype': '',
        'servicemode': NODE_DICT[n],
        'cachetype': '',
        'domaintype': '1',
        'domain': '',
    }

    f = ww.post_web_page_ssl(url, form, cookie)
    # print(f)
    encodedjson = json.loads(f)
    # print(encodedjson.keys())
    service_rate = list()
    for item in encodedjson['message']['linearray']:
        # print(item['servicevolume'])
        service_rate.append(item['servicevolume'])

    return round(max(service_rate) / 1024 / 1024 / 1024, 2)


g_zte = open('cdn_rate_zte_cdn.csv', 'a', newline='', encoding='gbk')
writer_zte = csv.writer(g_zte)
n_days = int(input('想取多少天数据？: '))
# print(len(NODE_DICT) * n_days, 'requests will be sent.')
cookie = wl.zte_cdn_omc()

for i in range(n_days):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=n_days-i)
    ts = now - delta
    te = now - datetime.timedelta(days=n_days-i - 1)
    # sjc = str(int(time.time() * 1000))
    startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
    endTime = te.strftime('%Y-%m-%d')  # 调整时间格式

    max_rate = list()
    for j in NODE_DICT.keys():
        max_rate_tmp = query_ottnode_zte(j, cookie)
        max_rate.append(max_rate_tmp)
    csv_content_zte = [startTime]
    csv_content_zte.extend(max_rate)
    writer_zte.writerow(csv_content_zte)
    print(i)
    print(csv_content_zte)
