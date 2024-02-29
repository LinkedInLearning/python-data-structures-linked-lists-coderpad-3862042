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
                return True
            current = current.next
        return False

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




#      3   0   0   0   4
#      0   0   2   0   0
#      0   1   0   0   0
#      0   0   0   0   0
# OLL(row, col)
oll = OLL(4, 5)
oll.insert(ONode(3, 0, 0))
oll.insert(ONode(4, 0, 4))
oll.insert(ONode(2, 1, 2))
oll.insert(ONode(1, 2, 1))

oll.print()

