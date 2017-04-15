#! /usr/bin/env python3
# coding = utf-8

# srv_threaded.py - 多线程版本服务器

from threading import Thread
import zen_utils


def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(4):
        Thread(target=zen_utils.accept_connect_forever, args=t).start()

if __name__ == '__main__':
    address = zen_utils.parse_command_line('multi-threaded server')
    listener = zen_utils.create_srv_socket(address)
    start_threads(listener)
