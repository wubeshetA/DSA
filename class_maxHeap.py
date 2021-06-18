class MaxHeap:
    """ wrapper class for max heap """
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.push(item)
            self.__floatUp(len(self.heap)-1)

    # push data to the correct position of the heap
    def push(self, data):
        
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    # peeks the root element(max) of the heap
    def peek(self):
        return self.heap[1]

    # pop(delete) the root element(max) of the heap
    def pop(self):
        
        if len(self.heap) == 2:
            removed = self.heap.pop()
        elif len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            removed = self.heap.pop()
            self.__bubbleDown(1)
        else:
            False    
        return removed

    # swap two elements
    def __swap(self, index1, index2):
        
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # float (move up) a data up the heap to put it on the correct position in the heap
    def __floatUp(self, index):
        
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
      
    # bubble a data down the heap to put it on the correct position
    def __bubbleDown(self, index):
        left = 2 * index
        right = 2 * index + 1
        largest = index
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)    

    # returns string representation of maxHeap
    def __str__(self):
        return str(self.heap[1:])
        

lst = MaxHeap([8,2,3,1,7,4,6,5,9])
print(lst.pop())
print(lst)
