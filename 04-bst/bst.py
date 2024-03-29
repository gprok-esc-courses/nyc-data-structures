
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
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

    def preorder(self, node):
        if node is not None:
            self.preorder(node.left)
            print(node.value)
            self.preorder(node.right)

    def find(self, value):
        iter = self.root
        while iter is not None:
            if iter.value == value:
                return iter
            elif iter.value > value:
                iter = iter.left
            else:
                iter = iter.right
        return None
    
    def is_leaf(self, node):
        return node.left is None and node.right is None
    
    def has_single_child(self, node):
        return node.left is None or node.right is None
    
    def successor(self, node):
        if node.right is None:
            return None
        else: 
            iter = node.right
            while iter.left is not None:
                iter = iter.left
            return iter
    
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

    def max(self):
        pass

    def min(self):
        pass

    def inorder(self, node):
        pass

    def postorder(self, node):
        pass

    def preorder_iterative(self, node):
        pass

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
                


if __name__ == "__main__":
    bst = BinarySearchTree()
    data = [100, 80, 70, 90, 45, 85, 94, 130, 120, 140, 135]
    for v in data:
        bst.insert(v)
    bst.preorder(bst.root)
    print("Search 94: ", bst.find(94))
    print("Search 88: ", bst.find(88))
    bst.remove(140)
    bst.preorder(bst.root)
    # print("Successor 100: ", bst.successor(bst.root))
    print(bst.height(bst.root))

