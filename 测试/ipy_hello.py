from IPy import IP

ip = IP('183.192.8.0/22')
ip_1 = IP('183.192.12.0/22')
print(ip + ip_1)
print(ip_1 + ip)
print(ip.overlaps(ip_1), ip_1.overlaps(ip))
exit()
print(ip.len())
print(ip)
for item in ip:
    print(item)

print(ip.strNormal(0))
print(ip.strNormal(1))
print(ip.strNormal(2))
print(ip.strNormal(3))

print(ip.iptype())

