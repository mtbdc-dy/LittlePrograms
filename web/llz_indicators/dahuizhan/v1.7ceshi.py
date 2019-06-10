# -*- coding: utf-8 -*-
# @Time : 2019/5/21,021 9:31
# @Author : 徐缘
# @FileName: v1.7ceshi.py
# @Software: PyCharm


"""
大会战 采集部分
从dahuizhan.xlsx上次记录至昨日。
三部分：
    1、SQM
    2、ELK
    3、普天拨测

打包命令: pyinstaller -F -i img\dahuizhan.ico web\llz_indicators\dahuizhan\dahuizhan.py
"""

import web.webCrawler.webcrawler as ww
import web.webCrawler.login as wl
import urllib.request
import urllib.parse
import json
import xlrd
from bs4 import BeautifulSoup
import datetime
from xlutils.copy import copy
import time
import web.webCrawler.login as wl
import sys
import ssl


# Constant
filename = 'dahuizhan.xls'         # 文件名

companies = ['huawei', 'hy', 'fonsview', 'zte']        # 平面
query_curl = {                          # elk_search query中语句
    "5xx": {"wildcard": {"httpstatus": "5??"}},
    "all": {"wildcard": {"httpstatus": "*"}}
    # "all": {"wildcard": {"httpstatus": "???"}}
}


def sqm_nei(cookie, day_sqm):
    startTime = day_sqm.strftime('%Y-%m-%d')
    # 业务关键指标（首缓冲时延(ms)，EPG响应成功率(%)，在线播放成功率(%)，卡顿时间占比(%)，wifi接入占比(%)，卡顿次数占比(%)
    # EPG响应时延(ms)，EPG响应总次数，EPG响应成功次数
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
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
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
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
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


def elk_query(day_elk):

    def requ_post(u, form):
        json_info = bytes(json.dumps(form), 'utf8')
        header = {
            'Content-Type': 'application/json',
            'Cookie': 'searchguard_authentication=Fe26.2**58b9b06dca6c80d397da9f2a8de3d0e8c443a22f743e68c5d6e19ab6f83722e0*ImAxfRbmIEfZRFUIXslNxw*pn8F9R3Vhjz5x9wqBEQZjGGHQTmIuX9dqLRtpRn2xF6ViIezM6rplIEvy7LhmACuNDc6j7Wc2lkd3tZUMEWD7Sp1eYTi_XDAH1kkdc-vdK0Aa_R8tdHBJzx4OLeCntAY-HvbIfTCE8GnkwIP_GSR8HRtDnUkLGRL0pak4uVN-VTz4-6Q3v8NHYwRcaPkm2bILc9hy8adTbcwceXAD0gqdk5U2eCsl4ZkxMRr0IgmHbA**79a781f9685e2c7d5be49c91586db4b783c442b59a1e9cca85f27fa28bd33f9c*4kAyVrI8pN99pW1mR-QwamTa-LhCu2qtWQHhqWKZYhs; searchguard_storage=Fe26.2**4885c3cdb8c5a24bd52729c23dd7983529a89eea2b837f47c1e54472d9817b3a*WOymcqiVRHOMSzZS4PpXTw*weosPbNsIa2SOFOlUioSCll1O4oowQq-pxSW2ukeUtVllcOSqnN2_sSoaCmFaGyrUbxbMbZ4iO2EU6bOU-dCO_QfCzlCfnSoygLh4edUjvBPzVlmsKMm7APwuy93bdfi2FjFWf5kEym7G9GXAB0RT1IsGH5gNGXy5FtgXQmeTjJrZO3ldHtM1gQzPMJaPJlsGAEXKdsOWlyrqntbsNFWnuv8NY8I990EGqYxD6v4x9hwmjWSMCAp7jR63W8B5ff0**16b78b18e1c284718efa4ccfa7d7ae30783c43fc18c8afd273a8b5aefe42b858*lg0qzB3LqQVtj8F8cQ9taajzNdYwxUjtl8gMdR-NPW8',
            'kbn-version': '6.6.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        request = urllib.request.Request(u, headers=header, data=json_info)
        response = urllib.request.urlopen(request)
        f = response.read().decode("utf8")
        return json.loads(f)

    yesterday = day_elk.strftime('%Y.%m.%d')
    tmp_content = list()
    for cj in companies:    # 厂家
        url = 'http://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_count&method=POST'.format(cj, yesterday)
        for status in query_curl.keys():
            my_form = {
                "query": query_curl[status]
            }
            print(url, my_form)
            dict_tmp = requ_post(url, my_form)
            tmp_content.append(dict_tmp['count'])

    '''流量查询'''
    for cj in companies:  # 厂家
        url = 'http://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_search%3Fsize%3D0&method=POST' \
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


def putian_query(day_putian):
    startTime = day_putian.strftime('%Y-%m-%d')
    endTime = (day_putian + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    # http://10.221.17.131:9091/report/bizman/common/result.jsp?timename=jiakuandahuizhan
    # http://10.221.17.131:9091/report/bizman/common/report.jsp?timename=jiakuandahuizhan&reportType=&cac=5614146&iam=15614135&timename=jiakuandahuizhan&change=true&sid=null&reportFileName=1552455614217&iam=15614135&page=null&pageSizeCus=null&timetype=day&datefromto=2019-04-03~2019-04-04&bar=true
    # url = 'http://10.221.17.131:9091/report/bizman/common/report.jsp?timename=jiakuandahuizhan&reportType=&cac=56141' \
    #       '46&iam=15614135&timename=jiakuandahuizhan&change=true&sid=null&reportFileName=1552455614217&iam=15614135&' \
    #       'page=null&pageSizeCus=null&timetype=day&datefromto={}~{}&bar=true'.format(startTime, endTime)
    # url = 'http://10.221.17.131:9091/report/bizman/common/report.jsp?timename=jiakuandahuizhan&reportType=&cac=2762197&iam=12675442&timename=jiakuandahuizhan&change=true&sid=null&reportFileName=1554792716199&u=r&page=null&pageSizeCus=null&timetype=customday&datefromto=2019-04-02~2019-04-02'
    url = 'http://10.221.17.131:9091/report/bizman/common/report.jsp?timename=jiakuandahuizhan&reportType=&cac=2762197&iam=12675442&timename=jiakuandahuizhan&change=true&sid=null&reportFileName=1554792716199&u=r&page=null&pageSizeCus=null&timetype=customday&datefromto={}~{}'.format(startTime, startTime)
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
    elk_cookie = wl.elk()
    ssl._create_default_https_context = ssl._create_unverified_context
    form = {
        "query": {'match_all': {}}
    }
    json_info = bytes(json.dumps(form), 'utf8')
    header = {
        'Content-Type': 'application/json',
        'Cookie': elk_cookie,
        'kbn-version': '6.6.1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    request = urllib.request.Request('https://117.144.106.34:5601/api/console/proxy?path=_search&method=POST', headers=header, data=json_info)
    response = urllib.request.urlopen(request)
    f = response.read().decode("utf8")
    print(f)


