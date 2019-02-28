import requests
from bs4 import BeautifulSoup
import warnings
import web.webCrawler.webcrawler as ww

# 忽略警告
warnings.filterwarnings("ignore")

url = 'http://users.09game.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
data = {
    'ReturnUrl': '/User',
    'LoginAccount': '13901790208',
    'Password': ')9940208!',
    'name': '登录'
}

s = requests.session()
# get请求，获取cookie,token
r = s.get(url=url, headers=headers)
cookies = dict(r.cookies)
soup = BeautifulSoup(r.text)
token = soup.find_all(type="hidden")[1]["value"]
data['__RequestVerificationToken'] = token

print(data)
print(cookies)
cookies_tmp = ''
for item in cookies.keys():
    cookies_tmp = cookies_tmp + item + '=' + cookies[item] + ';'
# 模拟登陆

print(cookies_tmp)

ww.get_cookie(data, url, cookies_tmp)
exit()
url = 'http://users.09game.com/'
response = s.post(url=url, headers=headers, cookies=cookies, data=data)
cookies = dict(response.cookies)
print(cookies)
# response.encoding = 'utf8'
# print(r.text)

url = 'http://users.09game.com/User'