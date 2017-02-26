#! /usr/bin/env python3
# coding = utf-8

import urllib.request as ur

url = 'http://www.baidu.com'
conn = ur.urlopen(url)
for key, value in conn.getheaders():
    print(key, value)
