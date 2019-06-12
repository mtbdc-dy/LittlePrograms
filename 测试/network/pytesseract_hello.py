# -*- coding: utf-8 -*-
# @Time : 2019/6/12,012 13:41
# @Author : 徐缘
# @FileName: pytesseract_hello.py
# @Software: PyCharm


"""
通过SQM测试pytesseract，虽然以前好像测过
不过现在有本书可以参考着看看
https://github.com/madmaze/pytesseract
https://github.com/tesseract-ocr/tesseract/wiki

pip install virtualenv
portia
就结果而言迟早成为时代的糟粕
"""
import time
import random
from PIL import Image   # 这个包叫pillow就很奇怪
import pytesseract
import web.webCrawler.webcrawler as ww

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def removeFrame(img, width):
    '''
    :param img:
    :param width: 边框的宽度
    :return:
    '''
    w, h = img.size
    pixdata = img.load()
    for x in range(width):
        for y in range(0, h):
            pixdata[x, y] = 255
    for x in range(w - width, w):
        for y in range(0, h):
            pixdata[x, y] = 255
    for x in range(0, w):
        for y in range(0, width):
            pixdata[x, y] = 255
    for x in range(0, w):
        for y in range(h - width, h):
            pixdata[x, y] = 255
    return img


# 识别验证码就是为了获取cookie
url = 'http://117.144.107.165:8088/evqmaster/CheckCode'
cj = ww.get_cookie_without_form(url)
cookie = ''
for item in cj:
    cookie = item.name + '=' + item.value
print(cookie)
# cookie = 'JSESSIONID=859D1BE9728F46E71C2B765186B593A1'


# 获取验证码 加random 是为了改一下请求 那样就不会去缓存中获取这张图片了
url = 'http://117.144.107.165:8088/evqmaster/CheckCode?' + str(random.random())
f = ww.get_img_ssl(url, cookie)   # 不是特别懂，but it works.
# 是否传入文件名，来判断是普通验证，还是下载验证码
filename = 'validateCode0.png'
g = open(filename, 'wb')
g.write(f)
g.close()
im = Image.open("validateCode0.png")
gray = im.convert('L').point(lambda x: 0 if x < 40 else 255, '1')
gray = removeFrame(gray, 1)
gray.show()
print(pytesseract.image_to_string(gray, config='digits'))
exit()

pwd = input('输入验证码，谢谢')

# 提交登入表单
url = 'http://117.144.107.165:8088/evqmaster/configaction!login.action'
form = {
    'username': 'xuyuan',
    'password': '2EF60361839CBA359266E62F16E21A7A',
    'checkcode': pwd
}

ww.post_web_page(url, form, cookie)

