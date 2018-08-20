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
cookie = 'JSESSIONID=22A6B376FD58EEF915EF84D6F2E93ECE'
# cookie = webCrawler.login.sqm()
url = 'http://106.14.197.84:65009/evqmaster/configaction!returnMasterVersion.action'
f = webCrawler.webcrawler.get_web_page(url, cookie)
print('0:')
print(f)

form = {
    'paramData': '{\"location\":4,\"secFrom\":\"2018-07-20 00:00:00\",\"secTo\":\"2018-08-19 00:00:00\",\"dimension\":\"1\",\"idfilter\":\"4\",\"type\":\"activeuser\",\"dataType\":\"1\"}'
}

url = 'http://106.14.197.84:65009/evqmaster/report/reportaction!returnKpiData.action'
f = webCrawler.webcrawler.post_web_page(url, form, cookie)
print('1:')
print(f)

url = 'http://106.14.197.84:65009/evqmaster/useraction!SaveUSActionInfo.action'

form = {
    'paramData': '{\"location\":4,\"secFrom\":\"2018-07-20 00:00:00\",\"secTo\":\"2018-08-19 00:00:00\",\"dimension\":\"1\",\"idfilter\":\"4\",\"type\":\"activeuser\",\"dataType\":\"1\"}'
}

f = webCrawler.webcrawler.post_web_page(url, form, cookie)
print('2:')
print(f)
