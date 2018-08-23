import time
import csv
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import os

# OTT、IPTV 流量查询
# 1、烽火
# 2、华为
# 3、iptv
# part1 烽火
# 时间获取
te = int(time.mktime((time.localtime()[0], time.localtime()[1], time.localtime()[2], 0, 0, 0, 0, 0, 0)))
ts = te - (1533484800-1533398400)
te = str(te)
ts = str(ts)


url = 'http://39.134.89.13:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes%7Bgroup%3D%22%E5%A5%89%E8%B4%A4%E4%B8%AD%E5%BF%83%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22%5Elo%7Cbond0%7Cbond1%22%7D%5B5m%5D))%20%20*%208&start=' + ts + '&end=' + te + '&step=240'
f = webCrawler.webcrawler.get_web_page(url)
f = f[83:-5]
maximum = 0
for item in f.split("\""):
    if item <= ':':
        if float(item) > maximum:
            maximum = float(item)

# print(maximum)
print("%.2f" % (maximum/1024/1024/1024))

url = 'http://39.134.89.13:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes%7Bgroup%3D%22%E6%9D%A8%E6%B5%A6%E8%BE%B9%E7%BC%98%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22%5Elo%7Cbond0%7Cbond1%22%7D%5B5m%5D))%20%20*%208&start=' + ts + '&end=' + te + '&step=240'
f = webCrawler.webcrawler.get_web_page(url)
f = f[83:-5]
maximum = 0
for item in f.split("\""):
    if item <= ':':
        if float(item) > maximum:
            maximum = float(item)

# print(maximum)
print("%.2f" % (maximum/1024/1024/1024))


# part2 华为
# https://39.134.87.216:31943/itpaas/login.action

# part3 iptv
# 表头多了一个csrf_token 不规则了~
# JSESSIONID=542449E9565629E86261AA0D6EFE800D
cookie = webCrawler.login.zte_anyservice_uniportal()
# cookie = 'JSESSIONID=63C2852468457BBE5E14D858BBDB1E0C'
# 先去取 anti_csrf_token

url = 'https://117.135.56.61:8443/frame/frame.action'
webCrawler.webcrawler.get_web_page_ssl(url, cookie)

url = 'https://117.135.56.61:8443/iam/iampage.action'
webCrawler.webcrawler.get_web_page_ssl(url, cookie)

url = 'https://117.135.56.61:8443/iam/realtimeReport_init.action'

f = webCrawler.webcrawler.get_web_page_ssl(url, cookie)
a = f.find('sec_csrf_token')
csrf_token = f[a+18: a + 18 + 32]
# 144c9de7e22745b1b82660050c0eaa7e
# print(csrf_token)
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

