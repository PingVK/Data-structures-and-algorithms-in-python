from LinkedList import LNode


class StackUnderflow(ValueError):
    pass


class SStack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if not self._elems:
            raise StackUnderflow("in SStack.top()")
        else:
            return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if not self._elems:
            raise StackUnderflow("in SStack.pop()")
        else:
            return self._elems.pop()


class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self.top.elem

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem


def check_brackets(text):
    """Bracket pair check function"""
    brackets = "()[]{}"
    open_bracket = "([{"
    opposite = {")": "(", "]": "{", "}": "{"}
