# -*- coding: UTF-8 -*-

from functools import wraps


def corotine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args, **kwargs):  # <1>
        gen = func(*args, **kwargs)  # <2>
        next(gen)  # <3>
        return gen  # <4>
    return primer
