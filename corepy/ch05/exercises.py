#! /usr/bin/env python

'the exercises of ch05 -- Numbers'

def product(num1, num2):
    return num1 * num2

def isLeafYear(year):
    return (year % 4 == 0 and year % 100 != 0) or \
            (year % 400 == 0)


if __name__ == '__main__':
    print product(1.0, 5.5),
    print '2000 is a leafyear:', isLeafYear(2000)

