import time
import random
import urllib.error
import urllib.request
import urllib.parse
import ssl
import web.webCrawler.webcrawler as ww


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
        'roarand': 'ac907011-f1c0-4c7a-b7f2-9aa1c71d1aaa',
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
'''
1、roarand
2、JSESSIONID
'''
url = 'https://39.134.87.216:31943/rest/pm/history'
form = {
    'param': r'{"pageIndex":1,"historyTimeRange":24,"beginTime":1545835431687,"endTime":1545835431687,"isGetGraphicGroupData":true,"isMonitorView":true,"mo2Index":"[{\"dn\":\"com.huawei.hvs.pop=2101531\",\"indexId\":\"11735\",\"displayValue\":\"\",\"aggrType\":2}]"}'
}
cookie = 'CLIENTID=	8a142fe2-3267-4298-bf24-97bd9c5120a0;' \
         'JSESSIONID=8f4de920ac8d727f331d18f9d3d46924fa74591b1586bd61;' \
         'SLB_SID=;' \
         'access_time_cookie=1545835411502;' \
         'bme_locale_session=zh_CN;' \
         'clientTimezoneId=;' \
         'locale_cookie=zh_CN;' \
         'session_cookie=15ba827e-3ce0-43c9-872b-990cad7e50dd;' \
         'sna_cookie=15ba827e-3ce0-43c9-872b-990cad7e50dd;'
# cookie = 'JSESSIONID=8f4de920ac8d727f331d18f9d3d46924fa74591b1586bd61'
print(form)
f = ww.post_web_page_ssl(url, form, cookie)
print(f)
