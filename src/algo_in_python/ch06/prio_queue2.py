#! /usr/bin/env python3
# coding = utf-8

# prio_queue2.py - 裸写基于堆的优先级队列


class PrioQueueError(ValueError):
    "优先级队列操作中的异常定义"
    pass


class PrioQueue:
    "基于堆的优先级队列实现"

    def __init__(self, elems=[]):
        # 内部的堆使用列表实现，复制方式可以避免可变参数带来的副作用
        self._elems = list(elems)
        # TODO 建堆，待实现

    def is_empty(self):
        return not self._elems

    def peek(self):
        "获取对头元素"
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[0]

    def enqueue(self, e):
        "进队操作"
        # 将元队列扩展一个空间，但此时并不将元素放入
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def dequeue(self):
        "出队操作"
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        # 堆顶元素出队, 作为返回值
        e0 = elems[0]
        #
        e = elems.pop()
        return e0

    def siftup(self, e, last):
        "从last位置开始，不断向上筛选, 直到确定e的位置，并将其放入"
        # i: 待插入的位置，j: i的父亲节点
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def siftdown(self, e, begin, end):
        "从start位置开始，不断向下晒选, 直到确认e的位置"
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            # 确保j指向的元素不大于其兄弟节点
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            # 如果e在3个节点中最小, 表示已找到插入位置
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    def buildheap(self):
        """ 建堆，将列表看成一个完全二叉树，从end//2位置开始，
            后面的表元素都是叶子节点，即已经是堆了，
            从这个位置开始向前面做向下晒选的逻辑，就可将这个表
            构建成一个堆
        """
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)


def heap_sort(elems):
    """ 堆排序
        1. 基于列表建立一个大顶堆
        2. 不断将堆顶元素弹出，并放入列表的后部
    """
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:
            # 因为是大顶堆，需要确保j指向的元素不小于其兄弟节点
            if j + 1 < end and elems[j + 1] > elems[j]:
                j += 1
            if e > elems[j]:
                break
            # elems[j] 最大，上移
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    end = len(elems)
    # 建堆
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)
    # 将堆顶元素不断弹出放入列表后部，然后将置换出的元素放入堆顶，执行向下晒选
    # 以保持堆的性质
    for i in range(end - 1, 0, -1):
        # e保存被堆顶元素置换出的元素
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)

if __name__ == '__main__':
    elems = [1, 3, 9, 0, 10, 5, 5, 7, 6]
    heap_sort(elems)
    print(elems)
