# Implementation of Linked List

class Node:
    """Node of a single element in the single list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert new Node at the end of the linked list 
    def insertEnd(self, newNode):

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

    # insert New as the head of the Linked list        
    def insertHead(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            oldHead = self.head
            self.head = newNode
            self.head.next = oldHead
            del oldHead

    # insert a new node between to nodes
    def insertAt(self, newNode, position):
        
        if position == 1:
            self.insertHead(newNode)
            return
        i = 1
        currentNode = self.head    
        while i <= position:
            
            if i == position:
                previousNode.next = newNode
                newNode.next = currentNode
                # followingNode = precedingNode.next
                # precedingNode.next = newNode
                # newNode.next = followingNode
                # del followingNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            i+=1
            

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
linkedList.insertEnd(firstNode)
secondNode = Node("Abe")
linkedList.insertEnd(secondNode)
thirdNode = Node("kebe")
linkedList.insertEnd(thirdNode)

fourthNode = Node("lemma")
linkedList.insertAt(fourthNode, 2)
linkedList.printList()

print("head: ",linkedList.head.data)