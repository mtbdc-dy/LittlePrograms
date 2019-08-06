import urllib.request
import urllib.parse
import time
import csv
from bs4 import BeautifulSoup
import random
import urllib.error
import ssl
import datetime
import os

# 爬取网络全景可视化管控系统——用户分析
# 浏览器登入后，复制其所用的jsessionid

#
tb = '2018-06-04'   # default beginDate'2018-06-04'
te = '2018-06-05'   # default endDate'2018-06-05'
usrs_dict = {}
file_name = "gugandianxinliantong.csv"
url = 'https://117.136.129.122/cmnet/viewAnaUserList.htm'
n = 0

f = open(file_name, 'r')
reader = csv.reader(f)
direct = 0
print("Reading gugandianxinblabla.csv")
for i, item in enumerate(reader):
    print(item)
    if i == 0:
        cookie = item[0]
        n = int(item[1])
    if i > 0:
        direct += float(item[1])
    if i == 7:
        break
print()

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
        "IDC-上海（骨干）-策略地址1",         # 这个好像没了
        "IDC-上海（骨干）-策略地址2",
        "Cache-上海(骨干)-小文件",
        "2/3/4G-上海（骨干）"
    ]

    soup = BeautifulSoup(f, 'html.parser')
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
fo.close()
print('run part 3')
with open('GuGanDianXinLianTong_part3.py', 'r', encoding='UTF-8') as f:
    exec(f.read())



