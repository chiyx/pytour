# -*- coding: UTF-8 -*-

from coroutil import coroutine  # <4>


@coroutine  # <5>
def averager():  # <6>
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def main():
    coro_avg = averager()
    from inspect import getgeneratorstate
    print(getgeneratorstate(coro_avg))
    print(coro_avg.send(10))


if __name__ == '__main__':
    main()
