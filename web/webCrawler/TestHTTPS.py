# coding=gbk

import urllib.request
import urllib.parse
import time
import re
import csv
from bs4 import BeautifulSoup
import time
import codecs
import random

filename = 'input' + '.csv'
file_output = 'output' + '.csv'
encoding = 'utf-8'  # 设定文件编码，这里文件要提供给windows用户
flag = True  # 不处理第一行
counter_time = 0

header = {

            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

# 打开输出文件
g = open(file_output, 'w', encoding=encoding)
writer = csv.writer(g)


# 打开输入文件
with codecs.open(filename, 'r', encoding) as f:
    reader = csv.reader(f)

    for row in reader:
        if flag:
            row = row + ['厂商']
            writer.writerow(row)
            flag = False
            time.sleep(3)
        else:
            mac_tmp = row[18]

            n = 4
            mac = ''
            for i in row[18]:
                if i == ':':
                    mac = mac + '-'
                else:
                    mac = mac + i

            url = 'https://mac.51240.com/' + mac + '__mac/'
            print(mac)

            request = urllib.request.Request(url, headers=header)
            response = urllib.request.urlopen(request)
            f = response.read().decode('UTF8')
            # print(response.getcode())

            index = f.find('<td bgcolor="#F5F5F5" align="center">厂商</td>')
            a = f[index+100: index + 200]

            ans = a[a.find('>')+1: a.find('<')]
            print(ans)
            row = row + [ans]
            writer.writerow(row)

            counter_time = counter_time + 3.5
            time.sleep(3.1)
            print("time consumed:", counter_time)

