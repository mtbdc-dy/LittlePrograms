import os

cmd = 'ls'

# os.system(cmd)

hostname = 'img.baidu.com'
cmd = 'nslookup %s' % hostname
print(cmd)
handle = os.popen(cmd, 'r')
result_nslook = handle.read()
print(result_nslook)
