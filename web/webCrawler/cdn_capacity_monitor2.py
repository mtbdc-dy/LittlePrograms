import time
import xlrd
import random
import urllib.error
import urllib.request
import ssl
import datetime
import myPackages.getime as md
import web.webCrawler.login
import web.webCrawler.webcrawler
import myPackages.mailtools
import csv
import json

"""
先复制CMNET出口报表至目录，重要的事情说三遍
先复制CMNET出口报表至目录，重要的事情说三遍
先复制CMNET出口报表至目录，重要的事情说三遍
OTT、IPTV 流量统计四部部分组成：
# 1、iptv
# 2、SQM
# 3、CMNET出口数据统计报表
# 4、发送邮件
"""

'''Constants'''
# 输出文件名
file_output = 'cdn_rate.csv'
# IPTV
IPTV_total_capacity = 1241
print('中兴总容量： {:d}G'.format(IPTV_total_capacity))
# OTT
FX_FengHuo_OTT = 240
YP_FengHuo_OTT = 90
FX_HuaWei_OTT = 108
PD_HuaWei_OTT = 150
OTT_total_capacity = FX_FengHuo_OTT + YP_FengHuo_OTT + FX_HuaWei_OTT + PD_HuaWei_OTT
print('OTT总容量： {:d}G'.format(OTT_total_capacity))

# 打开输出文件
g = open(file_output, 'a', newline='')
writer = csv.writer(g)
g_zte = open('cdn_rate_zte.csv', 'a', newline='')
writer_zte = csv.writer(g_zte)

# 查询时间
now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
ts = now - delta
sjc = str(int(time.time() * 1000))
startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
endTime = now.strftime('%Y-%m-%d')  # 调整时间格式


def timestamp_to_date(time_stamp, format_string="%H:%M"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


# 烽火
def fenghuo():
    now_tiem = time.time()
    url = 'https://39.134.89.13:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit' \
          '_bytes_total%7Bdevice%3D~%22%5Elo%7Cbond0%7Cbond1%22%7D%5B5m%5D))%20%20*%208&start='\
          + ('%d' % (now_tiem - (now_tiem + 8 * 3600) % 86400 - 86400)) + '&end='\
          + ('%d' % (now_tiem - (now_tiem + 8 * 3600) % 86400)) + '&step=120'
    f = web.webCrawler.webcrawler.get_web_page_ssl(url, 'grafana_user=fonsview; grafana_remember=c3b58bb8cedb745aec3cc76133b253f2ef3811425f9e86a89a308bf16692ae82bc26b431; csk_sess=827941d628a2d37d')
    fenghuo_dict = json.loads(f)
    fenghuo_list = fenghuo_dict['data']['result'][0]['values']
    ans = list()
    for item in fenghuo_list:
        ans.append(float(item[1]))
    m = max(ans)
    for item in fenghuo_list:
        if m == float(item[1]):
            now_tiem = float(item[0])
            # print(item[1])
    now_tiem -= 1800
    # print(timestamp_to_date(now_tiem))
    str_ott = '' + timestamp_to_date(now_tiem)
    now_tiem += 3600
    # print(timestamp_to_date(now_tiem))
    str_ott = str_ott + '-' + timestamp_to_date(now_tiem)
    return max(ans)/1024/1024, str_ott


fenghuo_ott, ott_peak_period = fenghuo()


'''part1 zte'''
cookie = web.webCrawler.login.zte_anyservice_uniportal_v2()
url = 'https://117.135.56.61:8443/dashboard_queryChartData.action'
form = {
}
f = web.webCrawler.webcrawler.post_web_page_ssl(url, form, cookie)
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


def query_ottnode_zte(n, cookie):
    url = 'https://117.135.56.61:8443/monitor/ottnode_query.action'
    form = {
        'areaid': '# all#',
        'nodeid': 'SHFX_NODE3',
        'starttime': startTime + ' 00:00:00',
        'endtime': endTime + ' 00:00:00'
    }
    if n == 1:
        form['nodeid'] = 'SHFX_NODE1'
    if n == 2:
        form['nodeid'] = 'SHFX_NODE2'
    if n == 3:
        form['nodeid'] = 'OTT_3'
    if n == 4:
        form['nodeid'] = 'servicenode2'
    f = web.webCrawler.webcrawler.post_web_page_ssl(url, form, cookie)
    encodedjson = json.loads(f)

    # unit单位 upstreamband回源带宽
    upstreamband = max(encodedjson['upstreamband'])
    concurrent = max(encodedjson['concurrent'])
    bandwidth = max(encodedjson['bandwidth'])
    return concurrent, bandwidth, upstreamband


concurrent_0, bandwidth_0, upstreamband_0 = query_ottnode_zte(0, cookie)
concurrent_1, bandwidth_1, upstreamband_1 = query_ottnode_zte(1, cookie)
concurrent_2, bandwidth_2, upstreamband_2 = query_ottnode_zte(2, cookie)
concurrent_3, bandwidth_3, upstreamband_3 = query_ottnode_zte(3, cookie)
concurrent_4, bandwidth_4, upstreamband_4 = query_ottnode_zte(4, cookie)


csv_content_zte = [startTime,
                   concurrent_0, bandwidth_0, '{:.2f}'.format(bandwidth_0/96*100), upstreamband_0,
                   concurrent_1, bandwidth_1, '{:.2f}'.format(bandwidth_1/240*100), upstreamband_1,
                   concurrent_2, bandwidth_2, '{:.2f}'.format(bandwidth_2/240*100), upstreamband_2,
                   concurrent_3, bandwidth_3, '{:.2f}'.format(bandwidth_3/240*100), upstreamband_3,
                   concurrent_4, bandwidth_4, '{:.2f}'.format(bandwidth_4/120*100), upstreamband_4]

print('{:.2f}'.format(bandwidth_0/96*100), '{:.2f}'.format(bandwidth_1/240*100),
      '{:.2f}'.format(bandwidth_2 / 240 * 100), '{:.2f}'.format(bandwidth_3/240*100),
      '{:.2f}'.format(bandwidth_4 / 240 * 100))

'''part2 SQM'''
cookie = web.webCrawler.login.sqm_117()
# SQM峰值流用户数
# 系统特性 取某一日的值时需要始末日期一致
form = {
    'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}'
}
url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
f = web.webCrawler.webcrawler.post_web_page(url, form, cookie)
print(f)
tmp = f[f.find('maxStreamSTBs') + 18:]
maxStreamSTBs = f[f.find('maxStreamSTBs') + 18: f.find('maxStreamSTBs') + 18 + tmp.index('\\')]

# SQM终端盒子总数
url = 'http://117.144.107.165:8088/evqmaster/networkaction!returnAreaDetailByID.action'
form = {
    'paramData': '{\"id\":4,\"KPIUTCSec\":\"2000-01-01 00:00:00\",\"SampleInterval\":86400,\"ty'
                 'pe\":\"2\",\"realtime\":\"realtime\"}'
}
f = web.webCrawler.webcrawler.post_web_page(url, form, cookie)
tmp_index = f.find('上海市(')
tmp_index_ed = f[tmp_index:].find(')')
sum_box = f[tmp_index+4:tmp_index + tmp_index_ed]

# SQM故障用户占比
url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
form = {
    'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\", \"idfilter\": \"4\", \"type\": \"usercard\", \"dataType\": \"1\"}'
}
f = web.webCrawler.webcrawler.post_web_page(url, form, cookie)
tmp_index = f.find('GrnDevices')
f = f[tmp_index:]
tmp_normal_device = f[f.find(':')+1:f.find(',')]
tmp_index = f.find('RedDevices')
f = f[tmp_index:]
tmp_red_device = f[f.find(':') + 1:f.find(',')]
tmp_index = f.find('YlwDevices')
f = f[tmp_index:]
tmp_ylw_device = f[f.find(':') + 1:f.find(',')]
tmp_index = f.find('BlueDevices')
f = f[tmp_index:]
f = f[f.find(':') + 1:]
tmp_blue_device = ''
for i in f:
    if i.isdigit():
        tmp_blue_device = tmp_blue_device + i
    else:
        continue
laggy_device_ratio = 100 - (float(tmp_normal_device)/(float(tmp_normal_device)+float(tmp_blue_device)+float(tmp_ylw_device)+float(tmp_red_device)) * 100)


# SQM取NEI相关
def sqm_nei(cookie):
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnMiguData.action'
    form = {
        'paramData': '{\"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"location\"'
                     ': 4, \"dimension\": \"platform\", \"platform\": \"\", \"tType\": 2, \"isMigu\": false, \"isMiguShanxi'
                     '\": false, \"bIncludeShanxi\": false}'
    }

    f = web.webCrawler.webcrawler.post_web_page(url, form, cookie)
    fc = f
    # EPG响应时长
    tmp_index = f.find('CntEpgRspTime')
    f = f[tmp_index:]
    CntEpgRspTime = f[f.find(':') + 1:f.find(',')]
    CntEpgRspTime = float(CntEpgRspTime)
    tmp_index = f.find('TotEpgRspTime')
    f = f[tmp_index:]
    TotEpgRspTime = f[f.find(':') + 1:f.find(',')]
    TotEpgRspTime = float(TotEpgRspTime)
    epg_latency = TotEpgRspTime/CntEpgRspTime / 1000000

    # EPG响应成功率
    tmp_index = fc.find('Requests')
    fc = fc[tmp_index:]
    Requests = fc[fc.find(':') + 1:fc.find(',')]
    Requests = float(Requests)
    tmp_index = fc.find('Responses')
    fc = fc[tmp_index:]
    Responses = fc[fc.find(':') + 1:fc.find(',')]
    Responses = float(Responses)
    epg_success_ratio = Responses / Requests * 100
    return epg_latency, epg_success_ratio


# epg_latency = 0
# epg_success_ratio = 0
epg_latency, epg_success_ratio = sqm_nei(cookie)

'''part3 CMNET出口数据统计报表'''
date = myPackages.getime.yesterday(1)
filename = 'CMNET出口数据统计报表(' + date + ').xlsx'
f = xlrd.open_workbook(filename)
table = f.sheet_by_name("CMNET出口数据统计报表")
nrows = table.nrows
ott_max_rate = '0'
ott_mean_rate = '0'
for i in range(nrows):
    row = table.row_values(i)
    if row[1] == 'OTT/IPTV（总）':
        ott_max_rate = row[4]
        ott_mean_rate = row[3]


'''part4 发送邮件'''
# ott_max_rate = float(ott_max_rate) + fenghuo_ott
ott_max_rate = (26.99 + 100.06) * 1000 + fenghuo_ott
ott_mean_rate = float(ott_mean_rate)
max_rate = float(max_rate)
maxStreamSTBs = float(maxStreamSTBs)
max_user = float(max_user)
print(maxStreamSTBs, max_rate, max_user, ott_max_rate)
title = date + '互联网电视指标'
email_content = 'OTT峰值时间段: ' + ott_peak_period + \
                '; OTT峰值流用户数: {:.2f}万人; OTT峰值流速: {:.2f}Gbps; OTT利用率: {:.2f}%;'\
                .format(maxStreamSTBs/10000, ott_max_rate/1000, ott_max_rate/1000/OTT_total_capacity*100) \
                + 'IPTV峰值时间段: ' + iptv_peak_period +\
                '; IPTV峰值流用户数: {:.2f}万人; IPTV峰值流速: {:.2f}Gbps; IPTV利用率: {:.2f}%。'\
                    .format(max_user/10000, max_rate, max_rate/IPTV_total_capacity*100)
email_content = '(' + startTime + ')' + email_content
csv_content = [startTime] + ['{:.2f}'.format(maxStreamSTBs/10000)] + ['{:.2f}'.format(ott_max_rate/1000)] + ['%.2f' % (ott_mean_rate/1000)] + ['{:.2f}'.format(ott_max_rate/1000/OTT_total_capacity*100)] + ['{:.2f}'.format(max_user/10000)] + ['{:.2f}'.format(max_rate)] + ['{:.2f}'.format(max_rate/IPTV_total_capacity*100)] + ['{:.2f}'.format(laggy_device_ratio)] + [sum_box] + ['%.2f' % epg_success_ratio] + ['%.2f' % epg_latency]
print('email_content: ', email_content)
print('csv_content:', csv_content)
user = [
    'xuyuan2@sh.chinamobile.com', 'bianningyan@sh.chinamobile.com', 'chenlei5@sh.chinamobile.com',
    'huanglinling@sh.chinamobile.com', 'lilin2@sh.chinamobile.com', 'liujinlin@sh.chinamobile.com',
    'wuzhouhao@sh.chinamobile.com', 'xulingxia@sh.chinamobile.com', 'yanmin@sh.chinamobile.com',
    'yuxf@sh.chinamobile.com', 'zhenj@sh.chinamobile.com', 
    'zhangcheng2@sh.chinamobile.com', 'yushu@sh.chinamobile.com', 'zhengsen@sh.chinamobile.com',
    'zhouqihui@sh.chinamobile.com', 'chenhuanmin@sh.chinamobile.com', 'wuqian@sh.chinamobile.com',
    'yangjie@sh.chinamobile.com', 'xiongyt@sh.chinamobile.com', 'tanmiaomiao@sh.chinamobile.com',
    'wucaili@sh.chinamobile.com', 'dingy@sh.chinamobile.com', 'fenghongyu@sh.chinamobile.com',
    'xuzicheng@sh.chinamobile.com', 'zhanghe@sh.chinamobile.com'
]


print('EPG请求成功率：%.2f' % epg_success_ratio, end=' ')
if epg_success_ratio < 99:
    print('\033[32;0m<99%\033[0m')
if epg_latency > 0.02:
    print('\033[32;0mepg_latency过高\033[0m')


print()
print('After this operation, 25 e-mails will be sent.')
check_code = input('y or n or s(save)').lower()
if check_code == 'y':
    writer.writerow(csv_content)
    writer_zte.writerow(csv_content_zte)
    ret = myPackages.mailtools.mail139_customise(title, email_content, user)
    if ret:
        print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
    else:
        print("failed")  # 如果发送失败则会返回filed
elif check_code == 's':
    writer.writerow(csv_content)
    writer_zte.writerow(csv_content_zte)