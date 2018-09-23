import time
import csv
from bs4 import BeautifulSoup
import random
import urllib.request
import web.webCrawler.webcrawler


# 获取西刺代理,并将验证后的代理保存
#
# 功能：
#   获取proxy的IP,port,http类型
#   使用该代理访问特定网站，确定可不可用

# soft coding
#
file_output_csv = 'output_proxy.csv'

# 变量定义
#
page = 0
page_max = 4  # 爬取西刺代理的页面数
proxy_count = 0  # 记录存下的代理数目
row = []  # 写入CSV的代理数据 缓存列表

# 打开CSV文件，以待写入数据
#

g = open(file_output_csv, 'w')
writer = csv.writer(g)
# writer.writerow([1,2,3])

while page < page_max:
    page = page + 1
    # i = random.randint(0, 53)
    print('page No.' + str(page) + ':')
    header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            }

    url = 'http://www.xicidaili.com/wn/' + str(page)

    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)

    f = response.read().decode('UTF8')
    print(response.getcode())
    # print(f)

    soup = BeautifulSoup(f, 'html.parser')
    trs1 = soup.find('table', id='ip_list')
    # print(trs1)
    trs = trs1.find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        if tds[1].find('img') is None:
            nation = '未知'
            locate = '未知'
        else:
            nation = tds[1].find('img')['alt'].strip()
            locate = tds[4].text.strip()
        ip = tds[1].text.strip()
        port = tds[2].text.strip()
        # address = tds[3].text.strip()
        protocol = tds[5].text.strip()

        row = [ip, port, protocol]
        # if protocol == 'HTTPS':
        if web.webCrawler.webcrawler.check_proxy(ip, port):
            proxy_count = proxy_count + 1
            print("proxy No.", proxy_count)
            writer.writerow(row)
    time.sleep(random.randint(1, 2))
