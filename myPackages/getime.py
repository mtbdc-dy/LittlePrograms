import datetime


def yesterday(form):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    yd = now - delta

    if form is not None:
        return yd.strftime('%Y%m%d')
    else:
        return yd.strftime('%Y-%m-%d')


