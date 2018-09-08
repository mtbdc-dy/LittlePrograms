# import threading
# import time
#
# def action(arg):
#     time.sleep(1)
#     print('sub thread start!the thread name is:%s\r' % threading.currentThread().getName()）
#     print('the arg is:%s\r' %arg)
#     time.sleep(1)
#
# for i in range(4):
#     t =threading.Thread(target=action,args=(i,))
#     t.setDaemon(True)#设置线程为后台线程
#     t.start()
#
# print ('main_thread end!')