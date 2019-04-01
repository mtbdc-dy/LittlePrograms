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
需良好的网络环境

四部部分组成：
# 1、华为 => 峰值流量
# 2、 烽火 => 峰值流量、热点时段
# 3、iptv => 峰值流量、峰值用户数、热点时段
# 4、SQM =>  OTT峰值用户数
# X、CMNET出口数据统计报表（Deprecated）
# 6、发送邮件

维护成本 超大 涉及的系统太多了。
"""


'''Constants'''
# 输出文件名
file_output = 'cdn_rate.csv'
# IPTV
IPTV_total_capacity = 2055
print('中兴总容量： \033[32;0m{:d}\033[0mG'.format(IPTV_total_capacity))
# OTT
FX_FengHuo_OTT = 240
YP_FengHuo_OTT = 150
FengHuo_Total = YP_FengHuo_OTT + FX_FengHuo_OTT
PD_HuaWei_OTT = 222
OTT_total_capacity = FX_FengHuo_OTT + YP_FengHuo_OTT + PD_HuaWei_OTT
print('OTT总容量： \033[32;0m{:d}\033[0mG'.format(OTT_total_capacity))
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

    time_end = str(md.get_today_zero_stamp())
    time_start = str(int(time_end) - 24 * 3600)
    # print(time_start, time_end)

    # 奉贤分组
    # url = 'https://39.134.87.216:31943/rest/pm/history'
    # form = {
    #     'param': r'{"pageIndex":1,"historyTimeRange":0,"beginTime":' + time_start + r'000,"endTime":' + time_end + r'000,"isGetGraphicGroupData":true,"mo2Index":"[{\"dn\":\"com.huawei.hvs.pop=2101535\",\"indexId\":\"11735\",\"displayValue\":\"\",\"aggrType\":2}]","pmViewPage":"historyPm","isQueryOriginal":false}'
    # }
    # # print(form)
    # form_data = urllib.parse.urlencode(form).encode('utf8')
    # f = post_ssl(url, form_data)
    # # print(f)
    # huawei_dict = json.loads(f)
    # huawei_list = huawei_dict['result']['groupQueryData'][0][0]['indexValues']
    # # print(huawei_list)
    # HW_FX_ott_rate = list()
    #
    # for item in huawei_list:
    #     HW_FX_ott_rate.append(float(item['indexValue']))
    # HW_ott_rate = max(HW_FX_ott_rate)
    # print(max(HW_FX_ott_rate))

    HW_ott_rate = 0
    url = 'https://39.134.87.216:31943/rest/pm/history'
    form = b'param=%7B%22pageIndex%22%3A1%2C%22historyTimeRange%22%3A0%2C%22beginTime%22%3A' +\
           bytes(str(time_start), encoding='utf-8') + b'000%2C%22endTime%22%3A' +\
           bytes(str(time_end), encoding='utf-8') +\
           b'000%2C%22isGetGraphicGroupData%22%3Atrue%2C%22isMonitorView%22%3Atrue%2C%22mo2Index%22%3A%22%5B%7B%5C%22' \
           b'dn%5C%22%3A%5C%22com.huawei.hvs.pop%3D2101531%5C%22%2C%5C%22indexId%5C%22%3A%5C%2211735%5C%22%2C%5C%22di' \
           b'splayValue%5C%22%3A%5C%22%5C%22%2C%5C%22aggrType%5C%22%3A2%7D%5D%22%7D'
    # form = b'param=%7B%22pageIndex%22%3A1%2C%22historyTimeRange%22%3A0%2C%22beginTime%22%3A1546185600000%2C%22endTime%22%3A1546272000000%2C%22isGetGraphicGroupData%22%3Atrue%2C%22mo2Index%22%3A%22%5B%7B%5C%22dn%5C%22%3A%5C%22com.huawei.hvs.pop%3D2101535%5C%22%2C%5C%22indexId%5C%22%3A%5C%2211735%5C%22%2C%5C%22displayValue%5C%22%3A%5C%22%5C%22%2C%5C%22aggrType%5C%22%3A2%7D%5D%22%2C%22pmViewPage%22%3A%22historyPm%22%2C%22isQueryOriginal%22%3Afalse%7D'
    f = post_ssl(url, form)
    # print(f)
    huawei_dict = json.loads(f)
    huawei_list = huawei_dict['result']['groupQueryData'][0][0]['indexValues']
    # print(huawei_list)
    HW_FX_ott_rate = list()
    time_stamp = list()

    for item in huawei_list:
        HW_FX_ott_rate.append(float(item['indexValue']))
        time_stamp.append(item['timestampStr'].split(' ')[1])

    time_stamp_peak = time_stamp[HW_FX_ott_rate.index(max(HW_FX_ott_rate))]
    # print('峰值时刻:', time_stamp_peak)
    t = (2018, 12, 31, int(time_stamp_peak.split(':')[0]), int(time_stamp_peak.split(':')[1]), 0, 0, 0, 0)
    huawei_stamp = time.mktime(t)
    ott_peak_period = timestamp_to_date(huawei_stamp - 1800) + '-' + timestamp_to_date(huawei_stamp + 1800)
    print('峰值时间段:', ott_peak_period)
    print('浦东峰值:', max(HW_FX_ott_rate))
    print('浦东均值:', round(sum(HW_FX_ott_rate)/len(HW_FX_ott_rate)), 2)
    HW_ott_rate += max(HW_FX_ott_rate)
    # print(max(HW_FX_ott_rate))
    return HW_ott_rate, ott_peak_period, sum(HW_FX_ott_rate)/len(HW_FX_ott_rate)


print('华为：')
huawei_ott, ott_peak_period, huawei_mean_ott = huawei()


# p2 烽火
def fenghuo():
    now_tiem = time.time()
    # url = 'https://sh.csk.rhel.cc:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes_total%7Bgroup%3D%22%E5%A5%89%E8%B4%A4%E4%B8%AD%E5%BF%83%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22e.*%22%7D%5B5m%5D))%20%20*%208&start=1546963200&end=1547049600&step=600'
    url = 'https://sh.csk.rhel.cc:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes_total%7Bgroup%3D%22%E5%A5%89%E8%B4%A4%E4%B8%AD%E5%BF%83%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22e.*%22%7D%5B5m%5D))%20%20*%208&start='+ ('%d' % (now_tiem - (now_tiem + 8 * 3600) % 86400 - 86400)) + '&end='\
          + ('%d' % (now_tiem - (now_tiem + 8 * 3600) % 86400)) + '&step=240'

    print(url)
    f = ww.get_web_page_ssl(url, 'csk_sess=af51ac156f60680e; grafana_user=fonsview; grafana_remember=7a09dff47b67b97a0fedb308cc09636af8e2861184a8dc69b48ecb43e3a6464380a07fbd')
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
    return max(ans)/1024/1024/1024, str_ott


def fenghuo_yp():
    now_tiem = time.time()
    url = 'https://sh.csk.rhel.cc:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes_total%7Bgroup%3D%22%E6%9D%A8%E6%B5%A6%E8%BE%B9%E7%BC%98%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22e.*%22%7D%5B5m%5D))%20%20*%208&start='+ ('%d' % (now_tiem - (now_tiem + 8 * 3600) % 86400 - 86400)) + '&end='\
          + ('%d' % (now_tiem - (now_tiem + 8 * 3600) % 86400)) + '&step=240'
    f = ww.get_web_page_ssl(url, 'grafana_user=fonsview; grafana_remember=c3b58bb8cedb745aec3cc76133b253f2ef3811425f9e86a89a308bf16692ae82bc26b431; csk_sess=827941d628a2d37d')
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
    return max(ans)/1024/1024/1024, str_ott


print('烽火：')
fenghuo_ott_fx, fenghuo_ott_yp, fenghuo_ott, fenghuo_mean_ott = wl.fonsview()


# p3 中兴
def zte():
    cookie = wl.zte_anyservice_uniportal_v2()
    url = 'https://117.135.56.61:8443/monitor/cpstat_query.action?t=1549951114288'
    form = {
        'starttime': startTime + ' 00:00:00',
        'endtime': endTime + ' 00:00:00',
        'cpid': '000000000000',
        'servicetype': 'total'
    }
    f = ww.post_web_page_ssl(url, form, cookie)
    # print(f)
    zte_dict = json.loads(f)
    # print(zte_dict.keys())
    online_user = zte_dict['onlineusers']
    bandwidth = zte_dict['bandwidth']
    max_rate_tmp = max(bandwidth)
    mean_rate = round(sum(bandwidth) / len(bandwidth), 2)
    max_rate = max(bandwidth)
    max_user = max(online_user)
    print('max user: ', max_user)
    print('max rate: ', max_rate)
    print('mean rate: ', mean_rate)
    # 获取峰值时间段
    iptv_time_tmp = str(zte_dict['xaxis'][bandwidth.index(max_rate_tmp)])[11:]
    # print(bandwidth.index(max_rate_tmp))
    # print(iptv_time_tmp)
    h = iptv_time_tmp[0:2]
    m = iptv_time_tmp[3:5]
    # print(h, m)
    t = (2018, 12, 31, int(h) + 8, int(m), 0, 0, 0, 0)  # 鬼知道中兴的研发在搞什么
    timestamp_iptv = time.mktime(t)
    iptv_peak_period = timestamp_to_date(timestamp_iptv - 1800) + '-' + timestamp_to_date(timestamp_iptv + 1800)
    print('峰值时间段:', iptv_peak_period)
    return max_user, max_rate, mean_rate, iptv_peak_period


print('中兴：')
max_user, max_rate, mean_rate, iptv_peak_period = zte()

'''part4 SQM'''
print('SQM：')
# print(startTime)
cookie = wl.sqm_117()
# cookie = 'JSESSIONID=4CD5A39212EAA84F77E3BE9817B6AC09'
# SQM峰值流用户数
# 系统特性 取某一日的值时需要始末日期一致
form = {
    'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}'
}
url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
f = ww.post_web_page(url, form, cookie)
# print(f)
tmp = f[f.find('maxStreamSTBs') + 18:]
maxStreamSTBs = f[f.find('maxStreamSTBs') + 18: f.find('maxStreamSTBs') + 18 + tmp.index('\\')]
print('峰值流用户数:', maxStreamSTBs)

# SQM终端盒子总数
url = 'http://117.144.107.165:8088/evqmaster/networkaction!returnAreaDetailByID.action'
form = {
    'paramData': '{\"id\":4,\"KPIUTCSec\":\"2000-01-01 00:00:00\",\"SampleInterval\":86400,\"ty'
                 'pe\":\"2\",\"realtime\":\"realtime\"}'
}
f = ww.post_web_page(url, form, cookie)
tmp_index = f.find('上海市(')
tmp_index_ed = f[tmp_index:].find(')')
sum_box = f[tmp_index+4:tmp_index + tmp_index_ed]

# SQM故障用户占比
url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
form = {
    'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\", \"idfilter\": \"4\", \"type\": \"usercard\", \"dataType\": \"1\"}'
}

f = ww.post_web_page(url, form, cookie)
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
# SQM取NEI相关
def sqm_nei(cookie):
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnMiguData.action'
    form = {
        'paramData': '{\"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"location\"'
                     ': 4, \"dimension\": \"platform\", \"platform\": \"\", \"tType\": 2, \"isMigu\": false, \"isMiguShanxi'
                     '\": false, \"bIncludeShanxi\": false}'
    }
    f = ww.post_web_page(url, form, cookie)
    tmp_dict = json.loads(f)
    sqm_dict = json.loads(tmp_dict['resultData'])
    # print(sqm_dict.keys())
    fault = {0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 15}
    list_count = list()
    list_total = list()
    for i in fault:
        count_tmp = 0
        total_tmp = 0
        for item in sqm_dict['vod']:
            if item['FaultID'] == i:
                count_tmp += item['Count']
                total_tmp += item['Total']
        list_count.append(count_tmp)
        list_total.append(total_tmp)
    # print(list_total)
    # print(list_count)

    # 卡顿时间占比 = 卡顿时长 / 下载时长
    lag_duration = list_total[2] / 1000000
    total_duration = list_total[6]
    print('卡顿时间占比:', round(lag_duration / total_duration * 100, 2))

    # 卡顿次数占比 = 15 / 7 * 100
    lag_times = list_total[10]
    total_times = list_total[7]  # 播放节目数
    print('卡顿次数占比:', round(lag_times / total_times * 100, 2))

    # 首帧缓冲时长
    print('首帧缓冲时长(S):', round(list_total[4] / list_count[4] / 1000000, 2))  # 秒

    # 电视播放成功率
    print('电视播放成功率', round(list_total[8] / list_total[7] * 100, 2))

    # EPG加载成功率 加载成功率 和 登录成功率
    # print(sqm_dict['epg'])
    # print(sqm_dict['epgSuc'])
    print('EPG加载成功率', round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))

    # 卡顿时间占比, 卡顿次数占比, 首帧缓冲时长, 电视播放成功率, EPG加载成功率
    return (round(lag_duration / total_duration * 100, 2), round(lag_times / total_times * 100, 2),
            round(list_total[4] / list_count[4] / 1000000, 2), round(list_total[8] / list_total[7] * 100, 2),
            round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))


lag_time_proportion, lag_count_proportion, first_frame_latency, tv_success_ratio, epg_success_ratio = sqm_nei(cookie)
print()

'''partX CMNET出口数据统计报表'''
date = myPackages.getime.yesterday(1)
# filename = 'CMNET出口数据统计报表(' + date + ').xlsx'
# f = xlrd.open_workbook(filename)
# table = f.sheet_by_name("CMNET出口数据统计报表")
# nrows = table.nrows
# ott_max_rate = '0'
# ott_mean_rate = '0'
# for i in range(nrows):
#     row = table.row_values(i)
#     if row[1] == 'OTT/IPTV（总）':
#         ott_max_rate = row[4]
#         ott_mean_rate = row[3]

'''part5 准备邮件内容'''
# 数据准备和格式转换
huawei_ott = round(huawei_ott, 2)                               # 华为汇总
huawei_mean_ott = round(huawei_mean_ott, 2)                     # 华为均值
fenghuo_ott = round(fenghuo_ott, 2)                             # 烽火汇总
fenghuo_mean_ott = round(fenghuo_mean_ott, 2)                   # 烽火均值
ott_max_rate = round(huawei_ott + fenghuo_ott, 2)               # OTT求和
ott_mean_rate = round(huawei_mean_ott + fenghuo_mean_ott, 2)    # OTT均值
max_rate = round(max_rate, 2)                       # IPTV汇总
mean_rate = round(mean_rate, 2)                     # IPTV均值
maxStreamSTBs = float(maxStreamSTBs)                            # OTT人数
max_user = float(max_user)                          # IPTV人数

# 邮件正文
title = 'DoNotReply 互联网电视指标' + date
email_content = '<br>OTT峰值时间段: ' + ott_peak_period + \
                '; OTT峰值流用户数: {:.2f}万人; OTT峰值流速: {:.2f}Gbps; OTT利用率: {:.2f}%。'\
                .format(maxStreamSTBs/10000, ott_max_rate, ott_max_rate/OTT_total_capacity*100) \
                + '</br><br>IPTV峰值时间段: ' + iptv_peak_period +\
                '; IPTV峰值流用户数: {:.2f}万人; IPTV峰值流速: {:.2f}Gbps; IPTV利用率: {:.2f}%。'\
                    .format(max_user/10000, max_rate, max_rate/IPTV_total_capacity*100) + '</br>'
# email_content = '(' + startTime + ')' + email_content
# 邮件表格
table_content = """<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<table border="" style="border-collapse: collapse; text-align: center">
    <tr style="font-weight: bold;">
        <td></td><td>容量(Gbps)</td><td>峰值(Gbps)</td><td>均值(Gbps)</td><td>利用率(%)</td>
    </tr>

    <tr>
        <td>烽火汇总</td><td>""" + str(FengHuo_Total) + """</td><td>""" + str(fenghuo_ott) + """</td><td>""" + str(fenghuo_mean_ott) + """</td><td>""" + str(round(fenghuo_ott / FengHuo_Total * 100, 2)) + """</td>
    </tr>

    <tr>
        <td>华为</td><td>""" + str(PD_HuaWei_OTT) + """</td><td>""" + str(huawei_ott) + """</td><td>""" + str(huawei_mean_ott) + """</td><td>""" + str(round(huawei_ott / PD_HuaWei_OTT * 100, 2)) + """</td>
    </tr>

    <tr>
        <td>OTT总和</td><td>""" + str(OTT_total_capacity) + """</td><td>""" + str(ott_max_rate) + """</td><td>""" + str(ott_mean_rate) + """</td><td>""" + str(round(ott_max_rate / OTT_total_capacity * 100, 2)) + """</td>
    </tr>

    <tr>
        <td>中兴(IPTV)汇总</td><td>""" + str(IPTV_total_capacity) + """</td><td>""" + str(max_rate) + """</td><td>""" + str(mean_rate) + """</td><td>""" + str(round(max_rate/IPTV_total_capacity*100, 2)) + """</td>
    </tr>
</table>
<br>
<p>""" + email_content + """</p>"""
# excel内容
csv_content = [startTime] + ['{:.2f}'.format(maxStreamSTBs/10000)] + ['{:.2f}'.format(ott_max_rate)] +\
              ['%.2f' % ott_mean_rate] + ['{:.2f}'.format(ott_max_rate/OTT_total_capacity*100)] +\
              ['{:.2f}'.format(max_user/10000)] + ['{:.2f}'.format(max_rate)] + ['{:.2f}'.format(mean_rate)] +\
              ['{:.2f}'.format(max_rate/IPTV_total_capacity*100)] + ['{:.2f}'.format(laggy_device_ratio)] +\
              [sum_box] + [lag_time_proportion] + [lag_count_proportion] + [first_frame_latency] + [tv_success_ratio] +\
              [epg_success_ratio]
print('email_content: ', email_content)
# print('csv_content:', csv_content)
user = [
    'xuyuan2@sh.chinamobile.com', 'bianningyan@sh.chinamobile.com', 'chenlei5@sh.chinamobile.com',
    'huanglinling@sh.chinamobile.com', 'lilin2@sh.chinamobile.com', 'liujinlin@sh.chinamobile.com',
    'wuzhouhao@sh.chinamobile.com', 'xulingxia@sh.chinamobile.com', 'yanmin@sh.chinamobile.com',
    'yuxf@sh.chinamobile.com', 'zhenj@sh.chinamobile.com', 'wangyinchao@sh.chinamobile.com'
    'zhangcheng2@sh.chinamobile.com', 'yushu@sh.chinamobile.com', 'zhengsen@sh.chinamobile.com',
    'zhouqihui@sh.chinamobile.com', 'chenhuanmin@sh.chinamobile.com', 'wuqian@sh.chinamobile.com',
    'yangjie@sh.chinamobile.com', 'xiongyt@sh.chinamobile.com', 'tanmiaomiao@sh.chinamobile.com',
    'wucaili@sh.chinamobile.com', 'dingy@sh.chinamobile.com', 'fenghongyu@sh.chinamobile.com',
    'xuzicheng@sh.chinamobile.com', 'zhanghe@sh.chinamobile.com', 'sufeng@sh.chinamobile.com',
    'zhangcheng2@sh.chinamobile.com'
]
# user = ['xuyuan2@sh.chinamobile.com'] # 调试用

'''part6 指标达标检测'''
# print('EPG请求成功率：%.2f' % epg_success_ratio, end=' ')
# if epg_success_ratio < 99:
#     print('\033[32;0m<99%\033[0m')
# if epg_latency > 0.02:
#     print('\033[32;0mepg_latency过高\033[0m')

'''part7 存储数据和发送邮件'''
print()
print('Once you choose \'y\', ' + str(len(user)) + ' e-mails will be sent.')
check_code = input('y, n or s(save)').lower()
if check_code == 'y':
    writer.writerow(csv_content)
    ret = myPackages.mailtools.mail139_mine_table(title, table_content, user)
    if ret:
        print("ok")         # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
    else:
        print("failed")     # 如果发送失败则会返回filed
elif check_code == 's' or check_code == 'save':
    writer.writerow(csv_content)
