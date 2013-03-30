#! /usr/bin/env python

from time import time

def timeAdvise(func):
    def funcWithTime(func2, seq):
        startTime = time()
        value = func(func2, seq)
        endTime = time()
        return (value, endTime - startTime)
    return funcWithTime

@timeAdvise
def my_filter(func, seq):
    return [x for x in seq if func(x)]

if __name__ == '__main__':
    rs = my_filter(lambda x: x % 2 != 0, range(1, 100))
    print rs



