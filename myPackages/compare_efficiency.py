from timeit import Timer
"""运行时间比较"""


def t1():
    list1 = []
    for i in range(2000):
        list1 = list1 + [1]


def t2():
    list2 = []
    for i in range(2000):
        list2.append(i)


if __name__ == '__main__':

    time1 = Timer("t1()", "from __main__ import t1")
    print(time1.timeit(number=2000))    # 执行2000次的平均效率

    time2 = Timer("t2()", "from __main__ import t2")
    print(time2.timeit(number=2000))
