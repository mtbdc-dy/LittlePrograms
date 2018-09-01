import time
import xlrd
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import myPackages.mailtools
import myPackages.getime
import csv

# 现复制CMNET出口报表，重要的事情说三遍
# 现复制CMNET出口报表，重要的事情说三遍
# 现复制CMNET出口报表，重要的事情说三遍


# OTT、IPTV 流量统计四部部分组成：
# 1、iptv
# 2、SQM
# 3、CMNET出口数据统计报表
# 4、发送邮件

file_output = 'cdn_rate.csv'
g = open(file_output, 'ab')
writer = csv.writer

# part1 烽火（不需要了）
# 时间获取
flag_fenghuo = False
if flag_fenghuo:
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


# part1 iptv
# 表头多了一个csrf_token 不规则了~
cookie = webCrawler.login.zte_anyservice_uniportal()
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


####
# part2 SQM
cookie = webCrawler.login.sqm()

form = {
    'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}'
}
# 取数据
url = 'http://106.14.197.84:65009/evqmaster/report/reportaction!returnKpiData.action'
f = webCrawler.webcrawler.post_web_page(url, form, cookie)
print(f)
tmp = f[f.find('maxStreamSTBs') + 18:]
maxStreamSTBs = f[f.find('maxStreamSTBs') + 18: f.find('maxStreamSTBs') + 18 + tmp.index('\\')]


# part3 CMNET出口数据统计报表
date = myPackages.getime.yesterday(1)
filename = 'CMNET出口数据统计报表(' + date + ').xlsx'
f = xlrd.open_workbook(filename)
table = f.sheet_by_name("CMNET出口数据统计报表")
nrows = table.nrows
ott_max_rate = 'None'
for i in range(nrows):
    row = table.row_values(i)
    if row[1] == 'OTT/IPTV（总）':
        ott_max_rate = row[4]


# part4 发送邮件
ott_max_rate = float(ott_max_rate)
max_rate = float(max_rate)
maxStreamSTBs = float(maxStreamSTBs)
max_user = float(max_user)
print(maxStreamSTBs, max_rate, max_user, ott_max_rate)
title = date + '互联网电视指标'
email_content = 'OTT峰值流用户数: {:.2f}万人; OTT峰值流速: {:.2f}Gbps; OTT利用率: {:.2f}%; IPTV峰值流用户数: {:.2f}万人; IPTV峰值流速: {:.2f}Gbps; IPTV利用率: {:.2f}%。'.format(maxStreamSTBs/10000, ott_max_rate/1024, ott_max_rate/1024/850*100, max_user/10000, max_rate, max_rate/579*100)
email_content = startTime + ': ' + email_content
print(email_content)
user = ['xuyuan2@sh.chinamobile.com', 'bianningyan@sh.chinamobile.com', 'chenlei5@sh.chinamobile.com', 'huanglinling@sh.chinamobile.com', 'lilin2@sh.chinamobile.com', 'liujinlin@sh.chinamobile.com', 'wuzhouhao@sh.chinamobile.com', 'xulingxia@sh.chinamobile.com', 'yanmin@sh.chinamobile.com', 'yuxf@sh.chinamobile.com', 'zhenj@sh.chinamobile.com', 'yanmin@sh.chinamobile.com', 'shaoweihua@sh.chinamobile.com']


if input('y or n').lower() == 'y':
    ret = myPackages.mailtools.mail139_customise(title, email_content, user)
    if ret:
        print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
    else:
        print("filed")  # 如果发送失败则会返回filed
