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

# 查询时间
now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
ts = now - delta
sjc = str(int(time.time() * 1000))
startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
endTime = now.strftime('%Y-%m-%d')  # 调整时间格式


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
    nei_json = json.loads(f)

    print(nei_json)
    print(nei_json.keys())
    print(nei_json['resultData'])
    print(type(nei_json['resultData']))
    nei_json = json.loads(f)

    # EPG响应时长
    return

    # fc = f
    # # EPG响应时长
    # tmp_index = f.find('CntEpgRspTime')
    # f = f[tmp_index:]
    # CntEpgRspTime = f[f.find(':') + 1:f.find(',')]
    # CntEpgRspTime = float(CntEpgRspTime)
    # tmp_index = f.find('TotEpgRspTime')
    # f = f[tmp_index:]
    # TotEpgRspTime = f[f.find(':') + 1:f.find(',')]
    # TotEpgRspTime = float(TotEpgRspTime)
    # epg_latency = TotEpgRspTime/CntEpgRspTime / 1000000
    #
    # # EPG响应成功率
    # tmp_index = fc.find('Requests')
    # fc = fc[tmp_index:]
    # Requests = fc[fc.find(':') + 1:fc.find(',')]
    # Requests = float(Requests)
    # tmp_index = fc.find('Responses')
    # fc = fc[tmp_index:]
    # Responses = fc[fc.find(':') + 1:fc.find(',')]
    # Responses = float(Responses)
    # epg_success_ratio = Responses / Requests * 100
    # return epg_latency, epg_success_ratio


cookie = wl.sqm_117()
epg_latency, epg_success_ratio = sqm_nei(cookie)
