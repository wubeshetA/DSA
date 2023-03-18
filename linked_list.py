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
        self.head = self.next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    def list_length(self, head):
        if type(head) == Node:
            counter = 1
            current = head
            while current.next != None:
                current = current.next
                counter += 1
            return counter
        
    