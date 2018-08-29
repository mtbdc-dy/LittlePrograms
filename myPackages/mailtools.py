# coding:utf-8   #强制使用utf-8编码格式
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender = 'yxu9428@163.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
receiver = 'yxu9428@163.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量
receiver = 'xuyuan2@sh.chinamobile.com'


def mail_customise(title, content, my_user):
    flag = True
    try:
        msg=MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["徐缘", my_sender])   # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人", my_user[0]])   # 收件人，必须是一个字符串
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "Sqm940208")    # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   # 这句是关闭连接的意思
    except Exception:   # 如果try中的语句没有执行，则会执行下面的ret=False
        flag = False
    return flag


def mail139_customise(title, content, my_user):
    flag = True
    try:
        msg=MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["徐缘", 'shmcip@139.com'])   # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人", my_user[0]])   # 收件人，必须是一个字符串
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.139.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login('shmcip@139.com', "021SH@cmcc")    # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail('shmcip@139.com', my_user, msg.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   # 这句是关闭连接的意思
    except Exception:   # 如果try中的语句没有执行，则会执行下面的ret=False
        flag = False
    return flag


def mail(content, my_user):
    flag = True
    try:
        msg=MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["徐缘", my_sender])   # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人", my_user])   # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "Sqm940208")    # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   # 这句是关闭连接的意思
    except Exception:   # 如果try中的语句没有执行，则会执行下面的ret=False
        flag = False
    return flag


def mail_oa(content, my_user):
    flag = True
    try:
        msg=MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["徐缘", 'xuyuan2@sh.chinamobile.com'])   # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人", my_user])   # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.sh.chinamobile.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login('xuyuan2@sh.chinamobile.com', "Oa940208")    # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail('xuyuan2@sh.chinamobile.com', [my_user, ], msg.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   # 这句是关闭连接的意思
    except Exception:   # 如果try中的语句没有执行，则会执行下面的ret=False
        flag = False
    return flag


if __name__ == '__main__':
    my_user = 'xuyuan2@sh.chinamobile.com'
    ret = mail_oa('test_title', my_user)
    if ret:
        print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
    else:
        print("failed")  # 如果发送失败则会返回filed

