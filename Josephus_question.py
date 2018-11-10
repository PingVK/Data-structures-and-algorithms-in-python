"""
假设有n个人围坐一圈，现在要求从第k个人开始报数，报到第m个数的人退出。然后从下一个人开始继续报数并按相同规则退出，
直至所有人退出。
要求按顺序输出各出列人的编号。
"""

from LinkedList import LCList


def josephus_a(n, k, m):
    """Based on array"""
    people = list(range(1, n+1))
    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end='')
                people[i] = 0
            i = (i+1) % n
        if num < n-1:
            print(', ', end='')
        else:
            print()


def josephus_l(n, k, m):
    """Based on list"""
    people = list(range(1, n+1))
    i = k-1
    for num in range(n, 0, -1):
        i = (i+m-1) % num
        print(people.pop(i), end=(', 'if num > 1 else '\n'))


class Josephus(LCList):
    """Based on cyclic single linked list"""
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        super().__init__()
        for i in range(1, n+1):
            self.append(i)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(), end=('\n' if self.is_empty() else ', '))


if __name__ == '__main__':
    josephus_a(10, 2, 7)
    josephus_l(10, 2, 7)
    Josephus(10, 2, 7)
