# -*- coding: UTF-8 -*-

from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> Started: a = ', a)
    b = yield a
    print('-> Received: b = ', b)
    c = yield a + b
    print('-> Received: c = ', c)


def main():
    my_coro2 = simple_coro2(14)
    getgeneratorstate(my_coro2)
    x = next(my_coro2)
    print(x)
    getgeneratorstate(my_coro2)
    my_coro2.send(28)
    my_coro2.send(99)

if __name__ == '__main__':
    main()
