# -*- coding: UTF-8 -*-

# 特性(property)的使用, 使用工程方法包装


def quantity(storage_name):

    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise TypeError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:

    weight = quantity('weight')  # <1>
    price = quantity('price')  # <2>

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    item = LineItem('Moluccan nutmeg', 8, 13.95)
    
    # item.__dict__['weight'] = 0


if __name__ == '__main__':
    main()
