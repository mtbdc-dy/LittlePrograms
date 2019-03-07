# -*- coding: utf-8 -*-
# @Time : 2019/3/7,007 15:59
# @Author : 徐缘
# @FileName: nslookup_hello.py
# @Software: PyCharm


import os
address = 'iphone.cmvideo.cn'
cmd = 'nslookup {} 211.136.150.66'.format(address)
os.system(cmd)

handle = os.popen(cmd, 'r')
result_nslook = handle.read()
print(result_nslook)
