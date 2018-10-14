import collections


def bus(routes, S, T):
    if S == T:
        return 0

    to_route = collections.defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            to_route[stop].add(i)

    result = 1
    q = [S]
    lookup = set([S])
    while q:
        next_q = []
        for stop in q:
            for i in to_route[stop]:
                for next_stop in routes[i]:
                    if next_stop in lookup:
                        continue
                    if next_stop == T:
                        return result
                    next_q.append(next_stop)
                    to_route[next_stop].remove(i)
                    lookup.add(next_stop)
        q = next_q
        result += 1

    return -1


if __name__ == '__main__':
    filename = 'bus' + '.txt'   # 改下文件名
    f = open(filename, 'r')
    reader = f.readlines()

    '''customize'''
    s = 0
    t = 0
    b = list()
    for item in reader:
        item = item.rstrip()
        if item[0] == 'S':
            s = int(item[2:])
            continue
        if item[0] == 'T':
            t = int(item[2:])
            continue
        if item[0] == '-':
            # print(s, t)

            print(bus(b, s, t))
            s = 0
            t = 0
            b = list()
            continue
        if item[0] == 'r':
            item = item[9:-2]
            row = item.split(',')
            n = list()
            for i in row:
                # print(i)
                n.append(int(i))
            b.append(n)
            # print(item)
            continue
        if item[0] == '{' and item[-1] == ';':
            # print(item)
            item = item[1:-3]
            row = item.split(',')
            n = list()
            for i in row:
                n.append(int(i))
            b.append(n)
            continue
        if item[0] == '{' and item[-1] == ',':
            item = item[1:-2]
            row = item.split(',')
            n = list()
            for i in row:
                n.append(int(i))
            b.append(n)
            continue


