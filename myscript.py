#! /usr/bin/env python
# coding=gbk

currency=u"￥"
print ord(currency)

def fib(n): #write Fibonacci series up to n
    """Print a Fibonacci series up to n """
    a, b = 0, 1
    while a  < n:
        print a,
        a, b = b, a + b

def fib2(n): #return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

#call the function fib2
f100 = fib2(1000)
print f100
