# -*- coding: UTF-8 -*-

import os
import warnings
import json
import keyword
from urllib.request import urlopen
from collections import abc


class FrozenJSON:
    """
    一个只读接口，使用属性表示法访问JSNO类对像
    """

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableMapping):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self._data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self._data[key] = value

    def __getattr__(self, name):
        if (hasattr(self._data, name)):
            return getattr(self._data, name)
        else:
            return FrozenJSON(self._data[name])


URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


def main():
    raw_feed = load()
    for key, value in sorted(raw_feed['Schedule'].items()):
        print('{:5} {}'.format(len(value), key))
    feed = FrozenJSON(raw_feed)
    print(len(feed.Schedule.speakers))

    grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    print(grad.class_)


if __name__ == '__main__':
    main()
