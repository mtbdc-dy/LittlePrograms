# -*- coding: utf-8 -*-
# @Time : 2019/3/4,004 10:25
# @Author : 徐缘
# @FileName: part3_elk.py
# @Software: PyCharm


"""
查询ELk
查询当天中兴/华为/杭研平面2xx/3xx/4xx/all 总数
"""
import web.webCrawler.webcrawler as ww
import urllib.request
import urllib.parse
import json
import xlrd
import xlwt
import datetime
from xlutils.copy import copy
import time


# Constant
filename = 'dahuizhan.xlsx'         # 文件名
companies = ['huawei', 'hy']        # 平面
# companies = []
query_curl = {                          # elk_search query中语句
    "2xx": {"wildcard": {"httpstatus": "2??"}},
    "3xx": {"wildcard": {"httpstatus": "3??"}},
    "4xx": {"wildcard": {"httpstatus": "4??"}},
    "all": {"match_all": {}}
}

# 日期相关
now = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday = now.strftime('%Y.%m.%d')
print(yesterday)


# POST 请求
def requ_post(u, form):
    json_info = bytes(json.dumps(form), 'utf8')
    header = {
        'Content-Type': 'application/json',
        'kbn-version': '6.4.2',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
    request = urllib.request.Request(u, headers=header, data=json_info)
    response = urllib.request.urlopen(request)
    f = response.read().decode("utf8")
    return json.loads(f)
# {'count': 3458840096, '_shards': {'total': 210, 'successful': 210, 'skipped': 0, 'failed': 0}}


csv_content = list()
for cj in companies:
    url = 'http://117.144.106.34:5601/api/console/proxy?path=%2F{}_sh{}%2F_count&method=POST'.format(cj, yesterday)
    # print(url)
    for status in query_curl.keys():
        my_form = {
            "query": query_curl[status]
        }
        dict_tmp = requ_post(url, my_form)
        csv_content.append(dict_tmp['count'])

print(csv_content)


oldWb = xlrd.open_workbook(filename)
table = oldWb.sheet_by_name("Sheet1")
n_rows = table.nrows     # number of rows
if n_rows > 0:
    n_columns = len(table.row_values(0))    # number of columns
else:
    n_columns = 0

newWb = copy(oldWb)     # 复制
newWs = newWb.get_sheet(0)  # 取sheet表

for i, item in enumerate(csv_content):
    newWs.write(max(n_rows-1, 0), n_columns + i, item)
newWb.save(filename)    # 保存至result路径


