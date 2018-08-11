import time
import csv
import random
import urllib.error
import ssl
import datetime
import webCrawler.login
import webCrawler.webcrawler
import os

# OTT、IPTV 流量查询
# 1、烽火
# 2、华为
# 3、iptv

# part1 烽火
# 时间获取
te = int(time.mktime((time.localtime()[0], time.localtime()[1], time.localtime()[2], 0, 0, 0, 0, 0, 0)))
ts = te - (1533484800-1533398400)
te = str(te)
ts = str(ts)


url = 'http://39.134.89.13:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes%7Bgroup%3D%22%E5%A5%89%E8%B4%A4%E4%B8%AD%E5%BF%83%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22%5Elo%7Cbond0%7Cbond1%22%7D%5B5m%5D))%20%20*%208&start=' + ts + '&end=' + te + '&step=240'
f = webCrawler.webcrawler.get_web_page(url)
f = f[83:-5]
maximum = 0
for item in f.split("\""):
    if item <= ':':
        if float(item) > maximum:
            maximum = float(item)

# print(maximum)
print("%.2f" % (maximum/1024/1024/1024*1.0735))

url = 'http://39.134.89.13:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes%7Bgroup%3D%22%E6%9D%A8%E6%B5%A6%E8%BE%B9%E7%BC%98%E8%8A%82%E7%82%B9%22%2Cdevice%3D~%22%5Elo%7Cbond0%7Cbond1%22%7D%5B5m%5D))%20%20*%208&start=' + ts + '&end=' + te + '&step=240'
f = webCrawler.webcrawler.get_web_page(url)
f = f[83:-5]
maximum = 0
for item in f.split("\""):
    if item <= ':':
        if float(item) > maximum:
            maximum = float(item)

# print(maximum)
print("%.2f" % (maximum/1024/1024/1024*1.0735))


# part2 华为
