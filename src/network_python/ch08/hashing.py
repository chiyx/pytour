#! /usr/bin/env python3
# coding = utf-8

# hashing.py - hash分片测试

import hashlib

servers = ['server0', 'server1', 'server2', 'server3']


def alpha_shard(word):
    "根据首字母分片"
    ch = word[0]
    if ch < 'g':
        return servers[0]
    elif ch < 'n':
        return servers[1]
    elif ch < 't':
        return servers[2]
    else:
        return servers[3]


def hash_shard(word):
    "使用内建的hash算法分片"
    return servers[hash(word) % 4]


def md5_shard(word):
    "使用md5分片"
    data = word.encode('utf-8')
    return servers[hashlib.md5(data).digest()[-1] % 4]

if __name__ == '__main__':
    words = open('/usr/share/dict/words').read().split()
    for function in alpha_shard, hash_shard, md5_shard:
        d = {'server0': 0, 'server1': 0, 'server2': 0, 'server3': 0}
        for word in words:
            d[function(word.lower())] += 1
        print(function.__name__[:-6])
        for key, value in sorted(d.items()):
            print('   {} {} {:.2}'.format(key, value, value / len(words)))
        print()
