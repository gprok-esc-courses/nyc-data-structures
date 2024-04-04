
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'
    
    def __str__(self) -> str:
        return str(self.value)
    
class RedBlackTree:
    def __init__(self) -> None:
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        node = TreeNode(value)
        if self.is_empty():
            self.root = node
        else:
            iter = self.root
            added = False
            while not added:
                if value > iter.value:
                    if iter.right is None:
                        iter.right = node
                        node.parent = iter
                        added = True
                    else:
                        iter = iter.right
                else:
                    if iter.left is None:
                        iter.left = node
                        node.parent = iter
                        added = True
                    else:
                        iter = iter.left

    def rb_insert_fixup(self):
        pass

    def remove(self, value):
        node = self.find(value)
        if node is not None:
            if self.is_leaf(node):
                if node == self.root:
                    self.root = None
                else:
                    if node.value < node.parent.value:
                        node.parent.left = None
                    else:
                        node.parent.right = None
            elif self.has_single_child(node):
                if node == self.root:
                    self.root = node
                else: 
                    if node.value < node.parent.value:
                        if node.left is not None:
                            node.parent.left = node.left
                        else:
                            node.parent.left = node.right
                    else:
                        if node.left is not None:
                            node.parent.right = node.left
                        else:
                            node.parent.right = node.right
            else:
                next = self.successor(node)
                if next is not None:
                    v = next.value
                    self.remove(next.value)
                    node.value = v

    def remove_fixup(self, x):
        pass

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    