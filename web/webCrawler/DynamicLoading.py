import web.webCrawler.webcrawler as ww
import web.webCrawler.login as wl
# url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
#
# f = ww.get_web_page_ssl(url, '')
# print(f)

cookie = wl.login_wangluoquanjingkeshihua()
url = 'https://117.136.129.122/cmnet/mgrAnaIPTopN.htm?analyseMask=2097152'

f = ww.get_web_page_ssl_ie(url, cookie)
print(f)
