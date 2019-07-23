# -*- coding: utf-8 -*-
# @Time : 2019/7/23,023 13:09
# @Author : 徐缘
# @FileName: GuGanDianXinLianTong_allinone.py.py
# @Software: PyCharm


import time
import csv
import random
import ssl
import datetime
import web.webCrawler.login
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")
import time
import web.webCrawler.login as wl


"""
Note!!!
超过几天，n就赋值几，默认设为0。
pyinstaller -F web\webCrawler\GuGanDianXinLianTong_allinone.py
"""

time_start = time.time()    # 计算程序运行时间
n = int(input('超过几天就填几：'))
# 爬取 网络全景可视化管控系统 ——业务分析(历史)
# 入境流量
file_name = 'gugandianxinliantong.csv'  # 输出文件名
tb = '2018-06-04'   # default beginDate'2018-06-04'
te = '2018-06-05'   # default endDate'2018-06-05'
list = []   # 上海移动
list_direct = []    # 上海移动直连
list_outflow = []   # 出境流量
list_direct_outflow = []    # 出境流量
url = 'https://117.136.129.122/cmnet/viewAnaServiceList.htm'
cookie = web.webCrawler.login.login_wangluoquanjingkeshihua()
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': cookie,
}
my_form = {
    'isPost': '1',
    'deviceName': '所有设备',
    'devGrpName': '骨干电信联通互联全部',  # 这个是传着玩玩的，没用der!!!
    'groupName': '上海移动',
    'clusterName': '所有用户组',
    'userTypeName': '所有用户分类',
    'userName': '所有用户',
    'netName': '所有流向',
    'peerName': '所有邻居',
    'transitName': '转接',
    'provinceName': '所有省份',
    'ispName': '所有运营商',
    'countryName': '所有国家地区',
    'regionTypeName': '所有区域类型',
    'encapTypeName': '所有封装类型',
    'serviceName': '所有大类',
    'analyseItems': '0,',
    'analyseItemsName': '所有大类,',
    'queryPost': '0',
    'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
    'boneDomain': '1000',
    'domainId': '0',
    'analyseMask': '8',
    'analyseType': '2',
    'svcId': '0',
    'subServiceId': '0',
    'deviceType': '2',
    'devGrpId': '57',   # 这个才是区分设备组
    'deviceId': '0',
    'filterMask': '32',
    'filterMaskNet': '256',
    'userGroupId': '5310000',
    'userClusterId': '0',
    'userTypeId': '0',
    'isInUser': '0',
    'userId': '0',
    'netId': '0',
    'province': '0',
    'isp': '0',
    'country': '0',
    'regionType': '0',
    'encapTypeId': '-1',
    'transitIdChg': '0',
    'peerId': '0',
    'transitId': '1',
    'isSum': '0',
    'chartType': '1',
    'orderType': '65793',
    'isMerge': '0',
    'showData': '65536',
    'topN': '20',
    'timeType': '2',
    'beginDate': tb,
    'beginHour': '8',
    'endDate': te,
    'endHour': '0',
    'timeInterval': '-1'

}
# 禁用ssl认证
context = ssl._create_unverified_context()
# 获取时间
now = datetime.datetime.now()
now = now - datetime.timedelta(days=n)
print('Today is ', end='')
print(now)
# 打开输出文件
fo = open(file_name, 'w', newline='')
writer = csv.writer(fo)
# 把cookie写入输出文件
row = [cookie, n]
writer.writerow(row)
for i in range(7):
    delta_begin = datetime.timedelta(days=7-i)
    delta_end = datetime.timedelta(days=6-i)
    tb = now - delta_begin
    te = now - delta_end
    my_form['beginDate'] = tb.strftime('%Y-%m-%d')  # 调整时间格式
    my_form['endDate'] = te.strftime('%Y-%m-%d')    # 调整时间格式

    # 用户群：上海移动
    #
    my_form['groupName'] = '上海移动'
    my_form['userGroupId'] = '5310000'
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    # print(f)
    soup = BeautifulSoup(f, 'html.parser')
    links = soup.find_all('td', align='right')
    ans = links[8].get_text()
    ans = float(ans.replace(',', ''))
    print(ans)
    list.append(ans)
    list_outflow.append(float(links[9].get_text().replace(',', '')))
    time.sleep(random.randint(0, 1))

    # 用户群：上海移动直连
    #
    my_form['groupName'] = '上海移动直连'
    my_form['userGroupId'] = '5310001'
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    # print(response.getcode())
    f = response.read().decode('UTF8')
    soup = BeautifulSoup(f, 'html.parser')
    links = soup.find_all('td', align='right')
    ans = links[8].get_text()
    ans = float(ans.replace(',', ''))
    print(ans)
    list_direct.append(ans)
    list_direct_outflow.append(float(links[9].get_text().replace(',', '')))

    # 存入CSV文件
    row = [list[i]] + [list_direct[i]] + [list_outflow[i]] + [list_direct_outflow[i]]
    writer.writerow(row)
    time.sleep(random.randint(0, 1))
row = [sum(list)/len(list) + sum(list_direct)/len(list_direct)]
writer.writerow(row)
fo.close()
print('part1 cost: ', time.time()-time_start)

print('run part 2')
tb = '2018-06-04'   # default beginDate'2018-06-04'
te = '2018-06-05'   # default endDate'2018-06-05'
usrs_dict = {}
file_name = "gugandianxinliantong.csv"
url = 'https://117.136.129.122/cmnet/viewAnaUserList.htm'
n = 0

f = open(file_name, 'r')
reader = csv.reader(f)
direct = 0
for i, item in enumerate(reader):
    print(item)
    if i == 0:
        cookie = item[0]
        n = int(item[1])
    if i > 0:
        direct += float(item[1])
    if i == 7:
        break

# print(cookie)
f.close()
# cookie = webCrawler.login.login_wangluoquanjingkeshihua()
header = {
    # 'Host': '117.136.129.122',   # 10.221.154.141:20111',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    # 'Referer': 'http://10.221.154.141:20111/irm/login.html',
    'Connection': 'keep-alive',
    'Cookie': cookie,  # 需要一个没过期的
}

my_form = {
    'isPost': '1',
    'analyseMask': '128',
    'deviceName': '所有设备',
    'devGrpName': '骨干电信联通互联-上海出口',
    'userName': '所有用户',
    'netName': '所有流向',
    'provinceName': '所有省份',
    'ispName': '所有运营商',
    'countryName': '所有国家地区',
    'regionTypeName': '所有区域类型',
    'serviceName': '所有大类',
    'subSvcName': '所有业务',
    'analyseItems': '0,',
    'analyseItemsName': '所有用户,',
    'queryPost': '0',
    'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
    'boneDomain': '1000',
    'domainId': '2',
    'isInUser': '1',
    'analyseType': '1',
    'userId': '0',
    'deviceType': '2',
    'devGrpId': '161',
    'deviceId': '0',
    'filterMask': '0',
    'filterMaskNet': '256',
    'svcId': '0',
    'subServiceId': '0',
    'netId': '0',
    'province': '0',
    'isp': '0',
    'country': '0',
    'regionType': '0',
    'isSum': '0',
    'chartType': '1',
    'pktType': '1',
    'orderType': '65793',
    'isMerge': '0',
    'showData': '65536',
    'topN': '300',  # 可以调大一点以免选不到数据（没选到数据会报错）调大会增长处理时间。
    'timeType': '2',
    'beginDate': '2018-06-06',
    'beginHour': '8',
    'endDate': '2018-06-07',
    'endHour': '0',
    'timeInterval': '-1'

}

# 伪装浏览器申请
context = ssl._create_unverified_context()

# 打开输出文件
fo = open(file_name, 'a', newline='')
writer = csv.writer(fo)

# 获取时间
now = datetime.datetime.now() - datetime.timedelta(days=n)

average_idc = 0
average_fc = 0
average_gc = 0
average_2g3g4g = 0
for i in range(7):
    print(i+1, ': ')
    delta_begin = datetime.timedelta(days=7 - i)
    delta_end = datetime.timedelta(days=6 - i)
    tb = now - delta_begin
    te = now - delta_end
    my_form['beginDate'] = tb.strftime('%Y-%m-%d')  # 调整时间格式
    my_form['endDate'] = te.strftime('%Y-%m-%d')  # 调整时间格式

    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)

    f = response.read().decode('UTF8')

    # 欲得数据  入境流量为第三列数据
    #
    list_users = [
        "IDC-上海（骨干）",
        "家客-上海（骨干）",
        "集客-上海（骨干）",
        "其他-上海（骨干）",
        # "GI = 0.00",
        "上海移动骨干-深圳福江科技限速",
        "IDC-上海（骨干）-策略地址1",
        "IDC-上海（骨干）-策略地址2",
        "Cache-上海(骨干)-小文件",
        "2/3/4G-上海（骨干）"
    ]

    soup = BeautifulSoup(f, 'html.parser')
    string = ''

    trs1 = soup.find('tbody')
    trs = trs1.find_all('tr')
    usrs_dict.clear()
    for tr in trs:
        tds = tr.find_all('td')

        users = tds[1].text.strip()  # 网内用户
        if users == 'GI':
            print('\033[1;32mGI appers!! But im afraid i wont be able to notice this little poor sentence.\033[0m')
        for item in list_users:
            if users == item:
                usrs_dict[item] = float(tds[4].text.strip().replace(',', ''))
    average_idc = average_idc + usrs_dict['IDC-上海（骨干）'] + usrs_dict["IDC-上海（骨干）-策略地址1"] + usrs_dict["IDC-上海（骨干）-策略地址2"]
    average_fc = average_fc + usrs_dict['家客-上海（骨干）']
    average_gc = average_gc + usrs_dict['集客-上海（骨干）']
    average_2g3g4g = average_2g3g4g + usrs_dict['2/3/4G-上海（骨干）']
    row = []
    print(usrs_dict)
    for item in list_users:
        row = row + [usrs_dict[item]]
    writer.writerow(row)
    time.sleep(random.randint(0, 2))

row = [average_idc/7] + [average_fc/7] + [(average_gc+direct)/7] + [average_2g3g4g/7]
writer.writerow(row)

print('part 2 cost', time.time()-time_start)
print('run part 3')
tb = '2018-06-04'   # default beginDate'2018-06-04'
te = '2018-06-05'   # default endDate'2018-06-05'
cookie = 'unknown'
usr_dict = {}
file_name = "gugandianxinliantong.csv"
url = 'https://117.136.129.122/cmnet/viewAnaServiceList.htm'
n = 0
# 读取之前认证过的cookie
f = open(file_name, 'r')
reader = csv.reader(f)
for item in reader:
    cookie = item[0]
    n = int(item[1])
    break
print(cookie)
f.close()

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Connection': 'keep-alive',     # 应该不影响
    'Cookie': cookie,
}
# 伪装浏览器申请
context = ssl._create_unverified_context()
# 打开输出文件
f = open(file_name, 'a', newline='')
writer = csv.writer(f)
# 获取时间
now = datetime.datetime.now() - datetime.timedelta(days=n)

for i in range(7):
    raw_row = []    # 生的行
    delta_begin = datetime.timedelta(days=7 - i)
    delta_end = datetime.timedelta(days=6 - i)
    tb = now - delta_begin
    te = now - delta_end
    print(i, ':', tb.strftime('%Y-%m-%d'))
    if tb.strftime('%Y-%m-%d') == '2018-08-21':
        continue

    # Column H 三方出口入境总流量（Mbps）
    my_form = {
        'isPost': '1',
        'deviceName': '所有设备',
        'devGrpName': '三方出口设备组-new',
        'groupName': '所有用户群',
        'clusterName': '所有用户组',
        'userTypeName': '所有用户分类',
        'userName': '所有用户',
        'netName': '所有流向',
        'peerName': '所有邻居',
        'transitName': '转接',
        'provinceName': '所有省份',
        'ispName': '所有运营商',
        'countryName': '所有国家地区',
        'regionTypeName': '所有区域类型',
        'encapTypeName': '所有封装类型',
        'serviceName': '所有大类',
        'analyseItems': '0,',
        'analyseItemsName': '所有大类,',
        'queryPost': '0',
        'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
        'boneDomain': '1000',
        'domainId': '109',
        'analyseMask': '8',
        'analyseType': '2',
        'svcId': '0',
        'subServiceId': '0',
        'deviceType': '2',
        'devGrpId': '174',
        'deviceId': '0',
        'filterMask': '32',
        'filterMaskNet': '256',
        'userGroupId': '0',
        'userClusterId': '0',
        'userTypeId': '0',
        'isInUser': '0',
        'userId': '0',
        'netId': '0',
        'province': '0',
        'isp': '0',
        'country': '0',
        'regionType': '0',
        'encapTypeId': '-1',
        'transitIdChg': '0',
        'peerId': '0',
        'transitId': '1',
        'isSum': '0',
        'chartType': '1',
        'orderType': '65793',
        'isMerge': '0',
        'showData': '65536',
        'topN': '20',
        'timeType': '2',
        'beginDate': tb.strftime('%Y-%m-%d'),
        'beginHour': '20',
        'endDate': tb.strftime('%Y-%m-%d'),
        'endHour': '21',
        'timeInterval': '60',
        }
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    soup = BeautifulSoup(f, 'html.parser')
    tr = soup.find('tbody').find('tr').find_all('td')[2]  # table row
    raw_row.append(float(tr.text.strip().replace(',', '')))

    # Column I-M 三方出口入境
    # 欲得数据  入境通过（流控）流量为第九列数据,现在改取入境流量第五列
    my_form = {
        'isPost': '1',
        'deviceName': '所有设备',
        'devGrpName': '三方出口设备组-new',
        'groupName': '所有用户群',
        'clusterName': '所有用户组',
        'userTypeName': '所有用户分类',
        'userName': '所有用户',
        'netName': '所有流向',
        'peerName': '所有邻居',
        'transitName': '转接',
        'provinceName': '所有省份',
        'ispName': '所有运营商',
        'countryName': '所有国家地区',
        'regionTypeName': '所有区域类型',
        'encapTypeName': '所有封装类型',
        'serviceName': '所有大类',
        'analyseItems': '0,',
        'analyseItemsName': '所有大类,',
        'queryPost': '0',
        'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
        'boneDomain': '1000',
        'domainId': '109',
        'analyseMask': '8',
        'analyseType': '1',
        'svcId': '0',
        'subServiceId': '0',
        'deviceType': '2',
        'devGrpId': '174',
        'deviceId': '0',
        'filterMask': '0',
        'filterMaskNet': '256',
        'userGroupId': '0',
        'userClusterId': '0',
        'userTypeId': '0',
        'isInUser': '0',
        'userId': '0',
        'netId': '0',
        'province': '0',
        'isp': '0',
        'country': '0',
        'regionType': '0',
        'encapTypeId': '-1',
        'transitIdChg': '0',
        'peerId': '0',
        'transitId': '1',
        'isSum': '0',
        'chartType': '1',
        'orderType': '65793',
        'isMerge': '0',
        'showData': '65536',
        'topN': '20',
        'timeType': '2',
        'beginDate': tb.strftime('%Y-%m-%d'),
        'beginHour': '20',
        'endDate': tb.strftime('%Y-%m-%d'),
        'endHour': '21',
        'timeInterval': '-1',
        }
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    list_users = [
        "P2P流媒体",
        "P2P下载",
        "下载",
        "流媒体",
        "浏览",
        "即时通信",
        "网络电话",
        "电子邮件",
        "路由和网管",
        "游戏娱乐",
        "电子商务",
        "病毒和攻击",
        "其他业务",
        "Generic UDP",
        "Generic TCP"
    ]
    soup = BeautifulSoup(f, 'html.parser')
    trs1 = soup.find('tbody')
    trs = trs1.find_all('tr')
    usr_dict.clear()
    total = 0
    for tr in trs:
        tds = tr.find_all('td')
        users = tds[1].text.strip()  # 网内用户
        for item in list_users:
            if users == item:
                usr_dict[item] = float(tds[4].text.strip().replace(',', ''))
    print(usr_dict)
    for item in list_users:
        total = total + usr_dict[item]
    # ["%.2f" % total]
    raw_row = raw_row + [usr_dict['P2P下载']] + [usr_dict['P2P流媒体']] + \
        [usr_dict['流媒体']] + [usr_dict['即时通信']] + [usr_dict['下载']]

    # Column F 查询骨干电信联通出口入境总流量-上海移动
    my_form = {
        'isPost': '1',
        'deviceName': '所有设备',
        'devGrpName': '骨干电信联通互联全部',
        'groupName': '上海移动',
        'clusterName': '所有用户组',
        'userTypeName': '所有用户分类',
        'userName': '所有用户',
        'netName': '所有流向',
        'peerName': '所有邻居',
        'transitName': '转接',
        'provinceName': '所有省份',
        'ispName': '所有运营商',
        'countryName': '所有国家地区',
        'regionTypeName': '所有区域类型',
        'encapTypeName': '所有封装类型',
        'serviceName': '所有大类',
        'analyseItems': '0,',
        'analyseItemsName': '所有大类,',
        'queryPost': '0',
        'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
        'boneDomain': '1000',
        'domainId': '0',
        'analyseMask': '8',
        'analyseType': '2',
        'svcId': '0',
        'subServiceId': '0',
        'deviceType': '2',
        'devGrpId': '57',
        'deviceId': '0',
        'filterMask': '32',
        'filterMaskNet': '256',
        'userGroupId': '5310000',
        'userClusterId': '0',
        'userTypeId': '0',
        'isInUser': '0',
        'userId': '0',
        'netId': '0',
        'province': '0',
        'isp': '0',
        'country': '0',
        'regionType': '0',
        'encapTypeId': '-1',
        'transitIdChg': '0',
        'peerId': '0',
        'transitId': '1',
        'isSum': '0',
        'chartType': '1',
        'orderType': '65793',
        'isMerge': '0',
        'showData': '65536',
        'topN': '20',
        'timeType': '2',
        'beginDate': tb.strftime('%Y-%m-%d'),
        'beginHour': '20',
        'endDate': tb.strftime('%Y-%m-%d'),
        'endHour': '21',
        'timeInterval': '60',
    }
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    soup = BeautifulSoup(f, 'html.parser')
    tr = soup.find('tbody').find('tr').find_all('td')[2]  # table row
    raw_row.append(float(tr.text.strip().replace(',', '')))

    # Column N-R 骨干电信联通出口-上海移动
    # 欲得数据  入境通过（流控）流量为第九列数据,现在改取入境流量第五列
    my_form = {
        'isPost': '1',
        'deviceName': '所有设备',
        'devGrpName': '骨干电信联通互联全部',
        'groupName': '上海移动',
        'clusterName': '所有用户组',
        'userTypeName': '所有用户分类',
        'userName': '所有用户',
        'netName': '所有流向',
        'peerName': '所有邻居',
        'transitName': '转接',
        'provinceName': '所有省份',
        'ispName': '所有运营商',
        'countryName': '所有国家地区',
        'regionTypeName': '所有区域类型',
        'encapTypeName': '所有封装类型',
        'serviceName': '所有大类',
        'analyseItems': '0,',
        'analyseItemsName': '所有大类,',
        'queryPost': '0',
        'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
        'boneDomain': '1000',
        'domainId': '0',
        'analyseMask': '8',
        'analyseType': '1',
        'svcId': '0',
        'subServiceId': '0',
        'deviceType': '2',
        'devGrpId': '57',
        'deviceId': '0',
        'filterMask': '32',
        'filterMaskNet': '256',
        'userGroupId': '5310000',
        'userClusterId': '0',
        'userTypeId': '0',
        'isInUser': '0',
        'userId': '0',
        'netId': '0',
        'province': '0',
        'isp': '0',
        'country': '0',
        'regionType': '0',
        'encapTypeId': '-1',
        'transitIdChg': '0',
        'peerId': '0',
        'transitId': '1',
        'isSum': '0',
        'chartType': '1',
        'orderType': '65793',
        'isMerge': '0',
        'showData': '65536',
        'topN': '20',
        'timeType': '2',
        'beginDate': tb.strftime('%Y-%m-%d'),
        'beginHour': '20',
        'endDate': tb.strftime('%Y-%m-%d'),
        'endHour': '21',
        'timeInterval': '-1',
        }
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    list_users = [
        "P2P流媒体",
        "P2P下载",
        "下载",
        "流媒体",
        "浏览",
        "即时通信",
        "网络电话",
        "电子邮件",
        "路由和网管",
        "游戏娱乐",
        "电子商务",
        "病毒和攻击",
        "其他业务",
        "Generic UDP",
        "Generic TCP"
    ]
    soup = BeautifulSoup(f, 'html.parser')
    trs1 = soup.find('tbody')
    trs = trs1.find_all('tr')
    usr_dict.clear()
    total = 0
    for tr in trs:
        tds = tr.find_all('td')
        users = tds[1].text.strip()  # 网内用户
        for item in list_users:
            if users == item:
                usr_dict[item] = float(tds[4].text.strip().replace(',', ''))
    print(usr_dict)
    for item in list_users:
        total = total + usr_dict[item]
    # ["%.2f" % total]
    raw_row = raw_row + [usr_dict['P2P下载']] + [usr_dict['P2P流媒体']] + \
        [usr_dict['流媒体']] + [usr_dict['即时通信']] + [usr_dict['下载']]

    # Column R 骨干电信联通出口入境总流量-上海移动直连
    my_form = {
        'isPost': '1',
        'deviceName': '所有设备',
        'devGrpName': '骨干电信联通互联全部',
        'groupName': '上海移动直连',
        'clusterName': '所有用户组',
        'userTypeName': '所有用户分类',
        'userName': '所有用户',
        'netName': '所有流向',
        'peerName': '所有邻居',
        'transitName': '转接',
        'provinceName': '所有省份',
        'ispName': '所有运营商',
        'countryName': '所有国家地区',
        'regionTypeName': '所有区域类型',
        'encapTypeName': '所有封装类型',
        'serviceName': '所有大类',
        'analyseItems': '0,',
        'analyseItemsName': '所有大类,',
        'queryPost': '0',
        'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
        'boneDomain': '1000',
        'domainId': '0',
        'analyseMask': '8',
        'analyseType': '2',
        'svcId': '0',
        'subServiceId': '0',
        'deviceType': '2',
        'devGrpId': '57',
        'deviceId': '0',
        'filterMask': '32',
        'filterMaskNet': '256',
        'userGroupId': '5310001',
        'userClusterId': '0',
        'userTypeId': '0',
        'isInUser': '0',
        'userId': '0',
        'netId': '0',
        'province': '0',
        'isp': '0',
        'country': '0',
        'regionType': '0',
        'encapTypeId': '-1',
        'transitIdChg': '0',
        'peerId': '0',
        'transitId': '1',
        'isSum': '0',
        'chartType': '1',
        'orderType': '65793',
        'isMerge': '0',
        'showData': '65536',
        'topN': '20',
        'timeType': '2',
        'beginDate': tb.strftime('%Y-%m-%d'),
        'beginHour': '20',
        'endDate': tb.strftime('%Y-%m-%d'),
        'endHour': '21',
        'timeInterval': '60',
    }
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    soup = BeautifulSoup(f, 'html.parser')
    tr = soup.find('tbody').find('tr').find_all('td')[2]  # table row
    raw_row.append(float(tr.text.strip().replace(',', '')))

    # Column S-W 骨干电信联通出口-上海移动直连
    # 欲得数据  入境通过（流控）流量为第九列数据,现在改取入境流量第五列
    my_form = {
        'isPost': '1',
        'deviceName': '所有设备',
        'devGrpName': '骨干电信联通互联全部',
        'groupName': '上海移动直连',
        'clusterName': '所有用户组',
        'userTypeName': '所有用户分类',
        'userName': '所有用户',
        'netName': '所有流向',
        'peerName': '所有邻居',
        'transitName': '转接',
        'provinceName': '所有省份',
        'ispName': '所有运营商',
        'countryName': '所有国家地区',
        'regionTypeName': '所有区域类型',
        'encapTypeName': '所有封装类型',
        'serviceName': '所有大类',
        'analyseItems': '0,',
        'analyseItemsName': '所有大类,',
        'queryPost': '0',
        'boneDomainIds': '1,2,3,4,5,6,7,8,9,10,11,12,13',
        'boneDomain': '1000',
        'domainId': '0',
        'analyseMask': '8',
        'analyseType': '1',
        'svcId': '0',
        'subServiceId': '0',
        'deviceType': '2',
        'devGrpId': '57',
        'deviceId': '0',
        'filterMask': '32',
        'filterMaskNet': '256',
        'userGroupId': '5310001',
        'userClusterId': '0',
        'userTypeId': '0',
        'isInUser': '0',
        'userId': '0',
        'netId': '0',
        'province': '0',
        'isp': '0',
        'country': '0',
        'regionType': '0',
        'encapTypeId': '-1',
        'transitIdChg': '0',
        'peerId': '0',
        'transitId': '1',
        'isSum': '0',
        'chartType': '1',
        'orderType': '65793',
        'isMerge': '0',
        'showData': '65536',
        'topN': '20',
        'timeType': '2',
        'beginDate': tb.strftime('%Y-%m-%d'),
        'beginHour': '20',
        'endDate': tb.strftime('%Y-%m-%d'),
        'endHour': '21',
        'timeInterval': '-1',
        }
    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode('UTF8')
    list_users = [
        "P2P流媒体",
        "P2P下载",
        "下载",
        "流媒体",
        "浏览",
        "即时通信",
        "网络电话",
        "电子邮件",
        "路由和网管",
        "游戏娱乐",
        "电子商务",
        "病毒和攻击",
        "其他业务",
        "Generic UDP",
        "Generic TCP"
    ]
    soup = BeautifulSoup(f, 'html.parser')
    trs1 = soup.find('tbody')
    trs = trs1.find_all('tr')
    usr_dict.clear()
    total = 0
    for tr in trs:
        tds = tr.find_all('td')
        users = tds[1].text.strip()  # 网内用户
        for item in list_users:
            if users == item:
                usr_dict[item] = tds[4].text.strip()
    print(usr_dict)
    for item in list_users:
        total = total + float(usr_dict[item].replace(',', ''))
    # ["%.2f" % total]
    raw_row = raw_row + [usr_dict['P2P下载']] + [usr_dict['P2P流媒体']] + \
        [usr_dict['流媒体']] + [usr_dict['即时通信']] + [usr_dict['下载']]
    print(raw_row)
    writer.writerow(raw_row)
    time.sleep(random.randint(0, 1))

print('totally cost', time.time()-time_start)
