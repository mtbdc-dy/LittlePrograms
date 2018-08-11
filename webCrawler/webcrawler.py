import urllib.request
import urllib.parse
import time
import http.cookiejar
import csv, codecs
from bs4 import BeautifulSoup
import random
import urllib.error
import ssl
import datetime
from PIL import Image
import socket


print('from the webcrawler.py')


def get_web_page(url, cookie=''):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': cookie
    }
    # 伪装浏览器申请
    request = urllib.request.Request(url, headers=header)
    # 读取页面
    response = urllib.request.urlopen(request)
    f = response.read().decode("utf8")
    time.sleep(random.randint(0, 1))
    return f


def get_web_page_proxy(url, cookie=''):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': cookie
    }
    proxy = {
        'http':'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请
    request = urllib.request.Request(url, headers=header)
    # 读取页面
    response = urllib.request.urlopen(request)
    f = response.read().decode("utf8")
    time.sleep(random.randint(2,3))
    return f


def get_web_page_ssl(*url):
    context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': url[1]
    }
    proxy = {
        'http':'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请
    request = urllib.request.Request(url[0], headers=header)
    # 读取页面
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode("utf8")
    time.sleep(random.randint(0, 1))
    return f


def get_img_ssl(*url):
    context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': url[1]

    }
    proxy = {
        'http': 'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请
    request = urllib.request.Request(url[0], headers=header)
    # 读取页面
    response = urllib.request.urlopen(request, context=context)

    f = response.read()
    time.sleep(random.randint(2,3))
    return f


# show validate code
def get_validate_code(*url):
    f = get_img_ssl(*url)   # 不是特别懂，but it works.
    filename = 'validateCode.jpeg'
    g = open(filename, 'wb')
    g.write(f)
    g.close()
    im = Image.open("validateCode.jpeg")
    im.show()


def get_cookie(form, *url):
    ssl._create_default_https_context = ssl._create_unverified_context
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': url[1]
    }

    post_data = urllib.parse.urlencode(form).encode('utf8')
    proxy = {
        'http': 'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请
    request = urllib.request.Request(url[0], post_data, headers=header)
    # 获取Cookie
    cj = http.cookiejar.CookieJar()
    opener_cookie = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener_cookie.open(request)
    # print(r.read().decode('utf-8'))
    print(cj)
    return cj


def get_cookie_without_form(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': 'JSESSIONID=3276F5B76C95383468C71976890DF58C'     # 还不知是不是需要一个过期的cookie
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
    # 获取Cookie
    cj = http.cookiejar.CookieJar()
    opener_cookie = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener_cookie.open(request)
    # print(r.read().decode('utf-8'))
    print(cj)
    return cj


def post_web_page(url, my_form, cookie):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
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


def post_web_page_ssl(url, my_form, cookie):
    ssl._create_default_https_context = ssl._create_unverified_context
    # context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
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


def check_proxy(ip, port):
    url = 'https://mac.51240.com/f4-b8-a7-61-60-6b__mac/'
    address = 'https://' + ip + ':' + port
    print(address)
    proxy = {
        # 'https': 'https://' + P[0] + ':' + P[1]
        # 'http': 'http://180.110.6.55:3128'
        # 'http':'125.118.247.218:6666'
        # 'https': 'https://cmnet:cmnet@211.136.113.69:808'
        # 'https': 'https://114.231.66.99:22598'
        'https': address
    }
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        # 'Referer': 'https: // mac.51240.com / f4 - b8 - a7 - 6a - 60 - 6b__mac /'
    }
    request = urllib.request.Request(url, headers=header)
    socket.setdefaulttimeout(5)
    # noinspection PyBroadException
    try:
        response = urllib.request.urlopen(request)
    except:
        print("Error Occur")
        flag = False
    else:
        print(response.getcode())
        flag = True
    time.sleep(1)
    return flag


def download_web_page(url, cookie=''):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': cookie
    }
    # 伪装浏览器申请
    request = urllib.request.Request(url, headers=header)
    # 读取页面
    response = urllib.request.urlopen(request)
    f = response.read()
    time.sleep(random.randint(0, 1))
    return f


# specialized for network_quality_monthly_report_part3
def get_excel(url, cookie, json, filename):
    # part 1 获取 report_key
    f = get_web_page(url, cookie)
    a = f.find('window.location.href =')
    report_key = f[a + 65:a + 105]
    print(report_key)

    # part 2 传输数据
    url = 'http://10.221.18.3:8080/report_data/BaseReportServlet'
    form = {
        'reportKey': report_key,
        '_gt_json': json
    }
    post_web_page(url, form, cookie)

    # part 3 下载表单
    url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=' + report_key + '&export=excel'
    f = download_web_page(url, cookie)
    g = open(filename, 'wb')
    g.write(f)
    g.close()

