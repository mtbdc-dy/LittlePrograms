# -*- coding: utf-8 -*-
# @Time : 2019-06-17 21:37
# @Author : 徐缘
# @FileName: port_scan.py
# @Software: PyCharm


import sys
import threading
from socket import *


host = "120.204.206.32" if len(sys.argv) == 1 else sys.argv[1]
portList = [i for i in range(1, 1000)]
portList = [80, 443, 8080]
scanList = []
lock = threading.Lock()
print('Please waiting... From ', host)


def scanPort(port):
    try:
        tcp = socket(AF_INET, SOCK_STREAM)
        tcp.connect((host, port))
    except:
        pass
    else:
        if lock.acquire():
            print('[+]port', port, 'open')
            lock.release()
    finally:
        tcp.close()


for p in portList:
    t = threading.Thread(target=scanPort, args=(p,))
    scanList.append(t)
for i in range(len(portList)):
    print(i, 's')
    scanList[i].start()
for i in range(len(portList)):
    print(i, 'j')
    scanList[i].join()

