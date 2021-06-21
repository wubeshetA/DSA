# Implementation of Linked List

class Node:
    """Node of a single element in the single list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):

        # head -> wube
        if self.head is None:
            self.head = newNode

        # head -> wube => Abe => kebe    
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = self.head.next
                next
            lastNode.next = newNode
    
    # prints the linked list
    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        currentNode = self.head    
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
linkedList = LinkedList()

firstNode = Node("wube")
linkedList.insert(firstNode)
secondNode = Node("Abe")
linkedList.insert(secondNode)
thirdNode = Node("kebe")
linkedList.insert(thirdNode)

fourthNode = Node("lemma")
# linkedList.insertHead(fourthNode)
linkedList.printList()

print("head: ",linkedList.head.data)