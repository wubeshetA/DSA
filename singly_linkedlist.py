"""My implementation of singly linked list

Time complexity:
 Read - O(n)
 Insert - O(1)
 Delete - O(n)
"""

# Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Singly linked list 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __isempty(self):
        return self.head is None
    
    def append(self, data):
        node = Node(data)
        if self.__isempty():
            # if there is no head
            # create a new node
            
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def prepend(self, data):
        node = Node(data)
        if self.__isempty():
            # if there is no head
            # create a new node
            
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
        
    def display(self):
        # node(1) -> node(2) -> node(3)
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
    def reverse(self):
        current = self.head
        previous = None
        if current is not None: 
            self.tail = current
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            # next_node.next = current
        
        self.head = previous
    def deleteAll(self, data):
        current = self.head
        previous = None
        while current:
            # when current data is equal to target data
            if current.data == data:
                # node to be deleted is in the middle of the linked list
                if previous:
                    previous.next = current.next
                    
                    current = current.next
                    # del current
                # node to be deleted is the head node
                else:
                    self.head = current.next
                    current = self.head
                    # del current
            # else
            else:
                previous = current
                current = current.next
            
        
            
if __name__ == "__main__":
        
    my_linked_list = SinglyLinkedList()    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    # print(node1.data)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.prepend(5)
    my_linked_list.prepend(5)
    my_linked_list.append(5)
    # my_linked_list.append(4)
    my_linked_list.display()
    print("head:", my_linked_list.head.data)
    print("tail: ", my_linked_list.tail.data)
    # my_linked_list.reverse()
    # my_linked_list.display()
    # print("head:", my_linked_list.head.data)
    # print("tail: ", my_linked_list.tail.data)
    print('----delete-------')
    my_linked_list.deleteAll(3)
    my_linked_list.display()

