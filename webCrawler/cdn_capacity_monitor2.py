import time
import csv
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import os


cookie = 'JSESSIONID=C3510015E4066BBC6E607C2B56A58C2B'
cookie = 'JSESSIONID=B8A6BCFD9B6515E73EEA38E95978C159'

url = 'http://106.14.197.84:65009/evqmaster/configaction!login.action'

form = {
    'username': 'xuyuan',
    'password': '2EF60361839CBA359266E62F16E21A7A',
    'checkcode': '0005'
}

form = {
    "location": 4,
    "secFrom": "2018-07-20 00:00:00",
    "secTo": "2018-08-19 00:00:00",
    "dimension": "1",
    "idfilter": "4",
    "type": "activeuser",
    "dataType": "1"
}

url = 'http://106.14.197.84:65009/evqmaster/report/reportaction!returnKpiData.action'
f = webCrawler.webcrawler.post_web_page(url, form, cookie)
print('1:')
print(f)

url = 'http://106.14.197.84:65009/evqmaster/useraction!SaveUSActionInfo.action'

form = {
    "location": 4,
    "secFrom": "2018-07-20 00:00:00",
    "secTo": "2018-08-19 00:00:00",
    "dimension": "1",
    "idfilter": "4",
    "type": "activeuser",
    "dataType": "1"
}

f = webCrawler.webcrawler.post_web_page(url, form, cookie)
print('2:')
print(f)