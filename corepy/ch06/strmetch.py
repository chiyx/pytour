#! /usr/bin/env python

"""
metch two string by scanning each string
case-insensitiviy
"""

svarx = raw_input('Enter the first str >>')

if len(svarx) == 0:
    quit()

lvarx = list(svarx)
lvary = list(svarx)
lvarx.reverse()
lvary.extend(lvarx)



print ''.join(lvary)

