class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class SingleLinkedList:
    head = None
    def last(self, node = None):
        if(not node):
            node=self.head
        if(not node.next):
            return node
        else:
            return self.last(node.next)
    def insert(self, obj):
        if(not self.head):
            self.head = Node(obj)
        else:
            self.last().next = Node(obj)