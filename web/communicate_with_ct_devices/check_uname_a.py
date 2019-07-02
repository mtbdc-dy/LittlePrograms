# -*- coding: utf-8 -*-
# @Time : 2019/7/2,002 14:36
# @Author : 徐缘
# @FileName: check_uname_a.py
# @Software: PyCharm


"""
    登录设备查询uname -a

"""

import paramiko
import time
import csv
import re

# sshd:211.136.99.92/255.255.255.255

reader = csv.reader(open('zte_server_list.csv', 'r'))
writer = csv.writer(open('output.csv', 'a', newline=''))


def uname(server_info):
    print('当前IP： \033[32;0m{}\033[0m'.format(server_info[0]))
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # '39.137.36.100', 22222, 'zxisec', 'SHYD@uss100'
    ssh.connect(server_info[0], server_info[1], server_info[2], server_info[3])
    channel = ssh.invoke_shell()
    login_line = channel.recv(65535)    # 没这句好像不行，很奇怪

    # channel.send("su - root\n")
    # while not channel.recv_ready():     # Returns true if data is buffered and ready to be read from this channel. A False result does not mean that the channel has closed; it means you may need to wait before more data arrives.
    #     print("Working...")
    #     time.sleep(2)
    # time.sleep(2)                       # 中兴服务器不按套路出牌
    # print(channel.recv(1024))           # maximum number of bytes to read.

    # channel.send("%s\n" % server_info[4])
    # while not channel.recv_ready():
    #     print("Authenticating...")
    #     time.sleep(5)
    # print(channel.recv(1024))

    channel.send("%s\n" % r"uname --all")
    while not channel.recv_ready():
        print("uname -a")
        time.sleep(1)
    ret = channel.recv(1024)
    print(str(ret))
    ssh.close()
    return str(ret)


for item in reader:
    lv = uname(item)
    try:
        a = re.findall(r'\d+\.\d+\.\d+', lv)[0]
    except IndexError:
        time.sleep(1)
        a = re.findall(r'\d+\.\d+\.\d+', uname(item))[0]
    print(a)
    writer.writerow([item[0], a])
