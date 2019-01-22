import datetime
import time

# 无输入，格式为20180913
# 有输入，格式为2018-09-13
def yesterday(form):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    yd = now - delta

    if form is not None:
        return yd.strftime('%Y%m%d')
    else:
        return yd.strftime('%Y-%m-%d')


# n days ago
def n_days_ago(n):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_days = now-delta
    n_days.strftime('%Y-%m-%d')  # 不会改变对象的值
    # print(n_days)
    return n_days.strftime('%Y-%m-%d')


def today():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d+%H:%M:%S')


def get_today_zero_stamp():
    now = time.time()  # time.time() 零时区时间戳
    return '%d' % (now - (now + 8 * 3600) % 86400)  # 当天凌晨


if __name__ == '__main__':
    print(n_days_ago(1))
    print()
