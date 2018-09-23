import http.cookiejar,urllib.request

filename = 'cookieE.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HttpCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)