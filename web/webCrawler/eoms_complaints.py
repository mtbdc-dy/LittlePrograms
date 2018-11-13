# -*- coding: utf-8 -*-

import re
import urllib
import urllib.parse
import xlrd
import xlwt
import sys
import web.webCrawler.login
import web.webCrawler.webcrawler as ww
import myPackages.getime
import datetime
import csv
from lxml import etree  # 爬取页面元素


'''下面表单里和后面url里的时间可能需要手动修改'''
now = datetime.datetime.now()
start_time = '2018-09-01'
# end_time = '2018-10-28'
end_time = now.strftime('%Y-%m-%d+%H:%M:%S')
end_time_url = now.strftime('%Y-%m-%d+%H%%3A%M%%3A%S')  # 2018-09-24+04%3A27%3A45
filename = 'eoms_complaints.txt'
g = open(filename, 'w')


row = 1
# """
# 爬eoms
# cookie看起来是不会变的，但是每个电脑又有不同，也不知道他在哪里生成的
# """
#
# cookie = web.webCrawler.login.eoms()
#
# # 通用任务工单分支菜单
# url = 'http://10.221.246.100/eoms35/xtree.do?method=nav'
# form = {
#     'node':	'1007'
# }
# f = ww.post_web_page(url, form, cookie)
# # print(f)
#
# # 工单查询表单
# """
# 这里post时还是之前的cookie
# get页面的时候突然换了个cookie，不是很懂
# """
# url = 'http://10.221.246.100/eoms35/log/tawCommonLogOperators.do?method=saveLog'
# form = {
#     'href': 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=showQueryPage&amp;type=interface&amp;interface=interface&amp;userName=pdsjdlz',
#     'id': '100706',
#     'text':	"工单查询"
# }
# ww.post_web_page(url, form, cookie)
#
# cookie = 'JSESSIONID=0000DUlWKdFqa7ob9tuvNPqBMId:1ag9kvec7'
# url = 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=showQueryPage&type=interface&interface=interface&userName=pdsjdlz'
# f = ww.get_web_page(url, cookie)
# # print(f)

# 任务单查询
# cookie = 'JSESSIONID=0000UtivNKgIKyywfLHVuIypbDj:1ag9bqcd9'
cookie = 'JSESSIONID=0000EXUdVeYqqO8BowhyzBRj1up:1ag9bq1lq'
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







