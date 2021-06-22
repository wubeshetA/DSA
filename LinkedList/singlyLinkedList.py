# Implementation of Linked List

class Node:
    """Node of a single element in the single list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # return the length of the linked list
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            currentNode = currentNode.next
            length += 1
        return length 

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
        if position > self.listLength() or position < 1:
            print("Invalid Position")
            return
        if position == 1:
            self.insertHead(newNode)
            return
        i = 1
        currentNode = self.head    
        previousNode = currentNode
        while i <= position:
            
            if i == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            i+=1
            
    # delete the node at the end of the linked list
    def deleteEnd(self):
        # steps
        # 1.Traverse until we the end of the list (when currentNode.next
        # is None)
        # 2. change previousNode.next to None - so that it lose connection 
        # in the list

        currentNode = self.head
        if self.listLength() == 1:
            self.head = None
            return
        previousNode = currentNode    
        while True:
            if currentNode.next is None:
                # del currentNode - this operation only delete the reference to
                # currentNode to the actual data in the memory.
                previousNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
      # prints the linked list
    
    # delete the head node
    def deleteHead(self):
        if self.listLength != 0:
            previousNode = self.head
            self.head = self.head.next
            previousNode.next = None
        else:
            print("List is empty. Deletion failed!")
      
    # delete a node between two nodes
    def deleteAt(self, position):
        # steps
        # 1. Traverse till the node to be deleted
        # 2. preserve the details of the previous node
        # 3. establish a connection betwee the previous node and the next node
        # of the current node.
        if position > self.listLength() or position < 1:
            print("Invalid position")
            return
        if self.listLength == 0:
            print("The LinkedList is empty")
            return         
        if position == 1:
            self.deleteHead()
            return
        currentPosition = 1
        currentNode = self.head
        
        while currentPosition < position:
            previousNode = currentNode
            currentPosition += 1
            currentNode = currentNode.next
        if currentNode.next is None:
            self.deleteEnd()    
            return
        previousNode.next = currentNode.next
        currentNode.next = None

    # print the linked list
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
            

def main():
    if __name__ == "__main__":

        linkedList = LinkedList()

        firstNode = Node("wube")
        linkedList.insertEnd(firstNode)
        secondNode = Node("Abe")
        linkedList.insertEnd(secondNode)
        thirdNode = Node("kebe")
        linkedList.insertEnd(thirdNode)

        fourthNode = Node("lemma")
        linkedList.insertAt(fourthNode, 3)
        linkedList.deleteAt(1)
        linkedList.printList()
        
        print("head: ",linkedList.head.data)
main()
