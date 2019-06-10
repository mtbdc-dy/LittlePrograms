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
"""

import web.webCrawler.webcrawler as ww
import datetime
from lxml import etree  # 爬取页面元素
import csv


now = datetime.datetime.now()
start_time = '2019-05-01'
# end_time = '2018-06-01'
end_time = now.strftime('%Y-%m-%d+%H:%M:%S')
end_time_url = now.strftime('%Y-%m-%d+%H%%3A%M%%3A%S')  # 2018-09-24+04%3A27%3A45
filename = 'eoms_complaints.csv'
g = open(filename, 'a')

row = 1
# 投诉单查询
# cookie = 'JSESSIONID=0000EXUdVeYqqO8BowhyzBRj1up:1ag9bq1lq'
cookie = 'JSESSIONID=0000_jIu_Cjo9XeURD82DCdVsZl:1ag7gqe3n'
# url = 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=performQuery'
url = 'http://10.221.246.104/eoms35/sheet/complaint/complaint.do?method=performQuery'
form = {
    'complaintType1ChoiceExpression': '',
    'customPhoneStringExpression': 'like',
    'link.operateDeptId': '',
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
    'sendTimeEndDate': '2018-11-14+00:00:00',
    'sendTimeEndDateExpression': '<=',
    'sendTimeLogicExpression': 'and',
    'sendTimeStartDate': '2018-11-13+00:00:00',
    'sendTimeStartDateExpression': '>=',
    'sendUserIdStringExpression': 'in',
    'sheetIdStringExpression': 'like',
    'showArea': '',
    'statusChoiceExpression': '',
    'task.taskName': '',
    'titleStringExpression': 'like',
    'toDeptIdStringExpression': 'in',
}
f = ww.post_web_page(url, form, cookie)
# print(f)

page = 85   # 多少页 一个月 整个省公司的投诉单

for p in range(page):
    print('第{}页:'.format(p+1))
    '''各分页url'''
    url = 'http://10.221.246.104/eoms35/sheet/complaint/complaint.do?titleStringExpression=like&sendRoleIdStringExpre' \
          'ssion=in&main.parentCorrelation=&sheetIdStringExpression=like&complaintType1ChoiceExpression=&main.sendTim' \
          'e=&operateDeptIdStringExpression=in&main.complaintType=&sendDeptIdStringExpression=in&operateUserIdStringE' \
          'xpression=in&sendUserIdStringExpression=in&parentCorrelationStringExpression=like&main.complaintType1=&que' \
          'ryType=record&main.complaintType2=&main.complaintType4=&main.sheetId=&main.complaintType5=&customPhoneStri' \
          'ngExpression=like&main.complaintType6=&main.complaintType7=&showArea=&statusChoiceExpression=&sendTimeEndD' \
          'ateExpression=%3C%3D&main.sendRoleId=&main.toDeptId=&d-4025513-p=' + str(p+1) + '&sendTimeStartDateExpress' \
          'ion=%3E%3D&sendTimeStartDate=2018-10-01+00%3A00%3A00&main.sendDeptId=&main.sendUserId=&toDeptIdStringExpre' \
          'ssion=in&main.s' \
          'tatus=&main.customPhone=&sendTimeLogicExpression=and&link.operateRoleId=&method=performQuery&main.title=&m' \
          'ethod.save=%E6%8F%90%E4%BA%A4&link.operateDeptId=&sendTimeEndDate=2018-11-13+23%3A32%3A22&link.operateUser' \
          'Id=&task.taskName=&operateRoleIdStringExpression=in'
    f = ww.get_web_page(url, cookie)
    # print(f)

    selector = etree.HTML(f)
    # 获取 当前页全部工单号
    content_tasks = selector.xpath('/html/body/div/div/div/table/tbody/tr/td[1]/a/text()')
    print(content_tasks)

    for t, item in enumerate(content_tasks):
        task_sequence = item
        # 获取 a标签
        content = selector.xpath('/html/body/div/div/div/table/tbody/tr[' + str(t+1) + ']/td[1]/a/@href')
        address = content[0]
        # print(address)
        url = 'http://10.221.246.104/eoms35/sheet/complaint/' + address
        f_detail = ww.get_web_page(url, cookie)
        # print(f_detail.find(r'>投诉内容</td>'))
        # exit()
        f_detail = f_detail[f_detail.find(r'>投诉内容</td>')+58:]
        f_detail = f_detail[:f_detail.find('<')]
        print(f_detail)
        g.write(f_detail + '\n')





