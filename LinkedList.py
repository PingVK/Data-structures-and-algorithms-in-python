class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
        return -1

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print()

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort1(self):
        if self._head or self._head.next is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem < x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    def sort(self):
        if self._head or self._head.next is None:
            return
        p = self._head
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p


class LList1(LList):
    """Tail node"""
    def __init__(self):
        super(LList1, self).__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)  # add
            self._rear = self._rear.next  # move

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            # self._rear = None  # it can be ignored when we uniformly use _head to judge a empty linked_list
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        self._rear = p
        p.next = None
        return e

    def rev(self):
        self._rear = self._head
        LList.rev(self)


class LCList:
    """Cyclic single linked list"""
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            if p is self._rear:
                print(p.elem)
                break
            else:
                print(p.elem, end=', ')
            p = p.next

    def rev(self):
        p, end = self._rear, self._rear.next
        self._rear = p.next
        while True:
            q = self._rear
            self._rear = q.next
            q.next = p
            p = q
            if self._rear is end:
                break


class DLNode(LNode):
    """Double Linked Node"""
    def __init__(self, elem, prev=None, next_=None):
        super(DLNode, self).__init__(elem, next_)
        self.prev = prev


class DLList(LList1):
    def __init__(self):
        super(DLList, self).__init__()

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        # else:
        #     self._rear = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

    def rev(self):
        pass


if __name__ == "__main__":
    mlist = LList()
    for i in range(10):
        mlist.append(i)
    mlist.printall()

    # mlist1 = LList1()
    # mlist1.prepend(99)
    # for i in range(11, 20):
    #     mlist1.append(i)
    # for x in mlist1.filter(lambda y: y % 2 == 0):
    #     print(x, end=' ')
    # print()

    # lclist = LCList()
    # for i in range(10):
    #     lclist.append(i)
    # lclist.printall()
    # lclist.rev()
    # lclist.printall()
