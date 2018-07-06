import time
import datetime

now=datetime.datetime.now()
delta=datetime.timedelta(days=7-0)
n_days=now-delta
n_days.strftime('%Y-%m-%d') # 不会改变对象的值
print(n_days)