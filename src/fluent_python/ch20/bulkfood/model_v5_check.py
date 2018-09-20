# -*- coding: UTF-8 -*-

import abc


class AutoStorage:

    __counter = 0

    def __init__(self):
        cls = = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.store_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.store_name)

    def __set__(self, instance, value):
        setattr(instance, self.store_name, value)


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""


INVALID = object()


class Check(Validated):

    def __init__(self, checker):
        super().__init__()
        self.checker = checker
        if checker.__doc__ is None:
            doc = ''
        else:
            doc = checker.__doc__ + '; '
        self.message = doc + '{!r} is not valid.'

    def validate(self, instance, value):
        result = self.checker(value)
        if result is INVALID:
            raise ValueError(self.message.format(value))
        return result


def gt_zero(x):
    '''value must be > 0'''
    return x if x > 0 else INVALID


def non_blank(txt):
    txt = txt.strip()
    return txt if txt else INVALID


class LineItem:
    description = model.Check(non_blank)
    weight = model.Check(gt_zero)
    price = model.Check(gt_zero)

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
