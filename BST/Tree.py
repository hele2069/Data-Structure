
class TreeNode(object):
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

    def is_empty(self):
        return self.left is None and self.right is None

    def insert(self, item):
        if self.value == item:
            return
        if self.value > item:
            if self.left:
                self.left.insert(item)
            else:
                self.left = TreeNode(item)
        else:
            if self.right:
                self.right.insert(item)
            else:
                self.right = TreeNode(item)

    def find(self, item):
        if self.value == item:
            return True
        if self is None:
            return False
        if self.value > item:
            return self.left.find(item)
        if self.value < item:
            return self.right.find(item)

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    def preorder(self):
        elements = [self.value]
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.value)
        if self.right:
            elements += self.right.inorder()
        return elements

    def postorder(self):
        elements = [self.value]
        if self.left:
            elements += self.left.Pre_Order_Traversal()
        if self.right:
            elements += self.right.Pre_Order_Traversal()

        return elements
