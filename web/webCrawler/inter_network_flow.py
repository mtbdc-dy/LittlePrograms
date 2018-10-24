import datetime
import web.webCrawler.login
import web.webCrawler.webcrawler as ww
from lxml import etree

"""这个系统提交的表单数据居然有顺序要求？？？"""
# 爬取 网络全景可视化管控系统 ——业务分析
# 入境流量
# file_name = '网间流量.csv'  # 输出文件名

'''登入'''
cookie = web.webCrawler.login.login_wangluoquanjingkeshihua()

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': cookie,
}


my_form = {
    'analyseMask': '2097152',
    'analyseType': '1',
    'beginDate': '2018-10-24',
    'beginHour': '0',
    'boneDomain': '1000',
    'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
    'chartType': '2',
    'devGrpId': '161',
    'devGrpName': '骨干电信联通互联-上海出口',
    'deviceId': '0',
    'deviceName': '所有设备',
    'deviceType': '2',
    'domainId': '0',
    'endDate': '2018-10-25',
    'endHour': '0',
    'filterMask': '0',
    'isMerge': '0',
    'isPost': '1',
    'isSum': '0',
    'orderType': '65793',
    'serviceName': '所有业务',
    'showData': '65536',
    'subServiceId': '0',
    'subSvcName': '所有业务',
    'svcId': '0',
    'timeType': '2',
    'topN': '500'
}
# 获取时间
now = datetime.datetime.now()
print('Today is ', end='')
print(now)

delta_begin = datetime.timedelta(days=1)
tb = now - delta_begin
te = now
my_form['beginDate'] = tb.strftime('%Y-%m-%d')  # 调整时间格式
my_form['endDate'] = te.strftime('%Y-%m-%d')    # 调整时间格式
url = 'https://117.136.129.122/cmnet/mgrAnaIPTopNInnerIP.htm'
ww.get_web_page_ssl_ie(url, cookie)
url = 'https://117.136.129.122/cmnet/mgrAnaIPTopN.htm?analyseMask=2097152'
ww.get_web_page_ssl_ie(url, cookie)
url = 'https://117.136.129.122/cmnet/viewAnaIPTopNList.htm'
f = ww.post_web_page_ssl_ie(url, my_form, cookie)
# print(f)

url = 'https://117.136.129.122/cmnet/exportAnaIPTopNList.htm'
f = ww.get_web_page_ssl_ie(url, cookie)
print(f)
f = f[f.find('<a href="') + 10: f.find('">下载文件')]

print(f)
url = 'https://117.136.129.122/cmnet' + f
f = ww.download_web_page(url, cookie)
filename = 'inter_network_flow.xls'
g = open(filename, 'wb')
g.write(f)
g.close()


