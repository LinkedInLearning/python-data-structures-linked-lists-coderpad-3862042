import random

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

    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next 
        print('->'.join(output))

elements = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(elements)
ll = LL()
for e in elements:
    ll.append(e)

ll.print()