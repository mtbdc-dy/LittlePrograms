import time
import xlrd
import random
import urllib.error
import ssl
import webCrawler.login
import webCrawler.webcrawler
import myPackages.mailtools
import myPackages.getime
import csv


cookie = webCrawler.login.eoms()
url = 'http://10.221.246.100/eoms35/log/tawCommonLogOperators.do?method=saveLog'
form = {
        'href': 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=showQueryPage&amp;type=interface'
                '&amp;interface=interface&amp;userName=chenqi',
        'id': '100706',
        'text': '工单查询'
    }
webCrawler.webcrawler.post_web_page(url, form, cookie)

url = 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=showQueryPage&type=interface&interface=inte' \
    'rface&userName=chenqi'
f = webCrawler.webcrawler.get_web_page(url, cookie)
# print(f)

url = 'http://10.221.246.108/eoms35/sheet/commontask/commontask.do?method=performQuery'
form = {
    'sheetIdStringExpression': 'like',
    'main.sheetId': '',
    'titleStringExpression': 'like',
    'main.title': '关于配合市场部',
    'main.status': '',
    'statusChoiceExpression': '',
    'task.taskName': '',
    'sendRoleIdStringExpression': 'in',
     'main.sendRoleId': '',
    'sendDeptIdStringExpression': 'in',
    'main.sendDeptId': '2',
    'sendUserIdStringExpression': 'in',
    'main.sendUserId': '',
    'operateRoleIdStringExpression': 'in',
    'link.operateRoleId': '',
    'operateDeptIdStringExpression': 'in',
    'link.operateDeptId': '',
    'operateUserIdStringExpression': 'in',
    'link.operateUserId': '',
    'main.mainNetSort1': '',
    'mainNetSort1ChoiceExpression': '',
    'main.mainNetSort2': '',
    'main.mainNetSort3': '',
    'main.sendTime': '',
     'sendTimeStartDateExpression': '>=',
    'sendTimeStartDate': '2016-06-01 00:00:00',
    'sendTimeLogicExpression': 'and',
    'sendTimeEndDateExpression': '<=',
    'sendTimeEndDate': myPackages.getime.current_time(),
    'queryType': 'record',
    'method.save': '提交'
}
# cookie = 'JSESSIONID=00005Gi_xISqNmdw8ESz94RZ2e-:1ag9kv0ln'
f = webCrawler.webcrawler.post_web_page(url, form, cookie)
# print(f)

# for i in range(15):

index = f.find('<td><a  href=\'')
f = f[index+14:]

index_end = f.find('\'')
s = f[:index_end]
print(s)

url = 'http://10.221.246.108/eoms35/sheet/commontask/' + s

f = webCrawler.webcrawler.get_web_page(url, cookie)
# print(f)

url = 'http://10.221.246.108/eoms35/accessories/tawCommonsAccessoriesConfigs/download/id-8a5d76ed65b03c320165c142ffe81ace/filelist-\'201809101015179816.xlsx\''
f = webCrawler.webcrawler.download_web_page(url, cookie)
print(f)
g = open('eoms.xlsx', 'wb')
g.write(f)
g.close()
