#! /usr/bin/env python3
# coding = utf-8

# link_list.py - linkList 的实现


class LinkedListUnderlow(ValueError):
    pass


class LNode:

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:

    def __init__(self):
        self._head = None
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self._num += 1

    def pop(self):
        if self._num == 0:
            raise LinkedListUnderlow("in pop")
        p = self._head
        e = p.elem
        self._head = p.next
        self._num -= 1
        return e

    def append(self, elem):
        self._num += 1
        if self._num == 0:
            self._head = LNode(elem)
            return
        # 找到最后一个元素
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        return

    def pop_last(self):
        if self._num == 0:
            raise LinkedListUnderlow('in pop_last')
        self._num -= 1
        p = self._head
        # 表中只有一个元素时
        if p.next is None:
            e = p
            self._head = None
            return e
        # 表中存在2个元素以上时，找到倒数第二个元素
        while p.next.next is not None:
            p = p.next
        e = p.next
        p.next = None
        return e

    def find(self, elem):
        p = self._head
        while p is not None:
            if p.elem == elem:
                return p.elem
            p = p.next
        return None

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def size(self):
        return self._num

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def elements(self):
        "遍历生成器"
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        "过滤生成器"
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def __str__(self):
        return '[' + ",".join([str(x) for x in self.elements()]) + ']'

    def __len__(self):
        return self._num

if __name__ == "__main__":
    llist = LList()
    for i in range(10):
        llist.prepend(i)
    print('llist size: %s' % (len(llist)))
    print(llist)
    llist.pop()
    llist.pop_last()
    llist.append(10)
    print('llist size: %s' % (len(llist)))
    print(llist)
    llist.rev()
    print('llist size: %s' % (len(llist)))
    print(llist)
