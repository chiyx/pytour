#! /usr/bin/env python3
# coding = utf-8

# str_match.py - 字符串匹配算法


def naive_matching(t, p):
    "朴素匹配算法"
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        # 字符相同，考虑下一对字符
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        # 字符不同，考虑t中下一个位置
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    else:
        return -1


def kmp_matching(t, kmpPattern):
    " KMP 匹配算法"
    p = kmpPattern.pattern
    m, n = len(t), len(p)
    i, j = 0, 0
    while i < m and j < n:
        if i == -1 or t[j] == p[i]:
            i, j = i + 1, j + 1
        else:
            i = p.pnext[i]
    if i == m:
        return j - i
    else:
        return -1


class KMPPattern:
    "kmp匹配的模式对象，负责将传入的待匹配串，做一定的预处理"

    def __init__(self, pattern):
        self.pattern = patter
        self.pnext = self.__compile()

    def __compile(self):
        return []


if __name__ == "__main__":
    print(naive_matching('abcd', 'dcefg'))
