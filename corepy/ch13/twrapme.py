#! /usr/bin/env python

from time import time, ctime

class TimedWrapMe(object):

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = \
                self.__atime = time()

    def get(self):
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or \
                t_type[0] not in 'cma':
            raise TypeError, \
            "argument of 'c', 'm', or 'a'' req 'd"
        return getattr(self, '_%s__%stime' % \
                (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return `self.__data`

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)


