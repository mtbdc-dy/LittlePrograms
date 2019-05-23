# -*- coding: utf-8 -*-
# @Time : 2019/4/26,026 20:15
# @Author : 徐缘
# @FileName: add_zte_server_hosts_allow.py
# @Software: PyCharm


import paramiko
import time
import csv

# sshd:211.136.99.92/255.255.255.255
filename = 'zte_server_list.csv'
f = open(filename, 'r')
reader = csv.reader(f)


def swith_user(server_info):
    print('当前IP： \033[32;0m{}\033[0m'.format(server_info[0]))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # '39.137.36.100', 22222, 'zxisec', 'SHYD@uss100'
    ssh.connect(server_info[0], server_info[1], server_info[2], server_info[3])
    channel = ssh.invoke_shell()

    channel.send("su - root\n")
    while not channel.recv_ready():     # Returns true if data is buffered and ready to be read from this channel. A False result does not mean that the channel has closed; it means you may need to wait before more data arrives.
        print("Working...")
        time.sleep(2)
    time.sleep(2)                       # 中兴服务器不按套路出牌
    print(channel.recv(1024))           # maximum number of bytes to read.

    channel.send("%s\n" % server_info[4])
    while not channel.recv_ready():
        print("Authenticating...")
        time.sleep(5)
    print(channel.recv(1024))

    channel.send("%s\n" % r"echo 'sshd:211.136.99.92'>>/etc/hosts.allow")
    while not channel.recv_ready():
        print("Add...")
        time.sleep(5)
    print(channel.recv(1024))

    channel.send("%s\n" % "systemctl restart sshd")
    while not channel.recv_ready():
        print("Restart sshd...")
        time.sleep(2)
    print(channel.recv(1024))

    channel.send("%s\n" % "history")
    while not channel.recv_ready():
        print("show shell history...")
        time.sleep(2)
    print(channel.recv(1024))


for item in reader:
    swith_user(item)


