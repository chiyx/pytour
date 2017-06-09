#! /usr/bin/env python3
# coding = utf-8

import urllib.request as ur

# url = 'http://www.baidu.com'
# conn = ur.urlopen(url)
# for key, value in conn.getheaders():
#     print(key, value)

line = 'shopId=106096685,userId=1745656365,nick=anta安踏童装旗舰店,url=antakids.tmall.com/campaign-3761-42.htm'

elem = {}
for kv in line.split(','):
    arr = kv.split('=')
    elem[arr[0]] = arr[1]
print(elem)
print(isinstance('a', str))

a = ['hello', 'world', '1', '2']
print(a[0::2], a[1::2])
print(dict(zip(a[0::2], a[1::2])))
