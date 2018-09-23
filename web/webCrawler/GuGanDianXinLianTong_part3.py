import urllib.request
import urllib.parse
import time
import csv, codecs
from bs4 import BeautifulSoup
import random
import urllib.error
import ssl
import datetime


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
for item in reader:
    cookie = item[0]
    n = int(item[1])
    break
print(cookie)
f.close()

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': cookie,
}
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
    'beginDate': tb,
    'beginHour': '0',
    'endDate': te,
    'endHour': '0',
    'timeInterval': '-1'
}

# 伪装浏览器申请
context = ssl._create_unverified_context()

# 打开输出文件
f = open(file_name, 'a', newline='')
writer = csv.writer(f)

# 获取时间
now = datetime.datetime.now() - datetime.timedelta(days=n)

for i in range(7):
    delta_begin = datetime.timedelta(days=7 - i)
    delta_end = datetime.timedelta(days=6 - i)
    tb = now - delta_begin
    te = now - delta_end
    if tb.strftime('%Y-%m-%d') == '2018-08-21':
        continue
    my_form['beginDate'] = tb.strftime('%Y-%m-%d')  # 调整时间格式
    my_form['endDate'] = te.strftime('%Y-%m-%d')  # 调整时间格式


    form_data = urllib.parse.urlencode(my_form).encode('utf8')
    request = urllib.request.Request(url, form_data, headers=header)
    response = urllib.request.urlopen(request, context=context)

    f = response.read().decode('UTF8')

    # 欲得数据  入境通过流量为第七列数据
    #
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
    string = ''

    trs1 = soup.find('tbody')
    trs = trs1.find_all('tr')
    usr_dict.clear()
    total = 0
    for tr in trs:
        tds = tr.find_all('td')

        users = tds[1].text.strip()  # 网内用户
        for item in list_users:
            if users == item:
                usr_dict[item] = tds[8].text.strip()

    row = []
    print(usr_dict)
    for item in list_users:
        total = total + float(usr_dict[item].replace(',', ''))

    row = ["%.2f" % total] + [usr_dict['P2P流媒体']] + [usr_dict['P2P下载']]
    print(row)
    writer.writerow(row)
    time.sleep(random.randint(0, 1))

print('Good Job!!!!')



