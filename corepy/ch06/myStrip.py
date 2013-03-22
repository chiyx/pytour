#! /usr/bin/env python

"""
my string.strip() implements
"""

def myStrip(svar = ''):
    ls=[]
    for x in svar:
        if not x.isspace():
            ls.append(x)
    return ''.join(ls)

if __name__ == '__main__':
    svar = myStrip('    \n hehhh    ')
    print svar
