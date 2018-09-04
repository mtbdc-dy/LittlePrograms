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

