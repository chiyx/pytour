#! /usr/bin/env python3
# coding = utf-8

# previous_lines.py - 返回匹配行的前n行


from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


if __name__ == '__main__':
    # print("a" * 20, end='')
    # print('-')
    with open('./test.txt') as f:
        for line, previous_lines in search(f, 'python'):
            for pline in previous_lines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

