# -*- coding: utf-8 -*-
# @Time: 2019/8/15,015 11:08
# @Last Update: 2019/8/15,015 11:08
# @Author: 徐缘
# @FileName: data_rate&watcher.py
# @Software: PyCharm


import json
import time
import datetime     # 日期

import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww


def zte(n):
    startTime = (datetime.datetime.now() - datetime.timedelta(n+1)).strftime('%Y-%m-%d')
    endTime = (datetime.datetime.now() - datetime.timedelta(n)).strftime('%Y-%m-%d')
    # print(startTime, endTime)
    cookie_zte = wl.zte_anyservice_uniportal_v2()
    url_zte = 'https://117.135.56.61:8443/monitor/ottnode_query.action'
    # form_zte = {
    #     'starttime': startTime + ' 00:00:00',
    #     'endtime': endTime + ' 00:00:00',
    #     'cpid': '000000000000',
    #     'servicetype': 'total'
    # }
    form_zte = {
        'granularity': '5',
        'starttime': startTime + ' 00:00:00',
        'endtime': endTime + ' 00:00:00',
        # 'cpid': '000000000000',
        'areaid': '#all#',
        'nodeid': 'all'
    }
    f_zte = ww.post_web_page_ssl(url_zte, form_zte, cookie_zte)
    # print(f_zte)
    zte_dict = json.loads(f_zte)        # 读json(str) => dict
    # print(zte_dict)
    # print(zte_dict.keys(), len(zte_dict))
    online_user = zte_dict['concurrent']
    bandwidth = zte_dict['bandwidth']
    max_rate_tmp = max(bandwidth)
    mean_rate = round(sum(bandwidth) / len(bandwidth), 2)
    max_rate = max(bandwidth)
    max_user = max(online_user)
    print(startTime)
    print('max user: ', max_user)
    print('max rate: ', max_rate)
    print('mean rate: ', mean_rate)

    # 获取峰值时间段
    # iptv_time_tmp = str(zte_dict['xaxis'][bandwidth.index(max_rate_tmp)])[11:]
    # # print(bandwidth.index(max_rate_tmp))
    # # print(iptv_time_tmp)
    # h = iptv_time_tmp[0:2]
    # m = iptv_time_tmp[3:5]
    # # print(h, m)
    # t = (2018, 12, 31, int(h) + 8, int(m), 0, 0, 0, 0)  # 鬼知道中兴的研发在搞什么
    # timestamp_iptv = time.mktime(t)
    # peak_period = timestamp_to_date(timestamp_iptv - 1800) + '-' + timestamp_to_date(timestamp_iptv + 1800)
    # print('峰值时间段:', peak_period)
    # return max_user, max_rate, mean_rate, peak_period
    return max_user, max_rate, mean_rate


if __name__ == '__main__':
    for i in range(3):      # 0,1,2
        zte(i)


