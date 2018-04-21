# -*- coding: UTF-8 -*-

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def dup(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.dup())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """
        返回折扣金额(正值)
        """


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


def main():
    joe = Customer('John Doe', 0)  # <1>
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),  # <2>
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    order = Order(joe, cart, FidelityPromo())  # <3>
    print(order)
    order = Order(ann, cart, FidelityPromo())  # <4>
    print(order)
    banana_cart = [LineItem('banana', 30, .5),  # <5>
                   LineItem('apple', 10, 1.5)]
    order = Order(joe, banana_cart, BulkItemPromo())  # <6>
    print(order)


if __name__ == '__main__':
    main()
