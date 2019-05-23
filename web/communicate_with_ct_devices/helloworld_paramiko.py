import paramiko
import chardet
import time


"""
API: http://docs.paramiko.org/en/2.4/api/channel.html?highlight=invoke_shell
"""
def hello():
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect('117.185.13.195', 22, 'llz@shmc', 'sw_76@Shmc')

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('dis arp')
    # 获取命令结果
    # print(type(stdout.read()))
    print(str(stdout.read()))
    ret = chardet.detect(stdout.read())
    print(ret)
    # 关闭连接
    ssh.close()


def swith_user():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('39.137.36.100', 22222, 'zxisec', 'SHYD@uss100')
    channel = ssh.invoke_shell()

    channel.send("su - root\n")
    while not channel.recv_ready():     # Returns true if data is buffered and ready to be read from this channel. A False result does not mean that the channel has closed; it means you may need to wait before more data arrives.
        print("Working...")
        time.sleep(2)
    time.sleep(2)                       # 中兴服务器不按套路出牌
    print(channel.recv(1024))           # maximum number of bytes to read.

    channel.send("%s\n" % 'SHYD@uss100')
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
        print("Restart sshd...")
        time.sleep(2)
    print(channel.recv(1024))


if __name__ == '__main__':
    hello()
    # swith_user()
