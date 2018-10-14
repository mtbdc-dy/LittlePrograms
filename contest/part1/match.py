def isMatch(s, p):
    p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
    while s_ptr < len(s):
        if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
            s_ptr += 1
            p_ptr += 1
        elif p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            last_s_ptr = s_ptr
            last_p_ptr = p_ptr
        elif last_p_ptr != -1:
            last_s_ptr += 1
            s_ptr = last_s_ptr
            p_ptr = last_p_ptr
        else:
            return False

    while p_ptr < len(p) and p[p_ptr] == '*':
        p_ptr += 1

    return p_ptr == len(p)


if __name__ == "__main__":
    filename = 'match' + '.txt'  # 改下文件名
    f = open(filename, 'r')
    reader = f.readlines()

    status = True
    for item in reader:
        item = item.rstrip()
        if item == '':
            continue
        if item == '---':
            # print()
            if isMatch(f, s):
                print('true')
            else:
                print('false')
        if status:
            f = item
            status = False
        else:
            s = item
            status = True
