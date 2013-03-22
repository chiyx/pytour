#! /usr/bin/env python

'some useful function for nums'

def getfactors(num):
    """get all factor of this num"""
    if num <= 0: 
        return []
    result = [1]
    count = num / 2 + 1
    other = [x for x in range(2, count) if not (num % x)]
    return result + other

def isperfect(num):
    """judge whether a num is a perfect num or not!"""
    factors = getfactors(num)
    total = sum(factors)
    return True if total == num and num != 0 else False


