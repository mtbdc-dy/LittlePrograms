# coding=gbk

import urllib.request
import urllib.parse
import time
import re
import csv
from bs4 import BeautifulSoup
import time
import codecs


header = {

            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'cookie': ''
        }

mac = 'f4-b8-a7-6a-60-6b'
url = 'https://mac.51240.com/' + mac + '__mac/'
print(mac)

proxy = {
    # 'http':'http://cmnet:cmnet@211.136.113.69:808'
    'http': '114.226.135.115:6666'
}

# 挂代理Handler
proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
f = response.read().decode('UTF8')
print(response.getcode())



