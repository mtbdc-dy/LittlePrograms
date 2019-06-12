# -*- coding: utf-8 -*-
# @Time : 2019-06-10 21:56
# @Author : 徐缘
# @FileName: eoms_complaints_work_sheet.py
# @Software: PyCharm

"""
主要是用于爬取个人投诉单的内容，作为NLP训练的数据。
0： IT
1： CDN
2： 短信
3： wLAN

按天来查吧，这样分步式查询，万一中断了会比较方便
"""

import web.webCrawler.webcrawler as ww
import datetime
from bs4 import BeautifulSoup
import csv
import re


# 找到流转信息按钮的URL
def get_liuzhuanxinxi_url(text):
    text = text[text.find('流转信息') + 19:]
    # print(text)
    return text[:text.find('\'')]


filename = 'eoms_complaints.csv'

g = open(filename, 'a')
writer = csv.writer(g)
now = datetime.datetime.now()
start_time = '2019-05-01'
# end_time = '2018-06-01'
end_time = now.strftime('%Y-%m-%d+%H:%M:%S')
end_time_url = now.strftime('%Y-%m-%d+%H%%3A%M%%3A%S')  # 2018-09-24+04%3A27%3A45


# 投诉单查询
# cookie = 'JSESSIONID=0000EXUdVeYqqO8BowhyzBRj1up:1ag9bq1lq'
cookie = 'JSESSIONID=00000sfqnlUlvDf7v2hGDNHpm4Y:1ag9bqcd9'
url = 'http://10.221.246.104/eoms35/sheet/complaint/complaint.do?method=performQuery'
form = {
    'complaintType1ChoiceExpression': '',
    'customPhoneStringExpression': 'like',
    'link.operateDeptId': '10223',
    'link.operateRoleId': '',
    'link.operateUserId': '',
    'main.complaintType': '',
    'main.complaintType1': '',
    'main.complaintType2': '',
    'main.complaintType4': '',
    'main.complaintType5': '',
    'main.complaintType6': '',
    'main.complaintType7': '',
    'main.customPhone': '',
    'main.parentCorrelation': '',
    'main.sendDeptId': '',
    'main.sendRoleId': '',
    'main.sendTime': '',
    'main.sendUserId': '',
    'main.sheetId': '',
    'main.status': '',
    'main.title': '',
    'main.toDeptId': '',
    'method.save': '提交',
    'operateDeptIdStringExpression': 'in',
    'operateRoleIdStringExpression': 'in',
    'operateUserIdStringExpression': 'in',
    'parentCorrelationStringExpression': 'like',
    'queryType': 'record',
    'sendDeptIdStringExpression': 'in',
    'sendRoleIdStringExpression': 'in',
    'sendTimeEndDate': '2019-06-11+00:00:00',
    'sendTimeEndDateExpression': '<=',
    'sendTimeLogicExpression': 'and',
    'sendTimeStartDate': '2019-6-10+00:00:00',
    'sendTimeStartDateExpression': '>=',
    'sendUserIdStringExpression': 'in',
    'sheetIdStringExpression': 'like',
    'showArea': '',
    'statusChoiceExpression': '1',
    'task.taskName': '',
    'titleStringExpression': 'like',
    'toDeptIdStringExpression': 'in',
}
f = ww.post_web_page(url, form, cookie)
# print(f)
soup = BeautifulSoup(f, "html.parser")
# print(soup.prettify())  # 这很beautiful

# 共 13 条记录。 如果大于15条还要分页处理。首先要提取出数字
num_complaints = soup.find(attrs={'class': 'pagebanner'}).get_text()    # 查询得到的投诉条数
num_complaints = re.sub("\D", "", num_complaints)
num_complaints = int(num_complaints)
# print(num_complaints)

if num_complaints == 0:
    print('怎么这天连个投诉都没？')
    exit()

if num_complaints <= 15:
    tmp_csv_content = list()

    for i, table_rows in enumerate(soup.find('tbody').find_all('tr')):
        table_colums = table_rows.find_all('td')[0]
        sheet_number = table_colums.find('a').get_text().strip()
        print(sheet_number)
        address = table_colums.find('a').get('href')
        tmp_csv_content.append([table_colums.find('a').get_text().strip()])
        # 'http://10.221.246.104/eoms35/sheet/complaint/complaint.do?method=showMainDetailPage&sheetKey=8a5d76eb6b09603c016b465b60442261'
        url = 'http://10.221.246.104/eoms35/sheet/complaint/' + address
        f = ww.get_web_page(url, cookie)
        # print(f)
        soup = BeautifulSoup(f, "html.parser")
        title = soup.find_all('table')[0].find_all('tr')[1].find_all('td')[1].get_text().strip()
        print(title)
        tmp_csv_content[i].append(title)
        content = soup.find_all('table')[2].find_all('tr')[13].find_all('td')[1].get_text().strip()
        print(content)
        tmp_csv_content[i].append(content)
        note = soup.find_all('table')[2].find_all('tr')[15].find_all('td')[1].get_text().strip()
        print(note)
        tmp_csv_content[i].append(note)

        # 流转信息
        url = 'http://10.221.246.104/eoms35/sheet/complaint/' + get_liuzhuanxinxi_url(f)
        print(url)
        f = ww.get_web_page(url, cookie)
        # print(f)
        soup = BeautifulSoup(f, "html.parser")
        # print(soup.find('div').find_all('div', recursive=False)[3].prettify())
        if sheet_number == 'SH-052-190610-00136':
            print(soup.prettify())
        chenqi = ''
        other = ''
        for k, item in enumerate(soup.find('div').find_all('div', recursive=False)[3].find_all(attrs={'class': 'history-item-title'})):
            operator = None
            if '处理完成' in item.get_text():
                next_sb = item.find_next_sibling(attrs={'class': 'history-item-content hide'})
                for rows in next_sb.find_all('td'):
                    news = rows.get_text().strip()
                    # print(news)
                    if '操作人' == news:
                        print('操作人', rows.find_next_sibling('td').get_text().strip())
                        operator = rows.find_next_sibling('td').get_text().strip()

                    if '处理结果描述' in rows.get_text():
                        print('处理结果描述', rows.find_next_sibling('td').get_text().strip())
                        result = rows.find_next_sibling('td').get_text().strip()

                        if operator and operator != '陈琦':
                            if other == '':
                                other = operator + ': ' + result
                            else:
                                other = other + '\n' + operator + ': ' + result

                        if operator and operator == '陈琦':
                            if chenqi == '':
                                chenqi = operator + ': ' + result
                            else:
                                chenqi = chenqi + '\n' + operator + ': ' + result

        tmp_csv_content[i].append(other)
        tmp_csv_content[i].append(chenqi)

    # print(tmp_csv_content)
    writer.writerows(tmp_csv_content)













