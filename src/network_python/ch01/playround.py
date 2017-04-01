#! /usr/bin/env python3
# coding = utf-8

# playround.py - 第一章中一些简短的演示代码


import socket


def getHost(hostname):
    addr = socket.gethostbyname(hostname)
    return (hostname, addr)

if __name__ == '__main__':
    hostname = 'www.python.org'
    host = getHost(hostname)
    print('The IP address of {}, is {}'.format(host[0], host[1]))
