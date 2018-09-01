# keep this file local, please!!!

import webCrawler.webcrawler
import random
import myPackages.number_base_conversion
import time


# 认证过程一般是 先去网站获取一个cookie 然后用账号密码认证这个cookie
def login_wangluoquanjingkeshihua():
    url = 'https://117.136.129.122/cmnet/index.htm'
    cj = webCrawler.webcrawler.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)
    # cookie = 'JSESSIONID=3276F5B76C95383468C71976890DF58C'
    date = int(time.time()*1000)
    temp = myPackages.number_base_conversion.base_n(date, 36)
    url = 'https://117.136.129.122/cmnet/validateCode.htm?temp=' + temp
    webCrawler.webcrawler.get_validate_code(url, cookie)

    url = 'https://117.136.129.122/cmnet/login.htm'

    pwd = input('输入验证码，谢谢')
    form = {
        'username': 'Xw1OfZDqN27WleNrhSAYAQ==',
        'password': 'gS4MY8BMAeRRfMVQswEVWA==',
        'exPassword': pwd
    }
    webCrawler.webcrawler.post_web_page_ssl(url, form, cookie)

    return cookie


def zte_anyservice_uniportal():
    url = 'https://117.135.56.61:8443/frame/loginOut.action'
    cj = webCrawler.webcrawler.get_cookie_without_form(url) # 这个函数默认输出结果
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

        # cookie = 'JSESSIONID=3276F5B76C95383468C71976890DF58C'
    url = 'https://117.135.56.61:8443/authimg'
    webCrawler.webcrawler.get_validate_code(url, cookie)

    url = 'https://117.135.56.61:8443/frame/login.action'

    pwd = input('输入验证码，谢谢')
    # 字段没匹配
    # 字段没匹配
    # 字段没匹配

    form = {
        'authCodeable': 'false',
        'password': 'tgNxV4VE9BlKZXt1G6f9CQ==',
        'userName': 'super',
        'validateCode': pwd
    }

    webCrawler.webcrawler.post_web_page_ssl(url, form, cookie)

    return cookie


def sqm():
    # 获取cookie
    url = 'http://106.14.197.84:65009/evqmaster/CheckCode'
    cj = webCrawler.webcrawler.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

    # 获取验证码 加random 是为了改一下请求 那样就不会去缓存中获取这张图片了
    url = 'http://106.14.197.84:65009/evqmaster/CheckCode?' + str(random.random())
    webCrawler.webcrawler.get_validate_code(url, cookie)
    pwd = input('输入验证码，谢谢')

    # 提交登入表单
    url = 'http://106.14.197.84:65009/evqmaster/configaction!login.action'
    form = {
        'username': 'xuyuan',
        'password': '2EF60361839CBA359266E62F16E21A7A',
        'checkcode': pwd
    }

    f = webCrawler.webcrawler.post_web_page(url, form, cookie)
    print(f)
    return cookie



