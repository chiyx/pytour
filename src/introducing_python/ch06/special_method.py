#! /usr/bin/env python3
# coding = utf-8


class Word():

    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'


first = Word('ha')
secord = Word('HA')
print(first == secord)
print(first)
