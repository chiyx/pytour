#! /usr/bin/env python
def f():
    a = [1, 2]
    b = 1
    c = 'hello'
    d = (1, )
    e = True
    f = {1: 2}
    
    def inf():
        print locals()
        a[0] += 1
        b = 2
        c = 3
        d = (2, )
        e = False
        f[1] = 3
        return a[0]
    return inf

if __name__ == '__main__':
    a = f()
    t = a()
    print t

