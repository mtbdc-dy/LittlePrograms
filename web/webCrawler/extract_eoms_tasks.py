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


workbook_write = xlwt.Workbook('tmp_emos.xlsx')
ws = workbook_write.add_sheet('sheet01')
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
cookie = 'JSESSIONID=0000DUlWKdFqa7ob9tuvNPqBMId:1ag9kvec7'
url = 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=performQuery'
form = {
    'link.operateDeptId': '',
    'link.operateRoleId': '',
    'link.operateUserId': '',
    'main.mainNetSort1': '',
    'main.mainNetSort2': '',
    'main.mainNetSort3': '',
    'main.sendDeptId': '',
    'main.sendRoleId': '',
    'main.sendTime': '',
    'main.sendUserId': '',
    'main.sheetId': '',
    'main.status': '',
    'main.title': '关于配合市场部制',
    'mainNetSort1ChoiceExpression': '',
    'method.save': '提交',
    'operateDeptIdStringExpression': 'in',
    'operateRoleIdStringExpression': 'in',
    'operateUserIdStringExpression': 'in',
    'queryType': 'record',
    'sendDeptIdStringExpression': 'in',
    'sendRoleIdStringExpression': 'in',
    'sendTimeEndDate': myPackages.getime.today(),
    'sendTimeEndDateExpression': '<=',
    'sendTimeLogicExpression': 'and',
    'sendTimeStartDate': '2016-06-01+00:00:00',
    'sendTimeStartDateExpression': '>=',
    'sendUserIdStringExpression': 'in',
    'sheetIdStringExpression': 'like',
    'statusChoiceExpression': '',
    'task.taskName': '',
    'titleStringExpression': 'like',
}
f = ww.post_web_page(url, form, cookie)
# print(f)

selector = etree.HTML(f)
# 获取 共有多少条记录
content = selector.xpath('/html/body/div[1]/div/div/span[3]/text()')
num_re = re.search('\d+', content[0])
num = num_re.group(0)
page = int(num) // 15 + 1
print('总条数:', num)
print('总页数:', page)

for p in range(page):
    print('第{}页:'.format(p+1))
    url = 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?titleStringExpression=like&sendRoleIdStringExp' \
          'ression=in&sheetIdStringExpression=like&main.sendTime=&operateDeptIdStringExpression=in&sendDeptIdStringEx' \
          'pression=in&operateUserIdStringExpression=in&sendUserIdStringExpression=in&queryType=record&main.mainNetSo' \
          'rt1=&main.mainNetSort2=&main.sheetId=&main.mainNetSort3=&statusChoiceExpression=&sendTimeEndDateExpression' \
          '=%3C%3D&main.sendRoleId=&d-4025513-p=' + str(p+1) + '&sendTimeStartDateExpression=%3E%3D&sendTimeStartDate=2016-06-26+00%3A00%3A00&main.sendDeptId=&main.sendUserId=&main.status=&mainNetSort1ChoiceExpression=&sendTimeLogicExpression=and&method=performQuery&link.operateRoleId=&main.title=%E5%85%B3%E4%BA%8E%E9%85%8D%E5%90%88%E5%B8%82%E5%9C%BA%E9%83%A8%E5%88%B6&method.save=%E6%8F%90%E4%BA%A4&link.operateDeptId=&sendTimeEndDate=2018-09-24+04%3A27%3A45&link.operateUserId=&task.taskName=&operateRoleIdStringExpression=in'
    f = ww.get_web_page(url, cookie)
    selector = etree.HTML(f)
    # 获取 当前页全部工单号
    content_tasks = selector.xpath('/html/body/div[1]/div/div/table/tbody/tr/td[2]/a/text()')
    print(content_tasks)
    for t, item in enumerate(content_tasks):
        task_sequence = item
        # 获取 a标签
        content = selector.xpath('/html/body/div[1]/div/div/table/tbody/tr[' + str(t+1) + ']/td[2]/a/@href')
        address = content[0]
        # print(address)
        # 访问详情页 只是去取excel的名字
        url = 'http://10.221.246.108/eoms35/sheet/commontask/' + address
        f_detail = ww.get_web_page(url, cookie)
        tmp_index = f_detail.find('var sheetAccessories = \"')
        if f_detail[tmp_index + 24] == '\"':
            continue
        else:
            f_detail = f_detail[tmp_index+25:]
            name_excel = f_detail[:f_detail.find('\'')]
            print('第{}条记录:'.format(t + 1), name_excel)

            # 获取excel的js
            url = 'http://10.221.246.108/eoms35/accessories/pages/view.jsp?appId=commontask&filelist=\'' + name_excel + '\'&idField=sheetAccessories&startsWith=0'
            f_excel_js = ww.get_web_page(url, cookie)
            tmp_index = f_excel_js.find('a href=\\\"')
            f_excel_js = f_excel_js[tmp_index+9:]
            address = f_excel_js[:f_excel_js.find('\\')]
            # print(address)

        # 下载excel
        url = 'http://10.221.246.108' + address
        f_excel = ww.download_web_page(url, cookie)
        # print(f_excel)
        # print(type(f_excel))
        flag = name_excel[-4:]
        # 判断附件是否为excel
        if not name_excel[-4:] == 'xlsx':
            tmp_zip = open(r'zip/' + item + '.zip', 'wb')
            tmp_zip.write(f_excel)
            tmp_zip.close()
        else:
            g = open('tmp_emos.xlsx', 'wb')
            g.write(f_excel)
            g.close()

            workbook = xlrd.open_workbook('tmp_emos.xlsx')
            booksheet = workbook.sheet_by_index(0)

            n_rows = booksheet.nrows  # 获得行数
            for i in range(1, n_rows):  #
                rows = booksheet.row_values(i)  # 行的数据放在数组里
                rows[0] = task_sequence
                for j in range(len(rows)):
                    ws.write(row, j, rows[j])
                row += 1


workbook_write.save('eoms_tasks.xls')

