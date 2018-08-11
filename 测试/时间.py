import time
import datetime

# now = datetime.datetime.now()
#
# print(time.gmtime())
# print(now)
# print(time.time())
# print(time.localtime())
print(time.localtime())

t = (time.localtime()[0], time.localtime()[1], time.localtime()[2], 0, 0, 0, 0, 0, 0)
print(t)
print(int(time.mktime(t)))

te = int(time.mktime((time.localtime()[0], time.localtime()[1], time.localtime()[2], 0, 0, 0, 0, 0, 0)))
ts = te - (1533484800-1533398400)
print(te)
print(ts)
