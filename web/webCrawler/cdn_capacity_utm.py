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


# # 一、login
# # 1. default cookie
# url = 'https://39.134.87.216:31943/itpaas/login.action'
# cj = ww.get_cookie_without_form(url)
# cookie = ''
# for item in cj:
#     cookie = cookie + item.name + '=' + item.value + ';'
# # print(cookie)
#
# # 2. get CAPTCHA
# url = 'https://39.134.87.216:31943/itpaas/verifycode?'
# ww.get_validate_code(url, cookie)
#
# # 3. post
# url = 'https://39.134.87.216:31943/itpaas/authenticate.action'
# CAPTCHA = input('CAPTCHA: ')
# form = {
#     'username': 'admin',
#     'password': 'HuaWei12#$',
#     'vcode': CAPTCHA,
#     'dstInfo': '480:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0',
#     'name': 'default',
#     'service': ''
# }
# cj = ww.get_cookie(form, url, cookie)
# cookie = ''
# for item in cj:
#     cookie = cookie + item.name + '=' + item.value + ';'
#
# # 二、query
# url = 'https://39.134.87.216:31943/pm/themes/default/pm/app/i2000_portlet_page.html?tag=pm.portlet.group_152734715982719&protalId=group_152734715982719'
# f = ww.get_web_page_ssl(url, cookie)
# print(f)

def post_ssl(url, my_form, cookie):
    ssl._create_default_https_context = ssl._create_unverified_context
    # context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'roarand': 'f602a03e-b7fa-4ae5-9f6a-9eb3aa496f85',
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


# 需要什么
url = 'https://39.134.87.216:31943/rest/pm/history'
form = {
    'param': r'{"pageIndex":1,"historyTimeRange":24,"beginTime":1545188873595,"endTime":1545188873595,"isGetGraphicGroupData":true,"isMonitorView":true,"mo2Index":"[{\"dn\":\"278657d6163e3c7e3b02fe\",\"indexId\":\"10409\",\"displayValue\":\"\",\"aggrType\":2}]"}'
}
cookie = 'CLIENTID=f813e2e3-58f0-4b0a-8dbd-0225fab62e48;' \
         'JSESSIONID=07f4e7733a18c3d5b4e2819c74591fa965da0488be5103d6;' \
         'SLB_SID=;' \
         'access_time_cookie=1545188846247;' \
         'bme_locale_session=zh_CN;' \
         'clientTimezoneId=;' \
         'locale_cookie=zh_CN;' \
         'session_cookie=cbeeb9cc-557e-4cba-b4ce-80b205832847;' \
         'sna_cookie=cbeeb9cc-557e-4cba-b4ce-80b205832847;'
print(cookie)
f = ww.post_web_page_ssl(url, form, cookie)
print(f)