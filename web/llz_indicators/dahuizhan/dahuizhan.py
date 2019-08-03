# -*- coding: utf-8 -*-
# @Time : 2019/3/5,005 9:34
# @Author : 徐缘
# @FileName: dahuizhan.py
# @Software: PyCharm


"""
大会战 采集部分
从dahuizhan.xlsx上次记录至昨日。
三部分：
    1、SQM
    2、ELK
    3、普天拨测

打包命令: pyinstaller -F -i img\dahuizhan.ico web\llz_indicators\dahuizhan\dahuizhan.py
        pyinstaller -F web\llz_indicators\dahuizhan\dahuizhan.py
"""

import json
import xlrd
import sys
import datetime
import ssl
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from xlutils.copy import copy
import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww


# Constant
filename = 'dahuizhan.xls'         # 文件名

companies = ['huawei', 'hy', 'fonsview', 'zte']        # 平面
query_curl = {
    "5xx": {"bool": {"must": [{"wildcard": {"httpstatus": "5??"}}],
                     "must_not": [{"term": {"cache_server_ip": "127.0.0.1"}}]}},
    "all": {"bool": {"must": [{"wildcard": {"httpstatus": "???"}}],
                     "must_not": [{"term": {"cache_server_ip": "127.0.0.1"}}]}}
    # "all": {"wildcard": {"httpstatus": "???"}}
}   # elk_search query中语句


def sqm_nei(cookie, day_sqm):
    addr = 'http://117.144.107.165:8088'
    addr = 'http://10.222.4.87:8088'

    startTime = day_sqm.strftime('%Y-%m-%d')
    # 业务关键指标（首缓冲时延(ms)，EPG响应成功率(%)，在线播放成功率(%)，卡顿时间占比(%)，wifi接入占比(%)，卡顿次数占比(%)
    # EPG响应时延(ms)，EPG响应总次数，EPG响应成功次数
    url = addr + '/evqmaster/report/reportaction!returnMiguData.action'
    form = {
        'paramData': '{\"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"location\"'
                     ': 4, \"dimension\": \"platform\", \"platform\": \"\", \"tType\": 2, \"isMigu\": false, \"isMiguShanxi'
                     '\": false, \"bIncludeShanxi\": false}'
    }
    f = ww.post_web_page(url, form, cookie)
    tmp_dict = json.loads(f)
    sqm_dict = json.loads(tmp_dict['resultData'])
    # print(sqm_dict.keys())
    fault = {0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 15}     # 14 就是 9 / 15 就是10
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
    # 先数据全部汇聚好，然后按公式算就成了 来来来欣赏一下飞思达的英文
    # Latency	首缓冲时延
    # DownSpeed	下载速率
    # EPGLoadSuc	EPG响应成功率
    # OnlineSucPlay	播放成功率
    # timeProprot	卡顿时长占比
    # wifiAcount	wifi接入占比
    # UnitTCaton	单位时间(h)卡顿次数
    # CatonAcount	卡顿次数占比(%)
    # EPGLoadDelay	EPG响应时延(ms)
    # EPGRequests	EPG响应总次数
    # EPGReponses	EPG响应成功次数
    # LoginSuc	登录成功率(%)
    res = list()

    Latency = round(list_total[4]/list_count[4]/1000, 2)
    # DownSpeed = round(list_total[9]*8/list_total[6]/1024/1024, 2)
    EPGLoadSuc = round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2)
    OnlineSucPlay = round(list_total[8] / list_total[7] * 100, 2)
    timeProprot = round(list_total[2] / 1000000 / list_total[6] * 100, 2)

    access_wifi = 0
    access_total = 0
    for item in sqm_dict['net'][0]['DistStreamDevice'].split('@'):
        tmp = item.split('#')
        if tmp[0] == '2':
            access_wifi = int(tmp[1])
        access_total += int(tmp[1])
    # wifiAcount = round(access_wifi / access_total * 100, 2)

    UnitTCaton = round(list_total[3]*3600/list_total[6], 2)
    CatonAcount = round(list_total[10]*100/list_total[7], 2)
    EPGLoadDelay = round(sqm_dict['epg'][0]['TotEpgRspTime'] / sqm_dict['epg'][0]['CntEpgRspTime'] / 1000, 2)
    EPGRequests = sqm_dict['epg'][0]['Requests']
    EPGReponses = sqm_dict['epg'][0]['Responses']
    # LoginSuc = round(sqm_dict['epgSuc'][0]['Responses'] / sqm_dict['epgSuc'][0]['Requests'] * 100, 2)
    # res.extend([Latency, DownSpeed, EPGLoadSuc, OnlineSucPlay, timeProprot, wifiAcount, UnitTCaton, CatonAcount,
    #             EPGLoadDelay, EPGRequests, EPGReponses, LoginSuc])
    res.extend([Latency, EPGLoadSuc, OnlineSucPlay, timeProprot, UnitTCaton, CatonAcount,
                EPGLoadDelay, EPGRequests, EPGReponses])

    # 用户卡顿分布
    url = addr + '/evqmaster/report/reportaction!returnKpiData.action'
    form = {
        'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\", \"idfilter\": \"4\", \"type\": \"usercard\", \"dataType\": \"1\"}'
    }

    f = ww.post_web_page(url, form, cookie)
    tmp_index = f.find('GrnDevices')
    f = f[tmp_index:]
    tmp_normal_device = f[f.find(':') + 1:f.find(',')]
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
    laggy_device_ratio = 100 - (float(tmp_normal_device) / (
                float(tmp_normal_device) + float(tmp_blue_device) + float(tmp_ylw_device) + float(
            tmp_red_device)) * 100)
    res.append(round(laggy_device_ratio, 2))

    # SQM峰值流用户数
    # 系统特性 取某一日的值时需要始末日期一致
    form = {
        'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}'
    }
    url = addr + '/evqmaster/report/reportaction!returnKpiData.action'
    f = ww.post_web_page(url, form, cookie)
    tmp_dict = json.loads(f)
    sqm_dict = json.loads(tmp_dict['resultData'])
    res.extend([sqm_dict[0]['maxActiveSTBs'], sqm_dict[0]['maxStreamSTBs'], sqm_dict[0]['TotalDevices']])

    return res
    # # 卡顿时间占比 = 卡顿时长 / 下载时长
    # print('卡顿时间占比:', round(list_total[2] / 1000000 / list_total[6] * 100, 2))
    #
    # # 卡顿次数占比 = 15 / 7 * 100
    # lag_times = list_total[10]
    # total_times = list_total[7]  # 播放节目数
    # print('卡顿次数占比:', round(lag_times / total_times * 100, 2))
    #
    # # 首帧缓冲时长
    # print('首帧缓冲时长(S):', round(list_total[4] / list_count[4] / 1000000, 2))  # 秒
    #
    # # 电视播放成功率
    # print('电视播放成功率', round(list_total[8] / list_total[7] * 100, 2))
    #
    # # EPG加载成功率 加载成功率 和 登录成功率
    # # print(sqm_dict['epg'])
    # # print(sqm_dict['epgSuc'])
    # print('EPG加载成功率', round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))
    #
    # # 卡顿时间占比, 首帧缓冲时长, 电视播放成功率, EPG加载成功率
    # return (round(lag_duration / total_duration * 100, 2),
    #         round(list_total[4] / list_count[4] / 1000000, 2), round(list_total[8] / list_total[7] * 100, 2),
    #         round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))


def elk_query(cookie, day_elk):

    def requ_post(u, form):
        ssl._create_default_https_context = ssl._create_unverified_context

        json_info = bytes(json.dumps(form), 'utf8')
        header = {
            'Content-Type': 'application/json',
            'Cookie': cookie,
            'kbn-version': '6.6.1',     # 6.4.2 -> 6.6.1
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        print(u, cookie)
        request = urllib.request.Request(u, headers=header, data=json_info)
        response = urllib.request.urlopen(request)
        f = response.read().decode("utf8")
        return json.loads(f)

    yesterday = day_elk.strftime('%Y.%m.%d')
    tmp_content = list()
    for cj in companies:    # 厂家
        url = 'https://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_count&method=POST'.format(cj, yesterday)
        for status in query_curl.keys():
            my_form = {
                "query": query_curl[status]
            }
            print(url, my_form)
            dict_tmp = requ_post(url, my_form)
            tmp_content.append(dict_tmp['count'])

    '''流量查询'''
    for cj in companies:  # 厂家
        url = 'https://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_search%3Fsize%3D0&method=POST' \
            .format(cj, yesterday)
        my_form = {
            "aggs": {
                "group_by_time": {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": "5m",
                        "format": "yyyy-MM-dd HH:mm"
                    },
                    "aggs": {
                        "data_rate": {
                            "sum": {
                                "field": "filesize"
                            }
                        }
                    }
                }
            }
        }
        print(url, my_form)
        dict_tmp = requ_post(url, my_form)
        # print(dict_tmp)
        elk_rate_dict = dict_tmp['aggregations']['group_by_time']['buckets']
        a = lambda x: x['data_rate']['value']
        tmp_content.append(round(max(list(map(a, [x for x in elk_rate_dict]))) / 1024 / 1024 / 1024 / 300 * 8, 2))
        tmp_content.append(round(sum(list(map(a, [x for x in elk_rate_dict])))
                                 / len(list(map(a, [x for x in elk_rate_dict]))) / 1024 / 1024 / 1024 / 300 * 8, 2))

    return tmp_content


def zte_query(cookie, day_zte):
    services = ['QQcache', 'BIGCACHE', 'SMALLcache']
    begin = day_zte.strftime('%Y-%m-%d')
    end = (day_zte + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    def hit_ratio(s):
        # 节点状态码
        url = 'https://39.134.88.198:8443/stat/requesthit_query.action'
        form = {
            'offset': '8',
            'beginDate': begin + ' 00:00:00',
            'endDate': end + ' 00:00:00',
            'areaid': '',
            'nodeid': s,
            'deviceid': '',
            'apptype': '',
            'servicemode': '',
            'cachetype': '',
            'inserttypeid': '',
            'terminalid': '',
            'domaintype': '1',
            'domain': '',
        }
        f = ww.post_web_page_ssl(url, form, cookie)
        # print(f)
        tmp_dict = json.loads(f)

        "EDIT SCRIPT FROM HERE"
        tmp_dict = tmp_dict['message']

        hit = 0
        miss = 0

        for item in tmp_dict:
            hit += int(item['hitsnum'])
            miss += int(item['missnum'])

        return hit, miss

    def download_rate(s):
        # 下载速率
        url = 'https://39.134.88.198:8443/stat/userdown_query.action'
        form = {
            'offset': '8',
            'beginDate': begin + ' 00:00:00',
            'endDate': end + ' 00:00:00',
            'areaid': '',
            'nodeid': s,
            'deviceid': '',
            'servicemode': '',
            'cachetype': '',
            'inserttypeid': '',
            'terminalid': '',
            'ratetype': '',
            'domain': '',
        }
        f = ww.post_web_page_ssl(url, form, cookie)
        tmp_dict = json.loads(f)

        "EDIT SCRIPT FROM HERE"
        download_rate = tmp_dict['message']['messageline']

        userdownload = 0
        for item in download_rate:
            userdownload += float(item['userdownload'])
        userdownload = userdownload / len(download_rate) / 1024 / 1024
        return round(userdownload, 2)

    tmp_content = list()
    for service in services:
        for item in hit_ratio(service):
            tmp_content.append(item)
    for service in services:
        tmp_content.append(download_rate(service))
    return tmp_content


def putian_query(day_putian):
    startTime = day_putian.strftime('%Y-%m-%d')
    endTime = (day_putian + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    # http://10.221.17.131:9091/report/bizman/common/result.jsp?timename=jiakuandahuizhan
    url = 'http://10.221.17.131:9091/report/bizman/common/report.jsp?timename=jiakuandahuizhan&reportType=&cac=27621' \
          '97&iam=12675442&timename=jiakuandahuizhan&change=true&sid=null&reportFileName=1554792716199&u=r&page=null' \
          '&pageSizeCus=null&timetype=customday&datefromto={}~{}'.format(startTime, startTime)
    print(url)

    f = ww.get_web_page(url)
    soup = BeautifulSoup(f, "html.parser")
    # print(soup.prettify())  # 这很beautiful
    # print(soup.find(attrs={'id': 'jiakuandahuizhan'}).prettify())
    res = list()
    for table_rows in soup.find(attrs={'id': 'jiakuandahuizhan'}).find_all('tr'):
        res.append(table_rows.find_all('td')[2].find('span').get_text())

    return res


if __name__ == '__main__':
    # 读excel
    oldWb = xlrd.open_workbook(filename, formatting_info=True)
    table = oldWb.sheet_by_name("Sheet1")
    n_rows = table.nrows  # number of rows
    if n_rows == 1 or n_rows == 0:
        print("Error: NO EXCEL FOUND.")
        input('Press any key to exit.')
        sys.exit()
    newWb = copy(oldWb)  # 复制
    newWs = newWb.get_sheet(0)  # 取sheet1

    # 日期
    now = datetime.datetime.now()
    pre_update_day = datetime.datetime.strptime(table.col_values(0)[-1], '%Y-%m-%d')
    print(pre_update_day)
    delta = now - pre_update_day - datetime.timedelta(days=1)       # 要查多少天
    if delta.days == 0:
        print("All data is up-to-date.")
        input('Press any key to exit.')
        sys.exit('Goodbye!')
    elif delta.days < 0:
        print("Date Error")
        sys.exit()
    print('待查询的天数：', delta.days)

    # 查询准备
    cookie_sqm = wl.sqm_10()   # 登录SQM
    cookie_elk = wl.elk()       # 登录ELK
    cookie_zte = wl.zte_cdn_omc()   # 登录中兴CDN IAM

    # 开始查询
    for i in range(delta.days):
        csv_content = list()
        day_query = pre_update_day + datetime.timedelta(days=i + 1)
        csv_content.append(day_query.strftime('%Y-%m-%d'))
        print('i:', i)
        print('Date:', csv_content[0])

        # sqm
        result = sqm_nei(cookie_sqm, day_query)
        for item in result:
            csv_content.append(item)

        # elk
        result = elk_query(cookie_elk, day_query)
        for item in result:
            csv_content.append(item)

        # zte
        result = zte_query(cookie_zte, day_query)
        for item in result:
            csv_content.append(item)

        # putian
        result = putian_query(day_query)
        for item in result:
            csv_content.append(item)

        for j, item in enumerate(csv_content):
            newWs.write(n_rows + i, j, item)
        print()
    newWb.save(filename)  # 保存至result路径

    input('Press any key to exit.')







