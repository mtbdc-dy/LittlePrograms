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
        "status": "softpedia https://www.softpedia.com",
    }
    files = {
        "pic": open("20181128360682_mSGega.gif", "rb")
    }
    r = requests.post(url_post_pic, data=playload, files=files)
    # r = requests.post(url_post_pic, data=playload)
    return r


if __name__ == '__main__':
    # print(check_token())
    f = post()
    print(f, f.content)

