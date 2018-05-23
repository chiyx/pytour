# -*- coding: UTF-8 -*-

import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add item from an iterable"""

    def pick(self):
        """
        Remove item at random, returning it.
        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):  # <4>
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())  # <5>

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:  # <6>
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  # <7>
        return tuple(sorted(items))
