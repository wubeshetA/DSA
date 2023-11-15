""" This is my implementation of Doubly linked list
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublylinkedList:
    def __init__(self, data=None):
        
        self.head = None
        self.tail = None
    
    
    def append(self, data):
        node = Node(data)
        
        if not self.head:
            
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
    def __str__(self) -> str:
        print_value = ""
        current = self.head
        while current:
            print_value =  print_value + str(current.data) + " "
            current = current.next
        return print_value

if __name__ == '__main__':
    db_list = DoublylinkedList()
    db_list.append(1)
    db_list.append(2)
    db_list.prepend(3)
    db_list.prepend(5)
    print(db_list.tail.data)
    print(db_list)