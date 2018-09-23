from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='')

# 127.0.0.1是回送地址，指本地机，一般用来测试使用。回送地址是本机回送地址（Loopback Address）
# ，即主机IP堆栈内部的IP地址，主要用于网络软件测试以及本地机进程间通信，无论什么程序，一旦使
# 用回送地址发送数据，协议软件立即返回，不进行任何网络传输。

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='80')



