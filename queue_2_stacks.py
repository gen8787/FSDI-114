class Queue2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        pass

    def dequeue(self, element):
    pass


def test():
    # 0, 1, 2, 3, 4
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)

    for i in range(5):
        print(q.dequeue())
