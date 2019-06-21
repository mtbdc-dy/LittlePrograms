# -*- coding: utf-8 -*-
# @Time : 2019-06-17 22:55
# @Author : 徐缘
# @FileName: multiprocessing_hello.py
# @Software: PyCharm


import os
from multiprocessing import Process
import time


# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# # s.fork()这个函数，对于父进程，返回的是子进程的pid，对于子进程，返回的是0.
# # 而通过os.getpid()得到的是当前的pid，os.getppid()得到的是父进程的pid。
# # 生成的自进程就会依照当前状态继续往下执行
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Process will start.')
    p.start()
    p.join()
    print('Process end.')
