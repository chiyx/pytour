#! /usr/bin/env python3
# coding = utf-8

import os
from bottle import route, run, static_file

base = os.path.dirname(os.path.abspath(__file__)) + '/static'


@route('/')
def home():
    return static_file('index.html', root=base)


@route('/echo/<thing>')
def echo(thing):
    return 'Say hello to my little friend: %s!' % thing

run(host='localhost', port=9999)


