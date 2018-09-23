import hashlib
import web.webCrawler.webcrawler

# 爬取DMS综合管理系统
# 第一第二part可以做成专用函数，如果有必要的话
# part1 峰值请求量
# 超关键 valid.pmt, 你得先去https://211.136.150.172:9090/领个jsessionid回来
# step1 获取验证码
# step2 提交用户名&密码、验证码

# part 1
# 获取jsessionid
url = 'https://211.136.150.172:9090'
cookie = ''
f = web.webCrawler.webcrawler.get_cookie_without_form(url)
for item in f:
    if item.name == 'JSESSIONID':
        cookie = item.name + '=' + item.value
print(cookie)
# sys.exit(0)

# part 2
# 获取token和验证码并验证登入
url = 'https://211.136.150.172:9090/toLogin.do'
f = web.webCrawler.webcrawler.get_web_page_ssl(url, cookie)
a = f.find('token')
# print(f[a+141:a+173])
token = f[a+141:a+173]
# sys.exit(0)

url = 'https://211.136.150.172:9090/CodeImageServlet'
web.webCrawler.webcrawler.get_validate_code(url, cookie)
validate_code = input("输入验证码")
h1 = hashlib.md5()
h2 = hashlib.md5()
h1.update('CD&N6!ch'.encode(encoding='utf-8'))
privatePa = h1.hexdigest() + validate_code
h2.update(privatePa.encode(encoding='utf-8'))
privatePa = h2.hexdigest()

form = {
    'struts.token.name': 'token',
    'token': token,
    'sysUser.username': 'cache',
    'privatePa': privatePa,
    'codeStr': validate_code
}

url = 'https://211.136.150.172:9090/doLogin.do'
f = web.webCrawler.webcrawler.post_web_page_ssl(url, form, cookie)

# part 3
# 获取数据
url = 'https://211.136.150.172:9090/getDNSReqHighChart.do'
form = {
    'con.mark': '0',
    'ipversion': '0',
    'con.seltype': '3',
    'con.starttimestr': '2018-06-01 00:00:00',
    'con.endtimestr': '2018-06-31 23:59:59'
}
f = web.webCrawler.webcrawler.post_web_page_ssl(url, form, cookie)
ft = f[-100:-1]

ans = ft[ft.find("最大值")+4:ft.find("最大值")+11]
ans = ans[0:3] + ans[-3:]
print("DNS业务量统计指标-峰值请求量：", ans)
