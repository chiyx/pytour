#! /usr/bin/env python

"""compare list comps and generator"""

def normal_find_longest():
    f = open('/etc/profile', 'r')
    longest = 0
    while True:
        linelen = len(f.readline().strip())
        if not linelen: break
        if linelen > longest:
            longest = linelen
    f.close()
    return longest

def comps_find_longest():
    f = open('/etc/profile', 'r')
    longest = 0
    allLines = [line.strip() for line in f.readlines()]
    f.close()
    for x in allLines:
        linelen = len(x)
        if linelen > longest:
            longest = linelen
    return longest

def generator_find_longest():
    return max(len(x.strip()) for x in open('/etc/profile'))

if __name__ == '__main__':
    c = raw_input("Enter you choice: n(Normal), c(Comps), g(Generator)>>>")
    result = ''
    if c == 'n':
        result = normal_find_longest()
    elif c == 'c':
        result = comps_find_longest()
    else:
        result = generator_find_longest()
    print result
