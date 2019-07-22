import urllib.request
import urllib.parse
import time
import csv, codecs
from bs4 import BeautifulSoup
import random
import urllib.error
import ssl
import datetime

import web.webCrawler.login as wl


# 网间健康度报表（晚忙时20-21点）
# 爬取网络全景可视化管控系统——业务分析
# 要过1点才能查


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
cookie = wl.login_wangluoquanjingkeshihua()
# for item in reader:
#     cookie = item[0]
#     n = int(item[1])
#     break
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
    raw_row = list()    # 生的行
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

print('Good Job!!!!')



