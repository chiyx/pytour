#! /usr/bin/env python3
# coding = utf-8

# search2.py - 通过谷歌地理api将一个地址转换为经纬度信息

import requests


def geocode(address):
    paramters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    respone = requests.get(base, paramters)
    respone.raise_for_status()
    answer = respone.json()
    return answer['results'][0]['geometry']['location']

if __name__ == '__main__':
    location = geocode('207 N. Defiance St, Archbold, OH')
    print(location)
