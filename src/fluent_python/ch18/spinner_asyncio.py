# -*- coding: UTF-8 -*-

import asyncio
import itertools
import sys


def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # <5>
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(3)  # <6>
    return 42


@asyncio.coroutine
def supervisor():  # <7>
    spinner = asyncio.async(spin('thinking!'))  # <8>
    print('spinner object:', spinner)  # <9>
    result = yield from slow_function()  # <10>
    spinner.cancel()  # <11>
    return result


def main():
    loop = asyncio.get_event_loop()  # <12>
    result = loop.run_until_complete(supervisor())  # <13>
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
