import requests


def check_token():
    url_post_pic = "https://api.weibo.com/oauth2/get_token_info"
    playload = {
        "access_token": '2.00ixOpPDIg6znDa273b69da7ZFtzqB',
    }
    r = requests.post(url_post_pic, data=playload)
    return r.content


def post():
    url_post_pic = 'https://api.weibo.com/2/statuses/share.json'
    playload = {
        "access_token": "2.00ixOpPDIg6znDa273b69da7ZFtzqB",
        "status": "速度慢问题",    # 微博内容
    }
    r = requests.post(url_post_pic, data=playload)
    # r = requests.post(url_post_pic, data=playload)
    return r


def post_with_pic():
    url_post_pic = 'https://api.weibo.com/2/statuses/share.json'
    playload = {
        "access_token": "2.00ixOpPDIg6znDa273b69da7ZFtzqB",

        "status": "解决stackoverflow.com网站打开速度慢问题 https://blog.csdn.net/weixin_40700486/article/details/83820972#_5",
    # 微博内容
    }
    files = {
        "pic": open("1.jpg", "rb")  # www.doutula.com 找些傻逼表情包配上
    }
    r = requests.post(url_post_pic, data=playload, files=files)
    # r = requests.post(url_post_pic, data=playload)
    return r


if __name__ == '__main__':
    print(check_token())
    exit()
    f = post()
    print(f, f.content)

