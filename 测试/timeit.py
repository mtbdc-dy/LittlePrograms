from timeit import Timer


# 还没跑通
def t1():
    list1 = []
    for i in range(2000):
        list1 = list1 + [1]


def t2():
    list2 = []
    for i in range(2000):
        list2.append(i)


time1 = Timer("t1()", "from _main_ import t1")
print(time1.timeit(number=2000))    # 执行2000次的平均效率

time2 = Timer("t2()", "from _main_ import t2")
print(time2.timeit(number=2000))
