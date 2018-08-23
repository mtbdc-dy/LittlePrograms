import time
import csv
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import os

# SQM
if __name__ == '__main__':
    cookie = webCrawler.login.sqm()

    form = {
        'paramData': '{\"location\": 4, \"secFrom\": \"2018-08-22 00:00:00\", \"secTo\": \"2018-08-22 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}'
    }
    # 取数据
    url = 'http://106.14.197.84:65009/evqmaster/report/reportaction!returnKpiData.action'
    f = webCrawler.webcrawler.post_web_page(url, form, cookie)
    print(f)
    tmp = f[f.find('maxStreamSTBs')+18:]
    maxStreamSTBs = f[f.find('maxStreamSTBs')+18: f.find('maxStreamSTBs')+18+tmp.index('\\')]
    print(maxStreamSTBs)
