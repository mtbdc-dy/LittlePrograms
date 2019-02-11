import paramiko
import chardet


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

