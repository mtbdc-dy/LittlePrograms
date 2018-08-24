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
    date = myPackages.getime.yesterday(1)
    print(date)
    filename = 'CMNET出口数据统计报表(' + date + ').xlsx'

    f = xlrd.open_workbook(filename)
    table = f.sheet_by_name("CMNET出口数据统计报表")
    nrows = table.nrows

    for i in range(nrows):
        row = table.row_values(i)
        if row[1] == 'OTT/IPTV（总）':
            ott_max_rate = row[4]
    print(ott_max_rate/1024)
