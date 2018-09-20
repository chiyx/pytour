# -*- coding: UTF-8 -*-


class Quantity:

    def __init__(self, store_name):
        self.store_name = store_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.store_name] = value
    else:
        raise ValueError('value must be > 0')


class LineItem:

    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
