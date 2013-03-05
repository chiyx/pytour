#! /usr/bin/env python

def f(x): return x % 2 != 0 and x % 3 != 0

data = filter(f, range(2, 25))
print data

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v


