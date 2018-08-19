import datetime
import time

now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d'))
sjc = str(int(time.time() * 1000))
print(sjc)
