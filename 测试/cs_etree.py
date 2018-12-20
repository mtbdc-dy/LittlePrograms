from lxml import etree
import web.webCrawler.webcrawler as ww
# text = '''<html><head>123</head><body><div>123</div></body></html>'''
# etree = html.etree
# htmlDiv = etree.HTML(text)
# title = htmlDiv.xpath("//div/text()")
# print(title)
# exit()
url = 'https://blog.csdn.net/qq_32590631/article/details/80941794'
f = ww.get_web_page_ssl(url, '')
# print(f)
# etree = html.etree
h = etree.HTML(f)
content = h.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[1]/h1/text()')
print(content)
