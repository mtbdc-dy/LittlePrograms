import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
timestamp = time.mktime(t)
time_array = time.localtime(timestamp)
print(time.strftime("%H:%M:%S", time_array))
print(time.strftime("%H:%M", t))


