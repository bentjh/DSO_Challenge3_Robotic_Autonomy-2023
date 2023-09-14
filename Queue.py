class Queue():
    """ 
    https://www.geeksforgeeks.org/introduction-to-queue-data-structure-and-algorithm-tutorials/
    """
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def enqueue(self, value):
        # insertion of data
        pass

    def dequeue(self, index = 0):
        # removal of data from queue
        pass

    def front(self):
        return self.buffer[0]
    
    def rear(self):
        return self.buffer[-1]
    
    def is_full(self):
        if len(self.buffer) == self.capacity:
            return True
        return False
    
    def is_null(self):
        if len(self.buffer) == 0:
            return True
        return False
    
class PriorityQueue():
    """
    https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
    """
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def insert_queue(self, value):
        pass

