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

    def gen_bracket(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in brackets:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for br, i in gen_bracket(text):
        if br in open_bracket:
            st.push(br)
        elif st.pop() != opposite[br]:
            print("Mismatch is found at", i, "for", br)
            return False
    if not st.is_empty():
        print("Some brackets are not matched at the end")
    else:
        print("All brackets are correctly matched")
