# -*- coding: UTF-8 -*-

import itertools


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        while forever or result < self.end:
            yield result
            result += self.step


def main():
    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))
    gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
    print(list(gen))


if __name__ == '__main__':
    main()
