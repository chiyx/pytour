#! /usr/bin/env python

var1 = 2
def localfn():
    var1 = 3
    return var1

print var1

def localfn2(var1):
    print var1
    return var1

localfn()
localfn2(5)
