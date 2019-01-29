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


def query_ottnode_zte(n, cookie):
    url = 'https://117.135.56.61:8443/monitor/ottnode_query.action'
    form = {
        'areaid': '# all#',
        'nodeid': 'SHFX_NODE3',
        'starttime': startTime + ' 00:00:00',
        'endtime': endTime + ' 00:00:00'
    }

    # 可以改成dict，好看点
    # default nodeid SHFX_NODE3 -> 区域中心
    if n == 1:
        form['nodeid'] = 'SHFX_NODE1'
    if n == 2:
        form['nodeid'] = 'SHFX_NODE2'
    if n == 3:
        form['nodeid'] = 'OTT_3'
    if n == 4:
        form['nodeid'] = 'servicenode2'
    if n == 'cm':
        form['nodeid'] = 'servicenode3'
    if n == 'bs':
        form['nodeid'] = 'servicenode4'
    if n == 'jd':
        form['nodeid'] = 'servicenode5'
    if n == 'sj':
        form['nodeid'] = 'servicenode6'
    if n == 'fx':
        form['nodeid'] = 'servicenode7'
    if n == 'js':
        form['nodeid'] = 'servicenode8'

    f = ww.post_web_page_ssl(url, form, cookie)
    encodedjson = json.loads(f)

    # unit单位 upstreamband回源带宽
    upstreamband = max(encodedjson['upstreamband'])
    concurrent = max(encodedjson['concurrent'])
    bandwidth = max(encodedjson['bandwidth'])
    mean = sum(encodedjson['bandwidth'])/len(encodedjson['bandwidth'])
    return concurrent, float(bandwidth), mean, upstreamband


g_zte = open('cdn_rate_zte.csv', 'a', newline='')
writer_zte = csv.writer(g_zte)
n_days = int(input('想取多少天数据？:'))
for i in range(n_days):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=n_days-i)
    ts = now - delta
    te = now - datetime.timedelta(days=n_days-i - 1)
    # sjc = str(int(time.time() * 1000))
    startTime = ts.strftime('%Y-%m-%d')  # 调整时间格式
    endTime = te.strftime('%Y-%m-%d')  # 调整时间格式

    cookie = wl.zte_anyservice_uniportal_v2()
    concurrent_0, bandwidth_0, mean_0, upstreamband_0 = query_ottnode_zte(0, cookie)    # 区域中心
    concurrent_1, bandwidth_1, mean_1, upstreamband_1 = query_ottnode_zte(1, cookie)    # 节点1
    concurrent_2, bandwidth_2, mean_2, upstreamband_2 = query_ottnode_zte(2, cookie)    # 节点2
    concurrent_3, bandwidth_3, mean_3, upstreamband_3 = query_ottnode_zte(3, cookie)    # 节点3
    concurrent_4, bandwidth_4, mean_4, upstreamband_4 = query_ottnode_zte(4, cookie)    # 节点4
    concurrent_cm, bandwidth_cm, mean_cm, upstreamband_cm = query_ottnode_zte('cm', cookie)    #
    concurrent_bs, bandwidth_bs, mean_ns, upstreamband_bs = query_ottnode_zte('bs', cookie)    #
    concurrent_jd, bandwidth_jd, mean_jd, upstreamband_jd = query_ottnode_zte('jd', cookie)    #
    concurrent_sj, bandwidth_sj, mean_sj, upstreamband_sj = query_ottnode_zte('sj', cookie)
    concurrent_fx, bandwidth_fx, mean_fx, upstreamband_fx = query_ottnode_zte('fx', cookie)
    concurrent_js, bandwidth_js, mean_js, upstreamband_js = query_ottnode_zte('js', cookie)

    csv_content_zte = [startTime, bandwidth_0, bandwidth_1, bandwidth_2, bandwidth_3, bandwidth_4, bandwidth_cm,
                       bandwidth_bs, bandwidth_jd, bandwidth_sj, bandwidth_fx, bandwidth_js,
                       bandwidth_0+bandwidth_1+bandwidth_2+bandwidth_3+ bandwidth_4,
                       bandwidth_cm+bandwidth_bs+bandwidth_jd+bandwidth_sj+bandwidth_fx+bandwidth_js,
                       mean_0 + mean_1 + mean_2 + mean_3 + mean_4
                       + mean_cm + mean_ns + mean_jd + mean_sj + mean_fx + mean_js
                       ]
    writer_zte.writerow(csv_content_zte)
    print(i)

