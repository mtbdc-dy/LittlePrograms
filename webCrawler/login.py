# keep this file local, please!!!

import webCrawler.webcrawler
import ssl
import urllib.request


# 认证过程一般是 先去网站获取一个cookie 然后用账号密码认证这个cookie
def login_wangluoquanjingkeshihua():
    url = 'https://117.136.129.122/cmnet/index.htm'
    cj = webCrawler.webcrawler.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)
    # cookie = 'JSESSIONID=3276F5B76C95383468C71976890DF58C'
    url = 'https://117.136.129.122/cmnet/validateCode.htm?temp=jjhpxaxi'
    webCrawler.webcrawler.get_validate_code(url, cookie)

    url = 'https://117.136.129.122/cmnet/login.htm'

    pwd = input('输入验证码，谢谢')
    form = {
        'username': 'shanghai_qw',
        'password': 'sh_50331061',
        'exPwd': pwd
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

