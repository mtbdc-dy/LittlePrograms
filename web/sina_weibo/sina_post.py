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
        # www.doutula.com 找些傻逼表情包配上
        "status": "为什么手机屏锁试四五次都打不开，付钱要认证的时候轻轻放一下就可以了？？ https://ws4.sinaimg.cn/large/9150e4e5gy1fxa7xmrdfhj208c05aglh.jpg",
    }
    files = {
        "pic": open("sina_pic.png", "rb")
    }
    r = requests.post(url_post_pic, data=playload, files=files)
    # r = requests.post(url_post_pic, data=playload)
    return r


if __name__ == '__main__':
    # print(check_token())
    f = post()
    print(f, f.content)
