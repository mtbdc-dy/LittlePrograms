from IPy import IP

"""
将txt中的IP地址段 展示成 x.x.x.x ~ x.x.x.x的格式 方便合并
"""

filename = 'ipy_hello.txt'
f = open(filename, 'r', newline='')
reader = f.readlines()

for item in reader:
    ip = IP(item)

    # print(ip.strNormal(0), '', end='')
    print(ip.strNormal(3))
    continue
    # print(ip.strNormal(1))
    # print(ip.strNormal(2))
    # print(ip.strNormal(3))
    length = ip.len() - 1
    # print(length)
    if length <= 255:
        print('0.0.0.', end='')
        print(length)
    else:
        length = int(((length + 1) / 256) - 1)
        print('0.0.', end='')
        print(length, end='')
        print('.255')


# ip = IP('183.192.8.0/22')
# ip_1 = IP('183.192.12.0/22')
# print(ip + ip_1)
# print(ip_1 + ip)
# print(ip.overlaps(ip_1), ip_1.overlaps(ip))
# exit()
# print(ip.len())
# print(ip)
# for item in ip:
#     print(item)
#
# print(ip.strNormal(0))
# print(ip.strNormal(1))
# print(ip.strNormal(2))
# print(ip.strNormal(3))
#
# print(ip.iptype())

