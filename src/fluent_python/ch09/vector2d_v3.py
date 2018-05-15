# -*- coding: UTF-8 -*-

from array import array
import math


class Vector2d:
    typecode = 'd'  # <1>

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <3>

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # <4>

    def __str__(self):
        return str(tuple(self))  # <5>

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # <6>
                bytes(array(self.typecode, self)))  # <7>

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # <8>

    def __abs__(self):
        return math.hypot(self.x, self.y)  # <9>

    def __bool__(self):
        return bool(abs(self))  # <10>

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod  # <1>
    def frombytes(cls, octets):  # <2>
        typecode = chr(octets[0])  # <3>
        memv = memoryview(octets[1:]).cast(typecode)  # <4>
        return cls(*memv)  # <5>


def main():
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)  # <1>
    x, y = v1
    print(x, y)
    print(repr(v1))
    # v1_clone = eval(repr(v1))
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    v1_clone = Vector2d.frombytes(bytes(v1))
    print(v1_clone)
    print(hash(v1))

if __name__ == '__main__':
    main()
