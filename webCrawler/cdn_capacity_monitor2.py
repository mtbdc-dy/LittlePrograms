import time
import csv
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import os

# cookie = webCrawler.login.zte_anyservice_uniportal()
cookie = 'JSESSIONID=63C2852468457BBE5E14D858BBDB1E0C'
# 先去取 anti_csrf_token


url = 'https://117.135.56.61:8443/frame/frame.action'
webCrawler.webcrawler.get_web_page_ssl(url, cookie)

url = 'https://117.135.56.61:8443/iam/iampage.action'
webCrawler.webcrawler.get_web_page_ssl(url, cookie)

url = 'https://117.135.56.61:8443/iam/realtimeReport_init.action'

f = webCrawler.webcrawler.get_web_page_ssl(url, cookie)
a = f.find('sec_csrf_token')
csrf_token = f[a+18: a + 18 + 32]
# 8db5afbce72a4019973dd9cf0b32296e
# 144c9de7e22745b1b82660050c0eaa7e
print(csrf_token)

# 查询时间
now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
ts = now - delta
sjc = str(int(time.time() * 1000))
startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
endTime = now.strftime('%Y-%m-%d')  # 调整时间格式

url = 'https://117.135.56.61:8443/iam/realtimeReport_list.action?t=' + sjc + '&startTime=' + startTime + '+00%3A00%3A00&endTime=' + endTime + '+13%3A44%3A36&queryType=all&queryparam=%7B%22areaids%22%3A%22%22%7D'

context = ssl._create_unverified_context()
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie': cookie,
    'Anti-CSRF-Token': csrf_token,
    # 'Referer': 'https://117.135.56.61:8443/iam/realtimeReport_init.action'
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
# 读取页面
response = urllib.request.urlopen(request, context=context)
f = response.read().decode("utf8")
time.sleep(random.randint(0, 1))

f = f[f.find('服务带宽(Gbps)'):]

f1 = f[:f.find('回源带宽')]
f1 = f1[f1.find('[')+1:f1.find(']')]
max_rate = 0
for item in f1.split(","):
    if float(item) > max_rate:
        max_rate = float(item)

print(max_rate)
f2 = f[f.find('在线用户会话数'):]
f2 = f2[f2.find('[')+1:f2.find(']')]

max_user = 0
for item in f2.split(","):
    if float(item) > max_user:
        max_user = float(item)
print(max_user/10000)
