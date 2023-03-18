"""Linked List implementation
"""

# task
# 1. create a node
# 2. add it's attributes (item and next pointer)
# 3. add head pointer - variable that points to the first node
# 4. Insertion at the tail
# 5. insertion at the head
# 6. insertion any where
# 4. deletion at the tail
# 5. deletion at the head
# 6. deletion any where

class Node:
    
    def __init__(self, data):
        """ Initialize Node

        Args:
            data (any): Stores the actual data
        """
        self.data = data # store the actual data
        self.next = None # points to the next node in the linear order

class LinkedList:
    
    def __init__(self, *args):
        self.head = None
        self.tail = None
        
        if args is not None:
            for data in args:
                node = Node(data)
                self.insert_tail(node)
            
        
    def length(self):
        
            counter = 0
            current = self.head
            while type(current) is Node:
                counter += 1
                current = current.next
            return counter
        
    def insert_head(self, head):
        head.next = self.head
        self.head = head
        if self.length() == 1:
            self.tail = head

    def insert_tail(self, tail):
        if self.head is None:
            self.insert_head(tail)
        self.tail.next = tail
        self.tail = tail
        
        
    def insert_at(self, node, index):
        pass
    def get_at(self, index):
        pass
    def delete(self, index):
        pass
    def delete_head(self):
        pass
    def delete_tail(self):
        pass
    
    def __str__(self) -> str:
        current = self.head
        list_data = []
        # list_data.append(current.data)
        while type(current) is Node:
            list_data.append(current.data)
            current = current.next
            
        return str(list_data)
    
    
        
        
if __name__ == "__main__":
    
    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(6)
    
    
lst = LinkedList(2,3)
# lst.insert_head(node1)
# lst.insert_tail(node2)
# lst.insert_tail(node3)

print(lst.length())
print(lst)