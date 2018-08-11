import urllib.request
import urllib.parse
import time
import http.cookiejar
import csv, codecs
from bs4 import BeautifulSoup
import random
import urllib.error


# 网卡MAC分析
#
# 注意:电脑网络设置有无使用代理
# mac 地址在输入文件的第十九列 [18]

# soft coding
#
url = 'https://mac.51240.com/f4-b8-a7-6a-60-6b__mac/'   # 默认查询地址
file_mac = 'input_mac.csv'
file_ua = 'output_UA.txt'
file_proxy = 'output_proxy.csv'
file_output_manufacturer = 'output_manufacturer.csv'
list_ua = []
list_proxy = []
count = 1 # 查询次数
counter_time = 0    # 记录查询时间
flag = True # 设置CSV第一行标志，不读数据

# 打开UA、Proxy文件，读数据，写入列表
f = open(file_ua, 'r')
g = open(file_proxy, 'r')
reader = csv.reader(g)
for item in f:
    list_ua.append(item[0:-1])
for item in reader:
    list_proxy.append(item)
f.close()
g.close()

# 打开输出文件，以待写入数据
#
h = open(file_output_manufacturer, 'w')
writer = csv.writer(h)

with open(file_mac, 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        if flag:
            row = row + ['厂商']
            writer.writerow(row)
            flag = False
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

            count = count + 1
            print(str(count) + ':')

            # 挂随机代理
            #
            P = list_proxy[random.randint(0, 122)]
            # print(P)
            proxy = {
                P[2]: P[0] + ':' + P[1]
            }
            proxy_support = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)

            # 伪装浏览器申请
            #
            A = list_ua[random.randint(0,53)]
            print(A)
            header = {
                # 'User-Agent': A
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            }

            request = urllib.request.Request(url, headers=header)
            response = urllib.request.urlopen(request)

            f = response.read().decode('UTF8')
            print(response.getcode())

            index = f.find('<td bgcolor="#F5F5F5" align="center">厂商</td>')
            a = f[index + 100: index + 200]

            ans = a[a.find('>') + 1: a.find('<')]
            print(ans)

            row = row + [ans]
            writer.writerow(row)
            tmp_time = random.randint(1, 2)
            counter_time = counter_time + 4
            time.sleep(4)

print(counter_time)




