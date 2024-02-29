class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node 

    def search(self, data):
        current = self.head 
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data):
        if not self.head:
            return 

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head 
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        if self.head.data > data:
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next 
        print('->'.join(output))

class DLL(LL):
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        node = self.search(data)
        if not node:
            return
        if node == self.head:
            self.head = self.head.next
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


elements = [0,1,2,3,4,5,6,7,8,9]

dll = DLL()
for e in elements:
    dll.append(e)

dll.print()

dll.delete(0)
dll.delete(5)
dll.delete(9)
dll.print()
