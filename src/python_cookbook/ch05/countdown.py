#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# countdown.py - 内部定义了一个线程但仍可被序列化的类

import time
import threading
import pickle


class Countdown:

    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


def main():
    c = Countdown(30)
    time.sleep(10)
    with open('cstate.p', 'wb') as f:
        pickle.dump(c, f)
    with open('cstate.p', 'rb') as f:
        pickle.load(f)

if __name__ == '__main__':
    main()
