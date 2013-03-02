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

# keyword argument function
def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print "-- This parrot would't", action
    print "if you put ", voltage, " volts through it."
    print "-- Lovely plumag, the ", type
    print "-- It's ", state, "!"

parrot(1000)
parrot(voltage = 1000)
parrot(voltage = 100000, action = 'VOOOOM')
