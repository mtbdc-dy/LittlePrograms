# -*- coding: utf-8 -*-
# @Time : 2019/3/15,015 10:50
# @Author : 徐缘
# @FileName: cache_performance_zte.py
# @Software: PyCharm


import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww
import json


def httpstatus():

    return


def hit_ratio():

    return


if __name__ == '__main__':
    cookie = wl.zte_cdn_omc()
    print(cookie)
    url = 'https://39.134.88.198:8443/stat/nodestatuscode_query.action'
    form = {
        'offset': '8',
        'beginDate': '2019-03-15 00:00:00',
        'endDate': '2019-03-15 16:32:02',
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
    json_tmp = json.loads(f)
    print(json_tmp)








