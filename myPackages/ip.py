"""
    Stuff about Ip Address
"""


def add_one_on_ip(ip):
    def to_str(a):
        s = ''
        for i in a:
            s = s + str(i) + '.'
        return s[0:-1]

    ip = ip.split('.')
    print(ip)
    if len(ip) != 4:
        return False
    
    ip_r = list()
    for item in ip:
        ip_r.append(int(item))
    print(ip_r)
    if ip_r[-1] < 255:
        ip_r[-1] += 1
        return to_str(ip_r)
    elif ip_r[-2] < 255:
        ip_r[-1] = 0
        ip_r[-2] += 1
        return to_str(ip_r)
    elif ip_r[-3] < 255:
        ip_r[-1] = 0
        ip_r[-2] = 0
        ip_r[-3] += 1
        return to_str(ip_r)
    else:
        ip_r[-1] = 0
        ip_r[-2] = 0
        ip_r[-3] = 0
        ip_r[0] += 1
        return to_str(ip_r)


if __name__ == '__main__':
    ip = '4.255.255.255'
    print(add_one_on_ip(ip))

