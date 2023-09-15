from BinaryTree import BinaryTree
from Queue import Queue
"""
Rule:
1. value on left > value of parent. 
2. value on left < value on right
"""
class PriorityQueue(Queue, BinaryTree):
    """
    https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
    """
    def __init__(self, capacity, ascending = True):
        self.Queue = Queue(capacity)
        self.BinaryTree = BinaryTree()
        self.ascending = ascending

    def add_to_queue(self, value):
        node = self.BinaryTree
        if self.ascending:
            while value >= node.value:
                if value >= node.left.value and value < node.right.value:
                    node = node.left
                else:
                    node = node.right
