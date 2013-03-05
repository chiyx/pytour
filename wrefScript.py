#! /usr/bin/env python

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print d['primary']
del a
print gc.collect()

print d['primary']


