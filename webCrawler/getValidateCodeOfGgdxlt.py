import webCrawler.webcrawler
import webCrawler.login
import time
import myPackages.number_base_conversion


url = 'https://117.136.129.122/cmnet/index.htm'
cj = webCrawler.webcrawler.get_cookie_without_form(url)
for item in cj:
    cookie = item.name + '=' + item.value

date = int(time.time()*1000)
temp = myPackages.number_base_conversion.base_n(date, 36)
url = 'https://117.136.129.122/cmnet/validateCode.htm?temp=' + temp

fold_path = '../PictureProcessing/GGDXLT_Examples/'
for i in range(1,11):
    webCrawler.webcrawler.get_validate_code(url, cookie, i, fold_path)
