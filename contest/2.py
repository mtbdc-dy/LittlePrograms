
filename = 'IP.txt'
filename_output = ''

f = open(filename, 'r')
lines = f.readlines()

# g = open(filename_output, 'w')

for item in lines:
    if item[-1] == '\n':
        ip = item[0:-1]
    else:
        ip = item

    # print(ip)

    count = 0
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                for q in range(1, 4):
                    if i+j+k+q != len(ip):
                        continue
                    else:
                        if i > 1:
                            if ip[0:1] == '0':
                                continue
                        if j > 1:
                            if ip[i:i+1] == '0':
                                continue
                        if k > 1:
                            if ip[i+j:i+j+1] == '0':
                                continue
                        if q > 1:
                            if ip[i+j+k:i+j+k+1] == '0':
                                continue
                        ip_1 = int(ip[0:i])
                        ip_2 = int(ip[i:i+j])
                        ip_3 = int(ip[i+j:i+j+k])
                        ip_4 = int(ip[i+j+k:i+j+k+q])
                        if ip_1 == 0 or ip_1 > 255 or ip_2 > 255 or ip_3 > 255 or ip_4 > 255:
                            continue
                        count += 1
                        # print(ip_1, ' ', ip_2, ' ', ip_3, ' ', ip_4)
    print(count)
    # print()



