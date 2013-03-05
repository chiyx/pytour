#! /usr/bin/env python

class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self):
        self.data=[]
    def f(self):
        return "hello world"

class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except C:
        print "C"
    except B:
        print "B"

