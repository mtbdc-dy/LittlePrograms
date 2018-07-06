import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup
import random

# 注意有无使用代理
# soft-coding

# http://www.itcast.cn/  http://oa.sh.cmcc/wps/portal
# 综资http://10.221.154.141:20111/irm/login.html;jsessionid=8j1M8M3Z2a0icl67_oK4hIn7dPmxxck7FhaPSdWUWst0kYIy22km!-296534936
url = 'https://shouji.51240.com/212__shouji/'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    # 'Connection': 'keep-alive'
}
# header.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)')

# proxy = {
#     'http':'http://cmnet:cmnet@211.136.113.69:808'
# }

# 挂代理Handler
# proxy_support = urllib.request.ProxyHandler(proxy)
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)

# 伪装浏览器申请
request = urllib.request.Request(url, headers=header)

# 读取页面
n = 70
counter = 0
counter_time = 0
while n>0:
    n = n - 1
    print('n=',n)
    response = urllib.request.urlopen(request)
    print('code=',response.getcode())
    if response.getcode() == 200:
        counter = counter + 1
    print('counter=', counter)

    print('counter_time=', counter_time)
    tmp_time = random.randint(1,2)
    counter_time = counter_time + tmp_time
    time.sleep(tmp_time)
