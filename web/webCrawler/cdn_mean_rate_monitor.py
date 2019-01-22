import time
import xlrd
import random
import urllib.error
import urllib.request
import urllib.parse
import ssl
import datetime
import myPackages.getime as md
import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww
import myPackages.mailtools
import csv
import json


"""
取各个平面
"""

# 查询多长时间
ndays = 7
# 从几天前开始查询
days_before = 8
'''Constants'''
# 输出文件名
file_output = 'cdn_mean_rate.csv'
# IPTV
IPTV_total_capacity = 1521
print('中兴总容量： \033[32;0m{:d}\033[0mG'.format(IPTV_total_capacity))
# OTT
FX_FengHuo_OTT = 240
YP_FengHuo_OTT = 90
FengHuo_Total = YP_FengHuo_OTT + FX_FengHuo_OTT
PD_HuaWei_OTT = 222
OTT_total_capacity = FX_FengHuo_OTT + YP_FengHuo_OTT + PD_HuaWei_OTT
print('OTT总容量： \033[32;0m{:d}\033[0mG'.format(OTT_total_capacity))
# 打开输出文件
g = open(file_output, 'a', newline='')
writer = csv.writer(g)


# 查询时间
now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
ts = now - delta
sjc = str(int(time.time() * 1000))
startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
endTime = now.strftime('%Y-%m-%d')  # 调整时间格式


'''Queries'''


# 时间戳格式转换
def timestamp_to_date(time_stamp, format_string="%H:%M"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


# p1 华为
def huawei():

    cookie = wl.utm()
    # cookie = 'JSESSIONID=608d6bf3654d0e1a2406d2c1099270078e295634e76211a7'
    url = 'https://39.134.87.216:31943/rest/framework/random?_=1546344328109'

    roarand = ww.get_web_page_ssl(url, cookie)

    def post_ssl(url, my_form):
        # ssl._create_default_https_context = ssl.create_unverified_context
        context = ssl._create_unverified_context()
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'roarand': roarand,
            'Cookie': cookie
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
        # 编码
        # form_data = urllib.parse.urlencode(my_form).encode('utf8')
        form_data = my_form
        # 读取页面
        response = urllib.request.urlopen(request, data=form_data, context=context)  # context=context

        f = response.read().decode("utf8")
        time.sleep(random.randint(0, 1))
        return f

    HW_ott_mean_rate = list()
    for i in range(ndays):
        time_end = str(int(md.get_today_zero_stamp()) - ((days_before - 1 - i) * 24 * 3600))
        time_start = str(int(time_end) - 24 * 3600)
        # print(time_start, time_end)

        url = 'https://39.134.87.216:31943/rest/pm/history'
        form = b'param=%7B%22pageIndex%22%3A1%2C%22historyTimeRange%22%3A0%2C%22beginTime%22%3A' +\
               bytes(str(time_start), encoding='utf-8') + b'000%2C%22endTime%22%3A' +\
               bytes(str(time_end), encoding='utf-8') +\
               b'000%2C%22isGetGraphicGroupData%22%3Atrue%2C%22isMonitorView%22%3Atrue%2C%22mo2Index%22%3A%22%5B%7B%5C%22' \
               b'dn%5C%22%3A%5C%22com.huawei.hvs.pop%3D2101531%5C%22%2C%5C%22indexId%5C%22%3A%5C%2211735%5C%22%2C%5C%22di' \
               b'splayValue%5C%22%3A%5C%22%5C%22%2C%5C%22aggrType%5C%22%3A2%7D%5D%22%7D'
        f = post_ssl(url, form)
        # print(f)
        huawei_dict = json.loads(f)
        huawei_list = huawei_dict['result']['groupQueryData'][0][0]['indexValues']
        HW_ott_rate = []
        for item in huawei_list:
            HW_ott_rate.append(float(item['indexValue']))
        # print(HW_ott_rate)
        HW_ott_mean_rate.append(sum(HW_ott_rate)/len(HW_ott_rate))

    return HW_ott_mean_rate


print('华为：')
huawei_ott = huawei()
print(huawei_ott)
print(sum(huawei_ott)/len(huawei_ott))

# p2 烽火
print('烽火：')
fenghuo_ott = wl.fonsview_mean(ndays, days_before)
print(fenghuo_ott)
exit()
'''part3 zte'''
print('中兴：')
cookie = wl.zte_anyservice_uniportal_v2()
url = 'https://117.135.56.61:8443/dashboard_queryChartData.action'
form = {}   # 仅仅是应为我写的方法，需要填form。也表明这个页面的请求方法有问题。
f = ww.post_web_page_ssl(url, form, cookie)
# print(f)
zte_dict = json.loads(f)
# print(zte_dict)
online_user = list()
bandwidth = list()
for item in zte_dict:
    bandwidth.append(item['bandwidth'])
    online_user.append(item['onlineuser'])
max_rate_tmp = max(bandwidth)
max_rate = max(bandwidth)/1024/1024/1024
print(max_rate)
max_user = max(online_user)
iptv_time_tmp = ''
for item in zte_dict:
    if item['bandwidth'] == max_rate_tmp:
        iptv_time_tmp = item['stattime']
h = iptv_time_tmp[0:2]
m = iptv_time_tmp[-2:]
# print(h, m)
t = (2018, 12, 31, int(h), int(m), 0, 0, 0, 0)
timestamp_iptv = time.mktime(t)
iptv_peak_period = timestamp_to_date(timestamp_iptv - 1800) + '-' + timestamp_to_date(timestamp_iptv + 1800)
