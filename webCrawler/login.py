# keep this file local, please!!!

import webCrawler.webcrawler


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
