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
    form = {
        'paramData': '{\"location\": 4, \"secFrom\": \"' + startTime + ' 00:00:00\", \"secTo\": \"' + startTime + ' 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}'
    }
    url = 'http://117.144.107.165:8088/evqmaster/report/reportaction!returnKpiData.action'
    f = ww.post_web_page(url, form, cookie)
    print(f)
    tmp = f[f.find('maxStreamSTBs') + 18:]
    maxStreamSTBs = f[f.find('maxStreamSTBs') + 18: f.find('maxStreamSTBs') + 18 + tmp.index('\\')]
    return maxStreamSTBs


print(sqm_nei(cookie))