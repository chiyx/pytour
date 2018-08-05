# -*- coding: UTF-8 -*-

import threading
import itertools
import time
import sys


def spin(msg, done):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        if done.wait(.1):
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # pretend waiting a long time for I/O
    time.sleep(3)
    return 42


def supervisor():
    done = threading.Event()
    spinner = threading.Thread(target=spin, args=('thinking!', done))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    done.set()
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
