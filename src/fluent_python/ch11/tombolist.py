# -*- coding: UTF-8 -*-

from random import randrange
from tombola import Tombola


@Tombola.register
class TomboList(list):  # <2>

    def pick(self):
        if self:  # <3>
            position = randrange(len(self))
            return self.pop(position)  # <4>
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # <5>

    def loaded(self):
        return bool(self)  # <6>

    def inspect(self):
        return tuple(sorted(self))


def main():
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)


if __name__ == '__main__':
    main()
