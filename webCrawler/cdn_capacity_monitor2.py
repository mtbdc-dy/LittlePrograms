import myPackages.getime
import xlrd
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import os

# OTT rate
if __name__ == '__main__':
    cookie = webCrawler.login.sqm()
    url = 'http://106.14.197.84:65009/evqmaster/report/reportaction!returnMiguData.action'
    form = {
        'paramData': '{\"secFrom\": \"2018-09-03 00:00:00\", \"secTo\": \"2018-09-03 00:00:00\", \"location\": '
                     '4, \"dimension\": \"platform\", \"platform\": \"\", \"tType\": 2, \"isMigu\": false, \"is'
                     'MiguShanxi\": false, \"bIncludeShanxi\": false}'

    }

    f = webCrawler.webcrawler.post_web_page(url, form, cookie)
    print(f)

    # EPG响应时长
    tmp_index = f.find('CntEpgRspTime')
    CntEpgRspTime = f[tmp_index][f[tmp_index:].find(':'):f[tmp_index:].find(',')]
    tmp_index = f.find('TotEpgRspTime')
    TotEpgRspTime = f[tmp_index][f[tmp_index:].find(':'):f[tmp_index:].find(',')]
    epg_latency = TotEpgRspTime/CntEpgRspTime / 1000000

    # EPG响应成功率
    tmp_index = f.find('Requests')
    Requests = f[tmp_index][f[tmp_index:].find(':'):f[tmp_index:].find(',')]
    tmp_index = f.find('Responses')
    Responses = f[tmp_index][f[tmp_index:].find(':'):f[tmp_index:].find(',')]
    epg_success_ratio = Responses / Requests * 100

    # 互联网电视节目播放成功率

