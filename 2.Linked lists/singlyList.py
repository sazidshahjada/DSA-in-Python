class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

    def insert_last(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = newNode

    def insert_first(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_at(self, idx, data):
        if idx <= 1:
            self.insert_first(data)
            return
        
        newNode = Node(data)
        current = self.head

        for _ in range(idx - 2):
            if current:
                current = current.next
            else:
                print("Index out of range")
                return
            
        if not current:
            print("Index out of range")
            return
        
        newNode.next = current.next
        current.next = newNode

    def delete_last(self):
        if not self.head:
            print("Index out of range")
            return
        
        if not self.head.next:
            self.head = None
            return
        
        current = self.head

        while current.next.next:
            current = current.next
        
        current.next = None

    def delete_first(self):
        if not self.head:
            print("Index out of range")
            return
        
        if not self.head.next:
            self.head = None
            return
        
        self.head = self.head.next

    def delete_at(self, idx):
        if idx == 0:
            self.delete_first()
            return
        
        current = self.head
        for _ in range(idx - 1):
            if current:
                current = current.next
            else:
                print("Index out of range")
                return
            
        if not current or not current.next:
            print("Index out of range")
            return
        
        current.next = current.next.next
        
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.printList()
    ll.insert_first(10)
    ll.printList()
    ll.insert_last(100)
    ll.printList()
    ll.insert_last(200)
    ll.printList()
    ll.insert_at(2, 50)
    ll.printList()
    ll.delete_at(3)
    ll.printList()
