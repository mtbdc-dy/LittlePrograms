# -*- coding: utf-8 -*-
# @Time : 三月 01, 2019
# @Author : 徐缘
# @FileName: part1.py
# @Software: PyCharm


"""
查询SQM
互联网电视卡顿时长占比
互联网电视节目播放成功率
互联网电视节目首次加载时延
EPG访问成功率
"""

import web.webCrawler.webcrawler as ww
import web.webCrawler.login as wl
import datetime
import json

now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
ts = now - delta
startTime = ts.strftime('%Y-%m-%d')


'''part4 SQM'''
print('SQM：')
cookie = wl.sqm_117()
# 系统特性 取某一日的值时需要始末日期一致


# SQM取NEI相关
def sqm_nei(cookie):
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnMiguData.action'
    form = {
        'paramData': '{\"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"location\"'
                     ': 4, \"dimension\": \"platform\", \"platform\": \"\", \"tType\": 2, \"isMigu\": false, \"isMiguShanxi'
                     '\": false, \"bIncludeShanxi\": false}'
    }
    f = ww.post_web_page(url, form, cookie)
    print(f)
    exit()
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

    # 卡顿时间占比, 首帧缓冲时长, 电视播放成功率, EPG加载成功率
    return (round(lag_duration / total_duration * 100, 2),
            round(list_total[4] / list_count[4] / 1000000, 2), round(list_total[8] / list_total[7] * 100, 2),
            round(sqm_dict['epg'][0]['Responses'] / sqm_dict['epg'][0]['Requests'] * 100, 2))


lag_time_proportion, first_frame_latency, tv_success_ratio, epg_success_ratio = sqm_nei(cookie)
print(lag_time_proportion, first_frame_latency, tv_success_ratio, epg_success_ratio)
