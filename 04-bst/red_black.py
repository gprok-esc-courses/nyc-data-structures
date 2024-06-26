
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'
        # next variables is used by pretty print
        self.level = 0
        self.tree_layout = []

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
            node.color = 'black'
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
            # print("BEFORE")
            # bst.pretty_print_tree()
            self.rb_insert_fixup(node)
            # print("AFTER")
            # bst.pretty_print_tree()
            # x = input("continue, click any key")

    
    def is_root(self, x):
        return x.parent is None

    def is_left_child(self, x):
        return x == x.parent.left

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x 
        y.parent = x.parent
        if self.is_root(x):
            self.root = y
        elif self.is_left_child(x):
            x.parent.left = y 
        else:  # is right child
            x.parent.right = y
        y.left = x 
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x 
        y.parent = x.parent
        if self.is_root(x):
            self.root = y
        elif self.is_left_child(x):
            x.parent.left = y 
        else:  # is right child
            x.parent.right = y
        y.right = x 
        x.parent = y
         

    def rb_insert_fixup(self, z):
        while z.parent is not None and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == 'red':        # Case 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z  = z.parent.parent
                elif z == z.parent.right:  # Case 2
                    z = z.parent
                    self.left_rotate(z)
                else: # z.parent is not None and z.parent.parent is not None:
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:  # parent is right child of grandparent
                y = z.parent.parent.left
                if y is not None and y.color == 'red':        # Case 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z  = z.parent.parent
                elif z == z.parent.left:  # Case 2
                    z = z.parent
                    self.right_rotate(z)
                else: # z.parent is not None and z.parent.parent is not None:
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'black'

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
            print(node.value, '(', node.color, ')')
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.value, '(', node.color, ')')
            self.preorder(node.left)
            self.preorder(node.right)

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
        
    def pretty_print_tree(self):
        self.level = -1
        h = self.height(self.root)
        self.tree_layout = [[] for i in range(h)]
        self.pretty_print_recursion(self.root, h)
        for row in self.tree_layout:
            print(row)


    def pretty_print_recursion(self, node, h):
        self.level += 1
        if self.level < h:
            if node is None:
                self.tree_layout[self.level].append('N-b')
            else:
                self.tree_layout[self.level].append(str(node.value)+"-"+node.color[0])
                self.pretty_print_recursion(node.left, h)
                self.pretty_print_recursion(node.right, h)
        self.level -= 1




if __name__ == "__main__":
    bst = RedBlackTree()
    # data = [100, 80, 70, 90, 45, 85, 94] # , 130, 120, 140, 135]
    # data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
    # data = [100, 80, 40, 90, 85, 95, 130, 110, 140]
    # data.sort(reverse=True)
    for v in range(1, 1000000):
        bst.insert(v)
    # bst.preorder(bst.root)
    # print("ROOT:", bst.root.value)
    # print("HEIGHT:", bst.height(bst.root))
    # bst.pretty_print_tree()
    print(bst.height(bst.root))
    
    