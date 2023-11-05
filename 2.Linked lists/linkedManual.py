
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def printNode(head):
    while True:
        print(head.value, end=' ')
        head = head.next
        if head is None:
            break
    print()

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4


    printNode(head)
        