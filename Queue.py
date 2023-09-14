class Queue():
    """ 
    https://www.geeksforgeeks.org/introduction-to-queue-data-structure-and-algorithm-tutorials/
    """
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def enqueue(self, value):
        # insertion of data
        if self.is_full():
            return "Error. Queue is Full"
        self.buffer.append(value)
        print(f"Success. {self.rear()} added to queue")
            
    def dequeue(self):
        # removal of data from queue
        if self.is_null():
            return "Error. Queue is Empty"
        print(f"Success. {self.buffer.pop(0)} removed from queue")

    def front(self):
        if self.is_null():
            return "Error. Queue is Empty"
        return self.buffer[0]
    
    def rear(self):
        if self.is_null():
            return "Error. Queue is Empty"
        return self.buffer[-1]
    
    def is_full(self):
        return len(self.buffer) == self.capacity
    
    def is_null(self):
        return len(self.buffer) == 0
    
    
from BinaryTree import BinaryTree
class PriorityQueue(Queue, BinaryTree):
    """
    https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
    """
    def __init__(self, capacity):
        self.Queue = Queue(capacity)
        self.BinaryTree = BinaryTree()

    def insert_queue(self, value):
        pass

