import time
import xlrd
import random
import urllib.error
import urllib.request
import ssl
import datetime
import myPackages.getime
import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww
import myPackages.mailtools
import csv
import json


def post_ssl(url, my_form, cookie):
    ssl._create_default_https_context = ssl._create_unverified_context
    # context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'roarand': 'c2dfb2df-817d-49fd-bdfe-51da71fac94c',
        'Cookie': cookie
    }

    proxy = {
        'http': 'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请

    request = urllib.request.Request(url, headers=header)
    # 编码
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    # 读取页面
    response = urllib.request.urlopen(request, data=form_data)  # context=context

    f = response.read().decode("utf8")
    time.sleep(random.randint(0, 1))
    return f


if __name__ == '__main__':
    url = 'https://39.134.87.216:31943/rest/pm/history'
    cookie = 'JSESSIONID=d97ecdb5a6d3797f54ad2f2ec8eed0faf4402021b9f545f7'
    form = {
        'param': r'{"pageIndex":1,"historyTimeRange":0,"beginTime":1541174400000,"endTime":1541260800000,"isGetGraphicGroupData":true,"mo2Index":"[{\"dn\":\"com.huawei.hvs.pop=2101534\",\"indexId\":\"11735\",\"displayValue\":\"\",\"aggrType\":2}]","pmViewPage":"historyPm","isQueryOriginal":false}'
    }

    f = post_ssl(url, form, cookie)
    print(f)

