#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# generator_from_demo_1.py - yield from 语法熟悉


def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next


def gather_tallies(tallies):
    while 1:
        tally = yield from accumulate()
        tallies.append(tally)

tallies = []
acc = gather_tallies(tallies)
next(acc)
for i in range(4):
    acc.send(i)

acc.send(None)
for i in range(5):
    acc.send(i)

acc.send(None)

print(tallies)
