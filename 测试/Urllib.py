import urllib.request
import urllib.parse
import time
import re
import csv
from bs4 import BeautifulSoup
import time
import codecs
import random
import scrapy

header = {
            'User-Agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        }

proxy = {
    'https':'114.228.73.105:6666'
}
# https://www.baidu.com/baidu?wd=ip&tn=monline_dg&ie=utf-8 百度查ip
# http://www.xicidaili.com/nn/1 西刺代理 前七页都是验证过的
url = 'http://www.xicidaili.com/nn/1'        # url = 'https://mac.51240.com/adads__mac/'

proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)


request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
f = response.read().decode('UTF8')
print(response.getcode())
# print(f)

soup = BeautifulSoup(f,"html.parser")
# print(soup.prettify())
print("===============================")
titles = soup.find_all('td')
# HREF Hypertext Reference的缩写。意思是指定超链接目标的URL
print(titles)