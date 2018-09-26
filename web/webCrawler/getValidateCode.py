import web.webCrawler.webcrawler
import time
from PIL import Image


def base_n(num,b):
    return ((num == 0) and "0") or ( base_n(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


# 用urlretrieve还是什么


if __name__ == '__main__':      # 仅在自身运行时才会执行

    filename = 'validateCode0.jpeg'
    g = open(filename, 'wb')

    n = base_n(int((time.time() * 1000)), 36)
    # print(type(n))
    url = 'https://117.136.129.122/cmnet/validateCode.htm?temp=' + n
    f = web.webCrawler.webcrawler.get_img_ssl(url)
    g.write(f)
    g.close()

    im = Image.open("validateCode0.jpeg")
    im.show()

    vc = input("输入验证码")

    form = {
        'username': 'shanghai_qw',
        'password': 'sh_50331061',
        'exPwd': vc
    }

    url = 'https://117.136.129.122/cmnet/login.htm'
    f = web.webCrawler.webcrawler.post_web_page_ssl(url, form)
    # print(f)

    url = 'https://117.136.129.122/cmnet/main.htm'

    f = web.webCrawler.webcrawler.get_web_page_ssl(url)

    print(f)
