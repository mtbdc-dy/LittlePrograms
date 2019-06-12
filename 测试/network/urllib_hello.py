# -*- coding: utf-8 -*-
# @Time : 2019/6/12,012 11:09
# @Author : 徐缘
# @FileName: urllib_hello.py
# @Software: PyCharm

"""
https://www.baidu.com/robots.txt 看看书还是很有用的啊
https://bitbucket.org/wswp/code/src/tip/chapter01/link_crawlers.py

"""
import urllib.request       # urllib2模块直接导入就可以用，在python3中urllib2被改为urllib.request
import urllib.parse         # 这个warning很烦，我又不用Python2   解析URL用的
import urllib.robotparser



class Throttle:
    """
        Add a delay between downloads to the same domain
    """
    def _init_(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urllib.parse.urlparse(url).netloc


def download(url, num_retries=2):
    print('Downloading:', url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        # 'Cookie': url[1]
    }
    request = urllib.request.Request(url, headers=header)
    try:
        html = urllib.request.urlopen(request).read()
        print(html)
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html


download('http://httpstat.us/200')


