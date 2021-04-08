class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def reverse_str(s):
    stack = Stack()

    for char in s:
        stack.push(char)

    temp_str = ""

    while not stack.is_empty():
        temp_str += stack.pop()

    return temp_str

def test_reverse_str():
    assert reverse_str("racecar") == reverse_str("racecar")
    assert reverse_str("SDGKU") == reverse_str("UKGDS")
    assert reverse_str("ping pong") == reverse_str("gnop gnip")


