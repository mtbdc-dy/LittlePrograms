import time
import csv
import random
import ssl
import datetime
import web.webCrawler.login
import urllib.request
import urllib.parse


# 爬取 网络全景可视化管控系统 ——业务分析
# 入境流量
# file_name = '网间流量.csv'  # 输出文件名
url = 'https://117.136.129.122/cmnet/viewAnaIPTopNList.htm'
url = 'https://117.136.129.122/cmnet/mgrAnaIPTopN.htm?analyseMask=2097152'
'''登入'''
cookie = web.webCrawler.login.login_wangluoquanjingkeshihua()

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': cookie,
}

my_form = {
    'MIME 类型': ' application/x-www-form-urlencoded',
    'isPost': ' 1',
    'deviceName': ' 所有设备',
    'devGrpName': ' 骨干电信联通互联-上海出口',
    'serviceName': ' 所有业务',
    'subSvcName': ' 所有业务',
    'boneDomainIds': ' 1,2,3,4,5,6,7,8,9,10,11,12,13',
    'boneDomain': ' 1000',
    'domainId': ' 0',
    'analyseMask': ' 2097152',
    'analyseType': ' 1',
    'deviceType': ' 2',
    'devGrpId': ' 161',
    'deviceId': ' 0',
    'filterMask': ' 0',
    'svcId': ' 0',
    'subServiceId': ' 0',
    'isSum': ' 0',
    'chartType': ' 2',
    'orderType': ' 65793',
    'isMerge': ' 0',
    'showData': ' 65536',
    'topN': ' 500',
    'timeType': ' 2',
    'beginDate': ' 2018-10-23',
    'beginHour': ' 0',
    'endDate': ' 2018-10-24',
    'endHour': ' 0'
}
# 禁用ssl认证
context = ssl._create_unverified_context()
# 获取时间
now = datetime.datetime.now()
print('Today is ', end='')
print(now)

delta_begin = datetime.timedelta(days=1)
tb = now - delta_begin
te = now
my_form['beginDate'] = tb.strftime('%Y-%m-%d')  # 调整时间格式
my_form['endDate'] = te.strftime('%Y-%m-%d')    # 调整时间格式

form_data = urllib.parse.urlencode(my_form).encode('utf8')
request = urllib.request.Request(url, form_data, headers=header)
response = urllib.request.urlopen(request, context=context)
f = response.read().decode('UTF8')
print(f)


url = 'https://117.136.129.122/cmnet/download.htm?fileName=class_inip_201810241521573649.xls'