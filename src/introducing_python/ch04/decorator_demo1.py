#! /usr/bin/env python3
# coding = utf-8
# decorator_demo1.py - 装饰器例子1


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b

cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))


