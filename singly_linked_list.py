class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node

    def search(self, key=None):
        last = self.head
        prev = None
        found = False

        while (last.next):
            if last.data == key:
                found = True
                break
            prev = last
            last = last.next

        if found == false and key != None:
            raise KeyError("%s not found" % key)

        return (prev, last)

    def add(self, data, key=None, before=False):
        if key == None:
            prev, last = self.search()
            new_node = Node(data)
            last.next = new_node
            new_node.prev = last
            return

        if before:
            if self.head.data == key:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            else:
                prev, last = self.search(key=key)
                new_node = Node(data)
                prev.next = new_node
                new_node.prev = prev
                new_node.next = last
                last.prev = new_node

        else:
            if self.head.data == key:
                new_node = Node(data)
                new_node.prev = self.head
                temp = self.head.next
                temp.prev = new_node
                self.head.next = new_node
                new_node.next = temp
            else:
                prev, last = self.search(key=key)
                temp = last.next
                new_node = Node(data)
                new_node.prev = last
                last.next = new_node
                new_node.next = temp
                temp.prev = new_node

    def remove(self, key):
        if self.head.data == key:
            self.head = self.head.next

        prev_node, node_to_remove = self.search(key=key)
        prev_node.next = node_to_remove.next


llist = LinkedList(1)
llist.add(2)
llist.add(3, key=2, before=True)
llist.add(4, key=3)
