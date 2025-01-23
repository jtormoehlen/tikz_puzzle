

class BinaryTree:

    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def get_root(self):
        return self.root
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def is_empty(self):
        return self.root is None


def depth_first_search(binary_tree):
    if binary_tree.get_root() is not None:
        print(binary_tree.get_root())
        depth_first_search(binary_tree.get_left())
        depth_first_search(binary_tree.get_right())

binary_tree = BinaryTree(3, BinaryTree(2, BinaryTree(5, BinaryTree(), BinaryTree()), BinaryTree(8, BinaryTree(), BinaryTree())), BinaryTree(9, BinaryTree(7, BinaryTree(), BinaryTree()), BinaryTree()))
depth_first_search(binary_tree)