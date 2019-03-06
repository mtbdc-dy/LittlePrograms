# -*- coding: utf-8 -*-
# @Time : 2019/3/6,006 10:01
# @Author : 徐缘
# @FileName: part1_putian.py
# @Software: PyCharm


"""
查询普天所提供的URL
会返回HTML，提取值
"""
import web.webCrawler.webcrawler as ww
import urllib.request
import urllib.parse
import json
import xlrd
import xlwt
import datetime
from xlutils.copy import copy
import time
from bs4 import BeautifulSoup


url = 'http://10.221.17.131:9091/report/bizman/common/report.jsp?lable_target=_parent&state=jiakuandahuizhan1551838391637&iam=17455483&timename=jiakuandahuizhan&'

f = ww.get_web_page(url)
soup = BeautifulSoup(f, "html.parser")
avg_1st_screen_delay_web = soup.find(attrs={'id': 'td_jiakuandahuizhan_2_3'}).find(attrs={'style': 'cursor:text;'}).get_text()
key_local_web_access_delay = soup.find(attrs={'id': 'td_jiakuandahuizhan_3_3'}).find(attrs={'style': 'cursor:text;'}).get_text()
video_buffering_ratio_home_broadband = soup.find(attrs={'id': 'td_jiakuandahuizhan_4_3'}).find(attrs={'style': 'cursor:text;'}).get_text()
game_ping_home_broadband = soup.find(attrs={'id': 'td_jiakuandahuizhan_5_3'}).find(attrs={'style': 'cursor:text;'}).get_text()
game_packet_loss_rate_home_broadband = soup.find(attrs={'id': 'td_jiakuandahuizhan_6_3'}).find(attrs={'style': 'cursor:text;'}).get_text()

# print(f)
print(avg_1st_screen_delay_web, key_local_web_access_delay, video_buffering_ratio_home_broadband,
      game_ping_home_broadband, game_packet_loss_rate_home_broadband)

