def base_n(num, b):
    return ((num == 0) and "0") or (base_n(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


if __name__ == '__main__':
    a = base_n(18128821, 36)
    print(a)
