import urllib.request
import urllib.parse
import time
import http.cookiejar
import csv, codecs
from bs4 import BeautifulSoup
import random
import urllib.error
import ssl
import datetime
from PIL import Image
import socket


a = 'http://www.baidu.com/s?ie=utf-8&f=8&tn=baidu&wd=临时邮箱'

b = urllib.parse.urlencode(a).encode('utf8')

print(b)
