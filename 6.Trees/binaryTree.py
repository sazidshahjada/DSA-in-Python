class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, current, value):
        if not self.root:
            self.root = Node(value)
            return
        
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if not current.left:
                current.left = Node(value)
                break
            elif not current.right:
                current.right = Node(value)
                break
            else:
                queue.append(current.left)
                queue.append(current.right)
        

    def level_travarse(self, current):
        if not self.root:
            return
        
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            print(current.value, end=' ')

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.value, end=' ')
            self.inorder(current.right)

    def delete_leaf(self, current):
        if not self.root:
            return
        
        queue = [self.root]

        while queue:
            current = queue.pop(-1)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            if current.right and not current.right.left and not current.right.right:
                current.right = None
                break
            if current.left and not current.left.left and not current.left.right:
                current.left = None
                break
            


if __name__ == '__main__':
    bt = BinaryTree()

    my_list = [1,2,3,4,5,6,7]

    for i in my_list:
        bt.insert(bt.root, i)

    bt.level_travarse(bt.root)
    print()

    bt.inorder(bt.root)
    print()

    bt.delete_leaf(bt.root)

    bt.level_travarse(bt.root)
    print()

    bt.delete_leaf(bt.root)

    bt.level_travarse(bt.root)
    print()

    bt.inorder(bt.root)
    print()
    
        
