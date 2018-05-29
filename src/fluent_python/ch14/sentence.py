# -*- coding: UTF-8 -*-

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # <1>

    def __getitem__(self, index):
        return self.words[index]  # <2>

    def __len__(self, index):  # <3>
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # <4>


def main():
    s = Sentence('"The time has come, " the world said')
    for word in s:
        print(word)

if __name__ == '__main__':
    main()
