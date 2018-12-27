import time
import random
import urllib.error
import urllib.request
import urllib.parse
import ssl
import web.webCrawler.webcrawler as ww


# 一、login
# 1. default cookie
url = 'https://39.134.87.216:31943/itpaas/login.action'
cj = ww.get_cookie_without_form(url)
cookie = ''
for item in cj:
    cookie = cookie + item.name + '=' + item.value + ';'

# 2. get CAPTCHA
url = 'https://39.134.87.216:31943/itpaas/verifycode?'
ww.get_validate_code(url, cookie)

# 3. post
url = 'https://39.134.87.216:31943/itpaas/authenticate.action'
CAPTCHA = input('CAPTCHA: ')
form = {
    'username': 'admin',
    'password': 'HuaWei12#$',
    'vcode': CAPTCHA,
    'dstInfo': '480:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0',
    'name': 'default',
    'service': ''
}
cj = ww.get_cookie(form, url, cookie)
cookie = ''
for item in cj:
    cookie = cookie + item.name + '=' + item.value + ';'
print(cookie)

# 4.exchange js id
url = 'https://39.134.87.216:31943/login/login.action?'
cj = ww.get_cookie_without_form_cookie(url, cookie)
cookie = ''
for item in cj:
    cookie = cookie + item.name + '=' + item.value + ';'
print(cookie)

# login.action?sevice
url = r'https://39.134.87.216:6016/sso/login.action?service=https%3A%2F%2F39.134.87.216%3A31943%2Flogin%2Flogin.action%3F&systemId=10002'
headers = ww.get_res_headers_ssl(url, cookie)
print(headers)
exit()
url = 'https://39.134.87.216:31943/login/login.action?'
cj = ww.get_cookie_without_form_cookie(url, cookie)
cookie = ''
for item in cj:
    cookie = cookie + item.name + '=' + item.value + ';'
print(cookie)

# 二、query
# 1. roarand roll a random number
url = 'https://39.134.87.216:31943/rest/framework/random'
roarand = ww.get_web_page_ssl(url, cookie)
print(roarand)


def post_ssl(url, my_form):
    ssl._create_default_https_context = ssl.create_unverified_context
    # context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'roarand': roarand,
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
    # form_data = urllib.parse.urlencode(my_form).encode('utf8')
    form_data = my_form
    # 读取页面
    response = urllib.request.urlopen(request, data=form_data)  # context=context

    f = response.read().decode("utf8")
    time.sleep(random.randint(0, 1))
    return f


# 需要什么
'''
1、roarand 关键点
2、JSESSIONID
'''
url = 'https://39.134.87.216:31943/rest/pm/history'
form = b'param=%7B%22pageIndex%22%3A1%2C%22historyTimeRange%22%3A12%2C%22beginTime%22%3A1545863398699%2C%22endTime%22%3A1545863398700%2C%22isGetGraphicGroupData%22%3Atrue%2C%22isMonitorView%22%3Atrue%2C%22mo2Index%22%3A%22%5B%7B%5C%22dn%5C%22%3A%5C%22278657d7162fcf3f4600c9%5C%22%2C%5C%22indexId%5C%22%3A%5C%2210020%5C%22%2C%5C%22displayValue%5C%22%3A%5C%22%5C%22%2C%5C%22aggrType%5C%22%3A2%7D%5D%22%7D'
f = post_ssl(url, form)
print(f)
