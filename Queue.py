class QueueUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class SQueue:
    """基于顺序表的队列实现"""
    def __init__(self, init_len=8):
        self._len = init_len    # 存储区长度
        self._elems = [0]*init_len  # 元素
        self._head = 0  # 表头元素下标
        self._num = 0   # 元素个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow("in peek of SQueue")
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow("in dequeue of SQueue")
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]
        self._elems, self._head = new_elems, 0

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = e
        self._num += 1


class LQueue:
    """基于链表的队列实现"""
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, e):
        if self._head is None:
            self._head = LNode(e)
            self._rear = self._head
        else:
            self._rear.next = LNode(e)
            self._rear = self._rear.next

    def dequeue(self):
        if self._head is None:
            raise QueueUnderflow("in dequeue of LQueue")
        e = self._head.elem
        self._head = self._head.next    # 此处尾节点可以不考虑
        return e

    def peek(self):
        if self._head is None:
            raise QueueUnderflow("in peek of LQueue")
        return self._head.elem
