def bubble_sort(slist):
    n = len(slist)
    for i in range(n):
        print('%d:' % i)
        for j in range(n-i-1):
            if slist[j] > slist[j+1]:
                slist[j], slist[j+1] = slist[j+1], slist[j]
            for k in range(n):
                print(slist[k], end=' ')
            print()
        for k in range(n):
            print(slist[k], end=' ')
        print()


def selection_sort(slist):
    n = len(slist)
    for i in range(n):
        min = slist[i]
        min_index = i
        for j in range(i+1, n):
            if min > slist[j]:
                min = slist[j]
                min_index = j
        if min_index != i:
            slist[i], slist[min_index] = slist[min_index], slist[i]

        for k in range(n):
            print(slist[k], end=' ')
        print()


def insert_sort(slist):
    n = len(slist)
    for i in range(n):
        for j in range(i, 0, -1):
            if slist[j] < slist[j-1]:
                slist[j], slist[j-1] = slist[j-1], slist[j]
            else:
                break
        for k in range(n):
            print(slist[k], end=' ')
        print()


if __name__ == '__main__':
    slist = [43, 36, 57, 23, 12, 78, 65, 42]
    # bubble_sort(slist)
    # selection_sort(slist)
    insert_sort(slist)

    print(slist)


