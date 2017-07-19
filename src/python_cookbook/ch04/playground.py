#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ch04 - 迭代器与生成器

from itertools import dropwhile
import sys


def manual_iter_1():
    "使用next进行手动迭代"
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


def manual_iter_2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


def frange(start, end, increment):
    x = start
    while x < end:
        yield x
        x += increment


class Node:
    "支持深度优先方式遍历的树的节点"

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


def test_iter_node():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)


def test_dropwhile():
    with open('/etc/passwd') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line)


def test_iter():
    with open('/etc/passwd') as f:
        for chunk in iter(lambda: f.read(10), ''):
            n = sys.stdout.write(chunk)


def main():
    print(sys.getfilesystemencoding())
    # manual_iter_1()
    # manual_iter_2()
    # for i in frange(0, 5, 0.5):
    #     print(i)
    # test_iter_node()
    # test_dropwhile()
    test_iter()

if __name__ == '__main__':
    main()
