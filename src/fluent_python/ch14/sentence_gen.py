# -*- coding: UTF-8 -*-

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:  # <1>
            yield word  # <2>
        return  # <3>


def main():
    s = Sentence('"The time has come, " the world said')
    for word in s:
        print(word)


if __name__ == '__main__':
    main()
