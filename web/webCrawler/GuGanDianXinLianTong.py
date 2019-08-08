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

# import time
#
# time_start = time.time()    # 计算程序运行时间


"""
Note!!!
超过几天，n就赋值几，默认设为0。
pyinstaller -F web\webCrawler\GuGanDianXinLianTong.py
"""
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

# 骨干电信联通入境流量 均值
row = [round(sum(list)/len(list) + sum(list_direct)/len(list_direct), 2)]
writer.writerow(row)

fo.close()

# print('part1 cost: ', time.time()-time_start)
print('run part 2')
with open('GuGanDianXinLianTong_part2.py', 'r', encoding='UTF-8') as f:
    exec(f.read())

# print('totally cost', time.time()-time_start)
