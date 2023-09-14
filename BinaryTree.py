"""
Binary Tree
Each Pareent has two children.
      A
  B       C
D   E   F   G
Binary Trees can be represented as an array [A, B, C, D, E, F, G]


https://www.geeksforgeeks.org/complete-binary-tree/
"""

class BinaryTree():
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = BinaryTree(left)

    def set_right(self, right):
        self.right = BinaryTree(right)

    def get_value(self):
        return self.value

    def get_left(self):
        if self.left != None:
            return self.left.value
        return None
        
    def get_right(self):
        if self.right != None:
            return self.right.value
        return None

# class BinaryTree():
#     def __init__(self, h):
#         self.height = h
#         self.number_of_nodes = 2**(self.height+1)
