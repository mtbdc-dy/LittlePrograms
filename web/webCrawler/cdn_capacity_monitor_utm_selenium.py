import web.webCrawler.login as wl
import web.webCrawler.webcrawler as ww
import urllib.request
import urllib.parse
import time
import json
import random
import urllib.error
import ssl



cookie = wl.utm()
# cookie = 'JSESSIONID=d63fee9db18bbeafba5c0b2378c96cc10b9ded22cc8832d9'
url = 'https://39.134.87.216:31943/rest/framework/random?_=1546344328109'

roarand = ww.get_web_page_ssl(url, cookie)


def post_ssl(url, my_form):
    # ssl._create_default_https_context = ssl.create_unverified_context
    context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'roarand': roarand,
        'Cookie': cookie
    }

    proxy = {
        'http': 'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请

    request = urllib.request.Request(url, headers=header)
    # 编码
    # form_data = urllib.parse.urlencode(my_form).encode('utf8')
    form_data = my_form
    # 读取页面
    response = urllib.request.urlopen(request, data=form_data, context=context)  # context=context

    f = response.read().decode("utf8")
    time.sleep(random.randint(0, 1))
    return f


url = 'https://39.134.87.216:31943/rest/pm/history'
form = b'param=%7B%22pageIndex%22%3A1%2C%22historyTimeRange%22%3A24%2C%22beginTime%22%3A1546345580251%2C%22endTime%22%3A1546345580251%2C%22isGetGraphicGroupData%22%3Atrue%2C%22isMonitorView%22%3Atrue%2C%22mo2Index%22%3A%22%5B%7B%5C%22dn%5C%22%3A%5C%22com.huawei.hvs.pop%3D2101535%5C%22%2C%5C%22indexId%5C%22%3A%5C%2211735%5C%22%2C%5C%22displayValue%5C%22%3A%5C%22%5C%22%2C%5C%22aggrType%5C%22%3A2%7D%5D%22%7D'
f = post_ssl(url, form)
# print(f)
huawei_dict = json.loads(f)
huawei_list = huawei_dict['result']['groupQueryData'][0][0]['indexValues']
print(huawei_list)
HW_FX_ott_rate = list()

for item in huawei_list:
    HW_FX_ott_rate.append(float(item['indexValue']))
print(max(HW_FX_ott_rate))



url = 'https://39.134.87.216:31943/rest/pm/history'
form = b'param=%7B%22pageIndex%22%3A1%2C%22historyTimeRange%22%3A24%2C%22beginTime%22%3A1546347937220%2C%22endTime%22%3A1546347937220%2C%22isGetGraphicGroupData%22%3Atrue%2C%22isMonitorView%22%3Atrue%2C%22mo2Index%22%3A%22%5B%7B%5C%22dn%5C%22%3A%5C%22com.huawei.hvs.pop%3D2101531%5C%22%2C%5C%22indexId%5C%22%3A%5C%2211735%5C%22%2C%5C%22displayValue%5C%22%3A%5C%22%5C%22%2C%5C%22aggrType%5C%22%3A2%7D%5D%22%7D'
f = post_ssl(url, form)
# print(f)
huawei_dict = json.loads(f)
huawei_list = huawei_dict['result']['groupQueryData'][0][0]['indexValues']
print(huawei_list)
HW_FX_ott_rate = list()

for item in huawei_list:
    HW_FX_ott_rate.append(float(item['indexValue']))
print(max(HW_FX_ott_rate))