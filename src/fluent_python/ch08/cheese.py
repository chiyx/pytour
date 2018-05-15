# -*- coding: UTF-8 -*-

import weakref


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


def main():
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
               Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))


if __name__ == '__main__':
    main()
