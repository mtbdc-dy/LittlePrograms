# keep this file local, please!!!

import web.webCrawler.webcrawler as ww
import random
import myPackages.number_base_conversion
import myPackages.pic_processing as mp
import time
import json  # eoms用json传了RSA公钥
import rsa
import base64


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


def zte_anyservice_uniportal():
    cookie = 'ERROR'
    url = 'https://117.135.56.61:8443/frame/loginOut.action'
    cj = ww.get_cookie_without_form(url)  # 这个函数默认输出结果
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

    # cookie = 'JSESSIONID=3276F5B76C95383468C71976890DF58C'
    url = 'https://117.135.56.61:8443/authimg'
    ww.get_validate_code(url, cookie)

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
        'password': 'tgNxV4VE9BlKZXt1G6f9CQ==',
        'userName': 'super'
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
    cookie = 'ERROR'
    # 获取cookie
    url = 'http://117.144.107.165:8088/evqmaster/CheckCode'
    cj = ww.get_cookie_without_form(url)
    for item in cj:
        cookie = item.name + '=' + item.value
    print(cookie)

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

    f = ww.post_web_page(url, form, cookie)
    print(f)
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
    url = 'https://39.134.87.216:31943/itpaas/login.action'
    cj = ww.get_cookie_without_form(url)
    # 4371b396e727fd23f4ddcaa2c16a90ea5b3f78df09d3997e
    # cookie = 'itpaasjsessionid=19E308B9A6AE374F4DD7E0F82711694D; session_cookie=ee3fe217-ce48-4b45-9d76-6b77e9fe40a1;' \
    #          ' bme_locale_session=zh_CN'
    cookie = ''
    for item in cj:
        cookie = cookie + item.name + '=' + item.value + ';'

    return cookie[:-1]


if __name__ == '__main__':
    sqm_117_auto_recognize_captcha()

    print()





