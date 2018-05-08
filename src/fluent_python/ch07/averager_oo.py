# -*- coding: UTF-8 -*-


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager


def main():
    avg = Averager()
    print(avg(10))
    print(avg(11))
    # func
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg.__code__.co_freevars)
    avg = make_averager2()
    print(avg(10))
    print(avg(11))
    print(avg.__code__.co_freevars)


if __name__ == '__main__':
    main()
