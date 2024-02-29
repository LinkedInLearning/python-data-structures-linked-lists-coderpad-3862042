import random
import sys

sys.setrecursionlimit(2000)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def search(self, data):
        if self.data == data:
            return True
        if self.next:
            return self.next.search(data)

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

    #def search(self, data):
    #    return self.head.search(data)

    def search(self, data):
        current = self.head 
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

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

print(ll.search(5))

print(ll.search(10))