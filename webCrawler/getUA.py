import urllib.request
import urllib.parse
import time
import re
import csv
from bs4 import BeautifulSoup
import time
import codecs
import random

file_output = 'output_UA.txt'
A = 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)'
header = {
            'User-Agent': A
        }

proxy = {
    'https':'114.228.73.105:6666'
}
# https://www.baidu.com/baidu?wd=ip&tn=monline_dg&ie=utf-8 百度查ip
# http://www.xicidaili.com/nn/1 西刺代理
url = 'https://blog.csdn.net/u012175089/article/details/61199238'        # url = 'https://mac.51240.com/adads__mac/'

proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)


request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
f = response.read().decode('UTF8')
print(response.getcode())
print(f)

g = open(file_output, 'w', encoding='utf8')  # utf8   gb2312
writer = csv.writer(g)

index = 0
while(index != -1):
    index = f.find("Agent:")
    f = f[index+6:]
    ans = f[0:f.find("<")]
    row = [ans]
    print(row)
    writer.writerow(row)

# soup = BeautifulSoup(f,"html.parser")
# # print(soup.prettify())
# print("===============================")
# titles = soup.find_all('td')
# # HREF Hypertext Reference的缩写。意思是指定超链接目标的URL
# print(titles)