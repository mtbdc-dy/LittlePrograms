import time
import csv
import random
import urllib.error
import socket


# 网卡MAC分析
#
# 注意:电脑网络设置有无使用代理
# mac 地址在输入文件的第十九列 [18]


# soft coding
#
url = 'https://mac.51240.com/f4-b8-a7-6a-60-6b__mac/'   # 默认查询地址
# url = 'http://www.baidu.com/baidu?wd=ip&tn=monline_dg&ie=utf-8'    #百度查询ip
file_proxy = 'output_proxy.csv'
file_output_proxy = 'output_proxy_verified.csv'
list_proxy = []
count = 1  # 查询次数
counter_time = 0    # 记录查询时间
flag = True  # 设置CSV第一行标志，不读数据

h = open(file_output_proxy, 'w')
writer = csv.writer(h)

with open(file_proxy, 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        count = count + 1
        print(str(count) + ':')

        address = 'https://' + row[0] + ':' + row[1]
        print(address)
        proxy = {
            # 'https': 'https://' + P[0] + ':' + P[1]
            # 'http': 'http://180.110.6.55:3128'
            # 'http':'125.118.247.218:6666'
            # 'https': 'https://cmnet:cmnet@211.136.113.69:808'
            # 'https': 'https://114.231.66.99:22598'
            'https': address
        }
        print(proxy)
        proxy_support = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

        header = {
            # ':authority': 'mac.51240.com',
            # ':method': 'GET',
            # ':path': '/f4-b8-a7-6a-60-6b__mac/',
            # ':scheme': 'https',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'https: // mac.51240.com / f4 - b8 - a7 - 6a - 60 - 6b__mac /'
        }

        request = urllib.request.Request(url, headers=header)

        socket.setdefaulttimeout(2)
        # noinspection PyBroadException
        try:
            response = urllib.request.urlopen(request)
        except:
            print("Error Occur")
        else:
            f = response.read().decode('UTF8')
            print(response.getcode())
            writer.writerow(row)
            print(row)

        tmp_time = random.randint(2, 3)
        counter_time = counter_time + tmp_time
        time.sleep(1)

print("counter_time: ", counter_time)




