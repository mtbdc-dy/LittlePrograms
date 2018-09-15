def base_n(num, b):
    return ((num == 0) and "0") or (base_n(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


filename = 'number.txt'
filename_output = ''

f = open(filename, 'r')
lines = f.readlines()

# g = open(filename_output, 'w')
for item in lines:
    if item[-1] == '\n':
        n = int(item[0:-1])
    else:
        n = int(item)
    # print(n)
    n_2 = base_n(n, 2)
    # print(str(n_2))

    str_n_2 = str(n_2)

    s_zero = ''
    for i in range(32 - len(str_n_2)):
        s_zero = s_zero + '0'
    str_n_2 = s_zero + str_n_2
    # print(len(str_n_2))
    # print(str_n_2[::-1])

    n_10 = 0
    for i in range(32):
        if i == 32:
            continue
        if str_n_2[::-1][i] == '1':
            n_10 += 2 ** (31 - i)

    print(n_10)

