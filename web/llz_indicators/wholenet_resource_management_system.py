# -*- coding: utf-8 -*-
# @Time : 2019/4/4,004 16:15
# @Author : 徐缘
# @FileName: wholenet_resource_management_system.py
# @Software: PyCharm


import web.webCrawler.webcrawler as ww
import matplotlib.pyplot as plt

if __name__ == '__main__':
    url = 'http://117.136.187.13:10086/img/checkImg'
    cookie = ''
    f = ww.get_img_ssl(url, cookie)
    filename = 'validateCode.jpeg'
    g = open(filename, 'wb')

    g.write(f)
    g.close()

    img = plt.imread("validateCode0.jpeg")  # 用pyplot会快很多呀
    plt.imshow(img)
    plt.show()
    cj = http.cookiejar.CookieJar()
    opener_cookie = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener_cookie.open(request)




