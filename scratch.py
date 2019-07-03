# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem


# Implement a bst

class Node:

    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


# left < val
# val < right
class BST:

    def __int__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(val)

    def insert_node(self, current, val):
        if val <= current.val:
            if current.left_child:
                self.insert_node(current.left_child, val)
            else:
                current.left_child = Node(val)
        elif val > current.val:
            if current.right_child:
                self.insert_node(current.right_child, val)
            else:
                current.right_child = Node(val)

    def inorder_helper(self, node):
        if node:
            self.inorder_helper(node.left_child)



