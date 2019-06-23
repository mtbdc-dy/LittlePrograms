# -*- coding: utf-8 -*-
# keep this file local, please!

import time
import random
import json  # eoms用json传了RSA公钥
import rsa
import base64
import ssl
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import web.webCrawler.webcrawler as ww
import myPackages.number_base_conversion
import myPackages.pic_processing as mp
import myPackages.getime as md
import requests
import datetime
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

"""
"""


# 认证过程一般是 先去网站获取一个cookie 然后用账号密码认证这个cookie
def login_wangluoquanjingkeshihua():
    cookie = 'ERROR'
    url = 'https://117.136.129.122/cmnet/index.htm'
    cj = ww.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)
    # cookie = 'JSESSIONID=3276F5B76C95383468C71976890DF58C'
    date = int(time.time()*1000)
    temp = myPackages.number_base_conversion.base_n(date, 36)
    url = 'https://117.136.129.122/cmnet/validateCode.htm?temp=' + temp
    ww.get_validate_code(url, cookie)

    url = 'https://117.136.129.122/cmnet/login.htm'

    pwd = input('输入验证码，谢谢')
    form = {
        'username': r'Xw1OfZDqN27WleNrhSAYAQ==',
        'password': r'gS4MY8BMAeRRfMVQswEVWA==',
        'exPassword': pwd
    }
    ww.post_web_page_ssl(url, form, cookie)

    return cookie


def zte_cdn_omc():
    cookie = 'ERROR'
    url = 'https://39.134.88.198:8443/frame/loginOut.action'
    cj = ww.get_cookie_without_form(url)  # 这个函数默认输出结果
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

    # cookie = 'JSESSIONID=4CD5A39212EAA84F77E3BE9817B6AC09'
    # url = 'https://39.134.88.198:8443/authimg'
    # ww.get_validate_code(url, cookie)

    url = 'https://39.134.88.198:8443/frame/login.action'

    # pwd = input('输入验证码，谢谢')

    form = {
        'authCodeable': 'false',
        'password': 'p2K8/TkfsQ6hpdE0h+JaZA==',
        'userName': 'llz',
        # 'validateCode': pwd
    }

    ww.post_web_page_ssl(url, form, cookie)

    return cookie


def zte_anyservice_uniportal_v2():
    cookie = 'ERROR'
    url = 'https://117.135.56.61:8443/frame/loginOut.action'
    cj = ww.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    # print(cookie)
    url = 'https://117.135.56.61:8443/frame/login.action'
    form = {
        'authCodeable': 'false',
        'password': 'p2K8/TkfsQ6hpdE0h+JaZA==',
        'userName': 'llz'
    }
    ww.post_web_page_ssl(url, form, cookie)
    return cookie


def sqm():
    cookie = 'ERROR'
    # 获取cookie
    url = 'http://106.14.197.84:65009/evqmaster/CheckCode'
    cj = ww.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

    # 获取验证码 加random 是为了改一下请求 那样就不会去缓存中获取这张图片了
    url = 'http://106.14.197.84:65009/evqmaster/CheckCode?' + str(random.random())
    ww.get_validate_code(url, cookie)
    pwd = input('输入验证码，谢谢')

    # 提交登入表单
    url = 'http://106.14.197.84:65009/evqmaster/configaction!login.action'
    form = {
        'username': 'xuyuan',
        'password': '2EF60361839CBA359266E62F16E21A7A',
        'checkcode': pwd
    }

    f = ww.post_web_page(url, form, cookie)
    print(f)
    return cookie


def sqm_117():
    # 获取cookie
    url = 'http://117.144.107.165:8088/evqmaster/CheckCode'
    cj = ww.get_cookie_without_form(url)
    cookie = ''
    for item in cj:
        cookie = item.name + '=' + item.value
    # print(cookie)
    # cookie = 'JSESSIONID=859D1BE9728F46E71C2B765186B593A1'

    # 获取验证码 加random 是为了改一下请求 那样就不会去缓存中获取这张图片了
    url = 'http://117.144.107.165:8088/evqmaster/CheckCode?' + str(random.random())
    ww.get_validate_code(url, cookie)
    pwd = input('输入验证码，谢谢')

    # 提交登入表单
    url = 'http://117.144.107.165:8088/evqmaster/configaction!login.action'
    form = {
        'username': 'xuyuan',
        'password': '2EF60361839CBA359266E62F16E21A7A',
        'checkcode': pwd
    }
    # print('sqm117', url, form, cookie)
    ww.post_web_page(url, form, cookie)
    return cookie


def sqm_10():
    # 获取cookie
    url = 'http://10.222.4.87:8088/evqmaster/CheckCode'
    cj = ww.get_cookie_without_form(url)
    cookie = ''
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)
    # cookie = 'JSESSIONID=859D1BE9728F46E71C2B765186B593A1'

    # 获取验证码 加random 是为了改一下请求 那样就不会去缓存中获取这张图片了
    url = 'http://10.222.4.87:8088/evqmaster/CheckCode?' + str(random.random())
    ww.get_validate_code(url, cookie)
    pwd = input('输入验证码，谢谢')

    # 提交登入表单
    url = 'http://10.222.4.87:8088/evqmaster/configaction!login.action'
    form = {
        'username': 'xuyuan',
        'password': '2EF60361839CBA359266E62F16E21A7A',
        'checkcode': pwd
    }

    ww.post_web_page(url, form, cookie)
    return cookie


def sqm_117_auto_recognize_captcha():
    cookie = 'ERROR'
    # 获取cookie
    url = 'http://117.144.107.165:8088/evqmaster/CheckCode'
    cj = ww.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

    # 获取验证码 加random 是为了改一下请求 那样就不会去缓存中获取这张图片了
    url = 'http://117.144.107.165:8088/evqmaster/CheckCode?' + str(random.random())
    im = ww.return_validate_code(url, cookie)
    captcha = mp.recognize_sqm_captcha(mp.cut_sqm_captcha(im))
    exit()
    pwd = input('输入验证码，谢谢')

    # 提交登入表单
    url = 'http://117.144.107.165:8088/evqmaster/configaction!login.action'
    form = {
        'username': 'xuyuan',
        'password': '2EF60361839CBA359266E62F16E21A7A',
        'checkcode': pwd
    }

    f = ww.post_web_page(url, form, cookie)
    print(f)
    return cookie


def eoms():
    cookie = 'JSESSIONID=0000YNYvzX_gIZNkQSGA5sGoxIq:1ag7gpqb9'
    # 获取rsa公钥对账户和密码进行加密
    id = 'pdsjdlz'
    pw = '2w1q#E$R'
    url = 'http://10.221.246.100/eoms35/RSAKey'
    form = {
        '_': '',
        '?rflags': str(int(time.time()*1000))
    }
    f = ww.post_web_page(url, form, cookie)
    f_dict = json.loads(f)
    m = int(f_dict['m'], 16)
    e = int(f_dict['e'], 16)
    print(e, m)
    id_rsa = base64.b64encode(rsa.encrypt(id.encode(), rsa.key.PublicKey(m, e)))
    pw_rsa = base64.b64encode(rsa.encrypt(pw.encode(), rsa.key.PublicKey(m, e)))
    print(id_rsa)
    print(pw_rsa)

    # 获取验证码
    url = 'http://10.221.246.100/eoms35/imageCode.jsp'
    ww.get_validate_code(url, cookie)
    pwd = input('输入验证码，谢谢')

    # 提交登录表单
    url = 'http://10.221.246.100/eoms35/index.do?method=saveSession&app=app'
    form = {
        'j_code': pwd,
        'j_password': pw_rsa,
        'j_username': id_rsa,
        'login': '登录'
    }
    f = ww.post_web_page(url, form, cookie)
    print(f)
    return cookie


def utm():
    driver = Chrome()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(5)
    driver.get("https://39.134.87.216:31943/pm/themes/default/pm/app/i2000_monitorView_pm.html?curMenuId=com.iemp.app.pm.monitorView&_=1545967221368#group_152734715982719")
    # print(driver.page_source)
    usr = driver.find_element_by_xpath("//*[@id=\"username\"]")
    usr.send_keys("admin")
    pw = driver.find_element_by_xpath("//*[@id=\"password\"]")
    pw.send_keys("HuaWei12#$")

    input('Press Enter to continue...')
    # captcha = driver.find_element_by_xpath("//*[@id=\"validate\"]")
    # vc = input('输入网页上的验证码')
    # captcha.send_keys(vc)
    # captcha.send_keys(Keys.RETURN)
    # time.sleep(1)

    # action = ActionChains(driver)
    # action.send_keys(Keys.ESCAPE)
    # print(2)
    # try:
    #     action.perform()
    # except TimeoutException:
    #     print('time out')
    # # action.perform()
    # print(3)

    # button = driver.find_element_by_css_selector('#treeDiv_1_switch')
    # button.click()
    # print(driver.get_cookies())
    cookie = ''
    for item in driver.get_cookies():
        # print(item)
        if item['name'] == 'JSESSIONID':
            cookie = 'JSESSIONID=' + item['value']
    # print(cookie)
    driver.close()
    driver.quit()
    return cookie


def fonsview():
    driver = Chrome()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(5)
    driver.get('https://sh.csk.rhel.cc:3000/login')
    # print(driver.page_source)
    usr = driver.find_element_by_xpath("//*[@id=\"login-view\"]/form/div[1]/input")
    usr.send_keys("fonsview")
    pw = driver.find_element_by_xpath("//*[@id=\"inputPassword\"]")
    pw.send_keys("ShangHai!23+")
    pw.send_keys(Keys.ENTER)
    time.sleep(2)

    # 地市入流量
    driver.find_element_by_xpath("/html").send_keys('s', 'o')
    pw = driver.find_element_by_xpath('/html/body/grafana-app/dashboard-search/div[2]/div[2]/div[1]/div/div[1]/dashboard-search-results/div[1]/div[3]/a/span[2]/div')
    pw.click()

    # 点击时间面板
    pw = driver.find_element_by_xpath('/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/gf-time-picker/div/button[1]/span[1]')
    pw.click()
    # 点击昨天
    pw = driver.find_element_by_xpath('/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/gf-time-picker/div[2]/div[1]/div[2]/ul[2]/li[1]/a')
    pw.click()
    time.sleep(1)

    # 取数据
    pw = driver.find_element_by_xpath('//*[@id="panel-1"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]')
    fx = pw.text.split(' ')[0]
    pw = driver.find_element_by_xpath('//*[@id="panel-17"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]')
    yp = pw.text.split(' ')[0]
    pw = driver.find_element_by_xpath('//*[@id="panel-16"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]')
    fh_hz = pw.text.split(' ')[0]
    pw = driver.find_element_by_xpath('//*[@id="panel-16"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]')
    fh_mean_hz = pw.text.split(' ')[0]

    print('峰值:', fh_hz)
    print('均值:', fh_mean_hz)
    time.sleep(1)
    driver.close()
    # driver.close()
    # driver.quit()
    return float(fx)/1.074, float(yp)/1.074, float(fh_hz)/1.074, float(fh_mean_hz)/1.074


# 这个废了
def fonsview_mean(nd, ndb):
    driver = Chrome()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(5)
    driver.get('https://sh.csk.rhel.cc:3000/login')
    # print(driver.page_source)
    usr = driver.find_element_by_xpath("//*[@id=\"login-view\"]/form/div[1]/input")
    usr.send_keys("fonsview")
    pw = driver.find_element_by_xpath("//*[@id=\"inputPassword\"]")
    pw.send_keys("ShangHai!23+")
    pw.send_keys(Keys.ENTER)

    pw = driver.find_element_by_xpath('/html/body/grafana-app/div[2]/div/div/div/dashnav/div/div[1]/a')
    pw.click()
    pw = driver.find_element_by_xpath(
        '/html/body/grafana-app/div[2]/div/div/div/dashnav/dashboard-search/div[2]/div[2]/div[1]/div/div[1]/dashboard-search-results/div[8]/div[1]/span')
    pw.click()
    pw = driver.find_element_by_xpath(
        '/html/body/grafana-app/div[2]/div/div/div/dashnav/dashboard-search/div[2]/div[2]/div[1]/div/div[1]/dashboard-search-results/div[8]/div[3]/a[2]/span[2]')
    pw.click()

    pw = driver.find_element_by_xpath(
        '/html/body/grafana-app/div[2]/div/div/div/dashnav/div/gf-time-picker/div/button[1]')
    pw.click()

    # 选择日期
    start_time = str(md.n_days_ago(ndb + 1))
    end_time = str(md.n_days_ago(ndb))
    print(start_time, end_time)
    pw = driver.find_element_by_xpath('/html/body/grafana-app/div[2]/div/div/div/dashnav/div/gf-time-picker/div[2]/form/div[1]/div[1]/input')
    for i in range(10):
        pw.send_keys(Keys.BACKSPACE)
    pw.send_keys(start_time + " 00:00:00")
    pw = driver.find_element_by_xpath('/html/body/grafana-app/div[2]/div/div/div/dashnav/div/gf-time-picker/div[2]/form/div[2]/div[1]/input')
    for i in range(10):
        pw.send_keys(Keys.BACKSPACE)
    pw.send_keys(end_time + " 00:00:00")
    pw = driver.find_element_by_xpath('/html/body/grafana-app/div[2]/div/div/div/dashnav/div/gf-time-picker/div[2]/form/div[3]/div[2]/button')
    pw.click()
    time.sleep(1)

    fh_hz_mean = list()
    for i in range(nd):
        # 下一天
        pw = driver.find_element_by_xpath('/html/body/grafana-app/div[2]/div/div/div/dashnav/div/gf-time-picker/div/button[3]')
        pw.click()
        time.sleep(1)
        pw.click()
        time.sleep(1)

        # 取值
        pw = driver.find_element_by_xpath('//*[@id="panel-16"]/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[2]/div/div[1]/tbody/div[1]/div[4]')
        fh_hz_mean.append(float(pw.text.split(' ')[0]))
    print(fh_hz_mean)
    print(sum(fh_hz_mean)/len(fh_hz_mean))
    driver.close()

    return sum(fh_hz_mean)/len(fh_hz_mean)


# 太烦了懒得写
def fonsview_demo():
    url = 'https://sh.csk.rhel.cc:3000/api/token'
    context = ssl._create_unverified_context()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'secret': 'pby7izcdgr'
    }
    proxy = {
        'http': 'http://cmnet:cmnet@211.136.113.69:808'
    }
    # 挂代理Handler
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    # 伪装浏览器申请
    request = urllib.request.Request(url[0], headers=header)
    # 读取页面
    response = urllib.request.urlopen(request, context=context)
    f = response.read().decode("utf8")
    time.sleep(random.randint(0, 1))



    url = 'https://sh.csk.rhel.cc:3000/login'
    form = {
        "password": "da9ffe54b2df76cf-fc441c7bec2bee8c4041da7e-1b42ecb96ff1eec4bb2ef085246ce09d5e985ab6fc60ce5ffe96c39d",
        "email": "",
        "user": "fonsview"
    }
    cj = ww.get_cookie(form, url, '')
    print(cj)
    exit()

    url = 'https://sh.csk.rhel.cc:3000/api/datasources/proxy/1/api/v1/query_range?query=sum(irate(node_network_transmit_bytes_total%7Bdevice%3D~%22e.*%22%7D%5B5m%5D))%20%20*%208&start=1552838400&end=1553154300&step=300'


    f = ww.get_web_page_ssl(url, 'grafana_session=dcd02f6093d59dc24866378ef57b32aa')
    print(f)

    return


# ELK
def elk():
    url = 'https://117.144.106.34:5601/api/v1/auth/login'
    ssl._create_default_https_context = ssl._create_unverified_context      # 信任所有证书
    header = {
        # 'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '54',
        # 'Content-Type': 'application/json;charset=utf-8',
        # 'Host': '117.144.106.34:5601',
        'kbn-version': '6.6.1',
        # 'Pragma': 'no-cache',
        # 'Referer': 'https://117.144.106.34:5601/login?type=basicauthLogout',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    form = {
        'password': 'Cl0lTaULdjw0uVcH4S1N',
        'username': 'admin'
    }
    post_data = urllib.parse.urlencode(form).encode('utf8')
    request = urllib.request.Request(url, post_data, headers=header)
    # 获取Cookie
    cj = http.cookiejar.CookieJar()
    opener_cookie = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener_cookie.open(request)
    # print(cj)
    cookie = ''
    for i, item in enumerate(cj):
        if i == 0:
            cookie = item.name + '=' + item.value
        else:
            cookie = cookie + '; ' + item.name + '=' + item.value
    print(cookie)
    return cookie


if __name__ == '__main__':
    print(sqm_117())
    print()







