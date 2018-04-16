# -*- coding: UTF-8 -*-

import os

symbols = '$%^&*'
codes = [ord(ch) for ch in symbols]
print(codes)

_, filename = os.path.split('/homoe/idrs.pub')
print(filename)

l = list(range(10))
l[2:5] = [20]
print(l)
