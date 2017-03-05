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
        "列表反转"
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort(self):
        "列表排序"
        # 空列表或者只有一个元素列表无需排序
        if self._head is None or self._head.next is None:
            return
        # 将元列表分成2个部分: 已排序段和未排序段，原本的_head指向以排序段，rem 指向未排序的列表
        rem = self._head.next
        self._head.next = None
        # 如果还有未排序的列表元素
        while rem is not None:
            p = self._head
            # q 指向需要插入位置的前一个元素
            q = None
            # 找出未排序列表第一个元素的插入位置
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            # 如果rem当前元素比已排序列表都小，表示需要插入到表头
            if q is None:
                self._head = rem
            # 否则将q.next即为rem当前元素需要插入的位置
            else:
                q.next = rem
            # 从未排序列表中断开rem当前指向的元素，并后移rem
            q = rem
            rem = rem.next
            # 链接后续排序的元素
            q.next = p

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

    def __getitem__(self, i):
        index = i if i >= 0 else self._num + i
        print(index, self._num)
        if index >= self._num:
            raise LinkedListUnderlow('in []')
        n = 0
        p = self._head
        while n != index:
            n += 1
            p = p.next
        return p.elem


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
    llist.sort()
    print(llist)
    print(llist[8])
