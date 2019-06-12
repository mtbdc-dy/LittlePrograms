# -*- coding: utf-8 -*-
# @Time : 2019/6/11,011 13:01
# @Author : 徐缘
# @FileName: builtwith_hello.py
# @Software: PyCharm

"""
识别网站 使用的技术类型
"""

import builtwith

res = builtwith.parse('http://example.webscraping.com')
print(res)
# {'web-servers': ['Nginx'], 'web-frameworks': ['Web2py', 'Twitter Bootstrap'],
# 'programming-languages': ['Python'], 'javascript-frameworks': ['jQuery', 'Modernizr', 'jQuery UI']}

res = builtwith.parse('http://tool.oschina.net')
print(res)

