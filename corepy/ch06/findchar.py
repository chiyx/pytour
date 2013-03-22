#! /usr/bin/env python

"findchr() not use string.*find() or string.*index()"

def findchr(string, char):
    for i, x in enumerate(string):
        if x == char:
            return i
    return -1
