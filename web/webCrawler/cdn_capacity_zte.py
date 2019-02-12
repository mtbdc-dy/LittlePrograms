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

NODE_DICT = {
        'area1': 'SHFX_NODE3',      # 区域中心1
        'area2': 'servicenode10',   # 区域中心2
        1: 'SHFX_NODE1',            # 节点1
        2: 'SHFX_NODE2',            # 节点2
        3: 'OTT_3',                 # 节点3
        4: 'servicenode2',          # 节点4
        5: 'servicenode9',          # 节点5
        'cm': 'servicenode3',       # 崇明
        'bs': 'servicenode4',       # 宝山
        'jd': 'servicenode5',       # 嘉定
        'sj': 'servicenode6',       # 松江
        'fx': 'servicenode7',       # 奉贤
        'js': 'servicenode8',       # 金山
        'qz': 'servicenode11',      # 钦州
        'qp': 'servicenode12',      # 青浦
    }


def query_ottnode_zte(n, cookie):
    url = 'https://117.135.56.61:8443/monitor/ottnode_query.action'
    form = {
        'areaid': '# all#',
        'nodeid': NODE_DICT[n],
        'starttime': startTime + ' 00:00:00',
        'endtime': endTime + ' 00:00:00'
    }

    f = ww.post_web_page_ssl(url, form, cookie)
    encodedjson = json.loads(f)
    # unit单位 upstreamband回源带宽
    upstreamband = max(encodedjson['upstreamband'])
    concurrent = max(encodedjson['concurrent'])
    bandwidth = max(encodedjson['bandwidth'])
    mean = sum(encodedjson['bandwidth'])/len(encodedjson['bandwidth'])

    # 数值小的时候 传过来的单位会变
    if encodedjson['unit'] == 'Mbps':
        return round(float(bandwidth) / 1024, 2), round(mean / 1024, 2)
    else:
        return float(bandwidth), round(mean, 2)
    # 数值小的时候 传过来的单位会变
    # if encodedjson['unit'] == 'Mbps':
    #     return concurrent, round(float(bandwidth)/1024, 2), round(mean/1024, 2), upstreamband/1024
    # else:
    #     return concurrent, float(bandwidth), mean, upstreamband


g_zte = open('cdn_rate_zte.csv', 'a', newline='')
writer_zte = csv.writer(g_zte)
n_days = int(input('想取多少天数据？: '))
print(len(NODE_DICT) * n_days, 'requests will be sent.')

for i in range(n_days):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=n_days-i)
    ts = now - delta
    te = now - datetime.timedelta(days=n_days-i - 1)
    # sjc = str(int(time.time() * 1000))
    startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
    endTime = te.strftime('%Y-%m-%d')  # 调整时间格式

    cookie = wl.zte_anyservice_uniportal_v2()
    max_rate = list()
    mean_rate = list()
    for j in NODE_DICT.keys():
        max_rate_tmp, mean_rate_tmp = query_ottnode_zte(j, cookie)
        max_rate.append(max_rate_tmp)
        mean_rate.append(mean_rate_tmp)

    csv_content_zte = [startTime]
    csv_content_zte.extend(max_rate)
    csv_content_zte.extend(mean_rate)
    writer_zte.writerow(csv_content_zte)
    print(i)
    print(csv_content_zte)

