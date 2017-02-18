#! /usr/bin/env python3
# coding = utf-8

from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck)
