#! /usr/bin/env python3
# coding = utf-8
# mp.py - multiprocssing demo

import multiprocessing
import os
import time


def do_this(what):
    whoami(what)


def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)


def whoami(waht):
    print("Process %s says: %s" % (os.getpid(), waht))

if __name__ == '__main__':
    whoami("I'm the main program")
    p = multiprocessing.Process(target=loopy,
                                args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
