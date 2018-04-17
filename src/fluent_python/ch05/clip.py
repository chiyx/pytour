# -*- coding: UTF-8 -*-

from inspect import signature


def clip(text, max_len=80):
    """
    在max_len前面或者后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
    return text[:end].rstrip()


def clip2(text: str, max_len: 'int > 0'=80) -> str:
    """
    在max_len前面或者后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
    return text[:end].rstrip()


def main():
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    sig = signature(clip)
    print(sig)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
    print(clip2.__annotations__)

if __name__ == '__main__':
    main()
