# -*- coding: UTF-8 -*-

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2} @ {1:2d}   {2}{0:<2d}'


def demo(bitsect_fn):
    for needle in reversed(NEEDLES):
        position = bitsect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


def main():
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect
    else:
        bisect_fn = bisect.bisect_left
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


if __name__ == '__main__':
    main()
