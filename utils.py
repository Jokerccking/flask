import time


def log(*args, **kwargs):
    f = '%Y/%m/%d'
    t = time.localtime(int(time.time()))
    ft = time.strftime(f, t)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(ft, *args, file=f, **kwargs)
