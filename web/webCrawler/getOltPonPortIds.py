# coding:utf-8
import time
import http.cookiejar
import csv
import codecs
import random
import urllib.error


'''
这个网站已经下线了
NOTE1 使用代理
NOTE2 输入为CSV文件第二列可调
NOTE3 查询频率可调
'''


# 第一步 尝试登入
url = 'http://10.221.154.141:20111/irm/login!doLogin.html?needDecode=true'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',  # 代表接受压缩文件
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
    'Host': '10.221.154.141:20111',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'http://10.221.154.141:20111/irm/login.html',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=w8avf8CrIJS3uwuqYvb9QjQWKb7Bj07T9pPNgBwst07jJhpVXZDi!1669067924',
    # 'Referer' 可能需要
    'Proxy-Authorization': 'Basic Y21uZXQ6Y21uZXQ=',
    'Proxy-Connection': 'keep-alive',
}
# 账号信息
my_post = {
    'username': 'sjpz_zx',
    'password': 'lotTJLMRBDtpHFKMPyt4nA==',
    'forceLogin': 'false'
    }
post_data = urllib.parse.urlencode(my_post).encode('utf8')
proxy = {
    'http': 'http://cmnet:cmnet@211.136.113.69:808'
}
# 挂代理Handler
proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
# 伪装浏览器申请
request = urllib.request.Request(url, post_data, headers=header, origin_req_host='http://10.221.154.141:20111')
# 获取Cookie
cj = http.cookiejar.CookieJar()
opener_cookie = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener_cookie.open(request)
time.sleep(5)
# 修改header
for item in cj:
    header['Cookie'] = item.name + '=' + item.value + '; ' + header['Cookie']
    # print('Name = ' + item.name)
    # print('Value = ' + item.value)
    print(header['Cookie'])
# print(r.read().decode('utf-8'))


# 第二步，爬取信息
url_2 = 'http://10.221.154.141:20111/irm/inventoryGridPage!queryData.html?gridPageId=11488'
my_form = {
    'start': '0',
    'limit': '20',
    'field_specialtyTypeId': '57',
    'field_entityTypeId': '85010',
    'field_specialtyTypeCode': 'Pon',
    'field_specialtyTypeName': 'PON',
    'field_nodeName': 'PON通道',
    'field_nodeCode': 'PonChannel',
    'field_modelId': '85010',
    'field_gridPageId': '11488',
    'count': '0',
    'field_mobile': '13917056789',
    'ce': 'false',
    'applicationScenarioType': '0',
    'queryEntrance': '0',
    'treeCode': 'ResourceMaintenanceTree',
    'countTotal': '13'
}

# 分区代码对应所属ONU所在分公司
dict_olt = {
    'HK': '北区分公司',  # 虹口
    'PD': '东区分公司',  # 浦东
    'BS': '宝山分公司',
    'SJ': '松江分公司',
    'CM': '崇明分公司',
    'FX': '奉贤分公司',
    'JD': '嘉定分公司',
    'JS': '金山分公司',
    'MH': '闵行分公司',
    'NH': '东区分公司',
    'QP': '青浦分公司',
    'PT': '西区分公司',
    'XH': '南区分公司',
    'JA': '西区分公司',
    'CN': '西区分公司',  # 长宁
    'YP': '北区分公司',  # 杨浦
    'HP': '南区分公司',  # 黄浦
    'LW': '南区分公司',  # 卢湾
    'ZB': '北区分公司'   # 闸北
}

# 循环爬取
filename = 'input_olt' + '.csv'
file_output = 'output_olt' + '.csv'
encoding = 'utf8'  # 设定文件编码
flag = True  # 不处理第一行
# 打开输出文件
g = open(file_output, 'w', encoding='utf8')  # utf8   gb2312
writer = csv.writer(g)
# 统计爬取时间和次数
counter_time = 0
counter_n = 0
counter_e = 0
# 打开输入文件
with codecs.open(filename, 'r', 'utf8') as f:  # utf8   gb2312
    reader = csv.reader(f)
    for row in reader:
        if flag:
            row = row + ['属地']
            writer.writerow(row)
            flag = False
            time.sleep(2)
        else:
            my_form['field_mobile'] = row[1]
            print(row[1])
            form_data = urllib.parse.urlencode(my_form).encode('utf8')
            request = urllib.request.Request(url_2, form_data, headers=header, origin_req_host='http://10.221.154.141:2'
                                                                                               '0111')
            # 发送http request
            # noinspection PyBroadException
            try:
                response = urllib.request.urlopen(request, timeout=5)
            except:
                counter_e = counter_e + 1
                print("Error Occur")
                writer.writerow(row)
            else:
                print(3)
                print(response.getcode())
                f = response.read().decode("utf8")
                counter_n = counter_n + 1
                print('n=', counter_n)
                print('counter_time=', counter_time)
                # 提取数据
                ans = f[f.find('oltPonPortId')+15:f.find('oltPonPortId')+17]
                print(ans)
                print(dict_olt[ans])
                row = row + [dict_olt[ans]]
                writer.writerow(row)
        tmp_time = random.randint(1, 2)
        counter_time = counter_time + tmp_time
        time.sleep(tmp_time)
print(counter_e)
