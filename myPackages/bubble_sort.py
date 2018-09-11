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


def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap / 2


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    num = len(alist)/2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left,right)


def merge(left, right):
    """合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组"""
    # left与right的下标指针
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    slist = [43, 36, 57, 23, 12, 78, 65, 42]
    # bubble_sort(slist)
    # selection_sort(slist)
    insert_sort(slist)

    print(slist)


