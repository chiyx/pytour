#! /usr/bin/env python
#coding: utf-8

def ma(cls):
    print 'method a'

def mb(cls):
    print 'method b'

method_dict = {
        'ma': ma,
        'mb': mb
}

class DynamicMethod(type):
    def __new__(cls, name, bases, dct):
        if name[:3] == 'Abc':
            dct.update(method_dict)
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(DynamicMethod, cls).__init__(name,bases, dct)

class AbcTest(object):
    __metaclass__= DynamicMethod
    def mc(self, x):
        print x * 3

class NotAbc(object):
    __metaclass__ = DynamicMethod
    def md(self, x):
        print x * 3

def main():
    a = AbcTest()
    a.mc(3)
    a.ma()
    print dir(a)
    
    b = NotAbc()
    print dir(b)

if __name__ == '__main__':
    main()


