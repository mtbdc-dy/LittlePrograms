# -*- coding: utf-8 -*-
# @Time : 2019/7/4,004 12:49
# @Author : 徐缘
# @FileName: check_broadband_account_password.py
# @Software: PyCharm



import ssl
import urllib
import web.webCrawler.webcrawler as ww
url = 'https://211.136.164.154/prx/000/http/pboss.cmcc/dbformrefresh?action=refresh&pk=-1&condition=queryAccInfoFromRadius&ACCOUNT_ID=15221070194&PASSWORD=123456&ACCOUNT_TYPE_ID=&staffID=&orgID=&domainID=&url_source=XMLHTTP'
form = '<FormInfo formid="crmInfoForm" setname="com.ailk.shmobile.pboss.set.SETAccountInfo" datamodel="com.ai.appframe2.web.tag.ActionDataModel" editable="false" conditionname="queryAccInfoFromRadius" parametersname="com.ailk.shmobile.pboss.action.ShQAccountLogin" cols="ACCOUNT_ID;EXT1;STATUS;VLAN_ID;BAND_WIDTH"  ></FormInfo>'
# form = {
#     'asd1': 'asd2'
# }
# b'asd1=asd2'
form = form.encode('utf8')
ssl._create_default_https_context = ssl._create_unverified_context
# context = ssl._create_unverified_context()
cooke = 'AN_nav1=1%3dopen%262%3dbuttons%263%3dright%264%3dclosed%265%3d2a381e25%26eoc;' \
        'ANsession0016020114037234=pboss+2a382179_b185335c1b86bb26799a529517884d5f;' \
        'NSCOOKIE%3Bpboss%2Ecmcc%3B%2F%3Bal_PBOSS=A1YiFmcpKCiILkQnSP%2FiPg%24%24%3B%3B;' \
        'NSCOOKIE%3Bpboss%2Ecmcc%3B%2F%3BWT_USER_ID=9319-22abf63c33f5d19%3B%3B;' \
        'NSCOOKIE%3Bpboss%2Ecmcc%3B%2F%3BJSESSIONID=b737bc7e02f0d91268cf63171197%3B%3B;' \
        'ANsession0016020114037234=pboss+2a382179_b185335c1b86bb26799a529517884d5f'
header = {
    'User-Agent': 'User-Agent Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; Media Center PC 6.0)',
    'Cookie': cooke
}

request = urllib.request.Request(url, headers=header)
# 编码
# form_data = urllib.parse.urlencode(form).encode('utf8')
# print(form_data)
# exit()
# 读取页面
response = urllib.request.urlopen(request, data=form)  # context=context
f = response.read().decode("utf8")
print(f)
