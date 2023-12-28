class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, current, data):
        if not self.root:
            self.root = Node(data)
            return
        
        if data < current.value:
            if not current.left:
                current.left = Node(data)
            else:
                self.insert(current.left, data)
        else:
            if not current.right:
                current.right = Node(data)
            else:
                self.insert(current.right, data)

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.value, end=' ')
            self.inorder(current.right)

    def preorder(self, current):
        if current:
            print(current.value, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.value, end=' ')

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

    def find_key(self, current, key):
        if not current:
            print("Key Not Found")
            return

        if current.value == key:
            print(f"{key} Found")
            return

        if key < current.value:
            self.find_key(current.left, key)
        else:
            self.find_key(current.right, key)


if __name__ == '__main__':
    bst = BinarySearchTree()

    TreeElements = [5,7,4,2,10,20,9,5]

    for i in TreeElements:
        bst.insert(bst.root, i)
    
    bst.inorder(bst.root)
    print()

    bst.preorder(bst.root)
    print()

    bst.postorder(bst.root)
    print()

    bst.level_travarse(bst.root)
    print()

    bst.find_key(bst.root, 5)

    bst.find_key(bst.root, 100)
