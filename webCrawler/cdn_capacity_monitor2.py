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
    fbc = fbt = fc = f

    fb_count = fb_total = 0
    # 播放成功率
    while fbc.find('Count') > 1:
        fbc = fbc[fbc.find('Count')+1:]
        tmp_count = float(fbc[fbc.find(':')+1:fbc.find(',')])
        fb_count = fb_count + tmp_count
    print(fb_count)

    while fbt.find('Total') > 1:
        fbt = fbt[fbt.find('Total')+1:]
        tmp_total = float(fbt[fbt.find(':')+1:fbt.find(',')])
        fb_total = fb_total + tmp_total
    print(fb_total)

    exit()
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

    print('%.2f' % epg_latency, '%.2f' % epg_success_ratio)
    # 互联网电视节目播放成功率

