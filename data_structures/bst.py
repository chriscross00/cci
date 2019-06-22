# https://gist.github.com/jakemmarsh/8273963


class Node:

    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

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

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, current, val):
        if current is None:
            return False
        elif current.val == val:
            return True
        elif current.val > val:
            return self.find_node(current.left_child, val)
        else:
            return self.find_node(current.right_child, val)

    def inorder_helper(self, node):
        if node:
            self.inorder_helper(node.left_child)
            print(node.val)
            self.inorder_helper(node.right_child)

    def inorder(self):
        print('inorder')
        self.inorder_helper(self.root)


r = BST()
r.insert(50)
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(70)
r.insert(60)
r.insert(80)

r.inorder()

