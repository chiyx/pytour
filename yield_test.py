#! /usr/bin/env python

def generator():
    alist = [i for i in range(1, 7)]
    for x in alist:
        print "x=",x
        yield x + 2

if __name__ == '__main__':
    for y in generator():
        print y
