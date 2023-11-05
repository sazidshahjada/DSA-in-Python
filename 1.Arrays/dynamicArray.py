
class DynamicArr:
    def __init__(self) -> None:
        self.Arr = []
        self.Size = 0

    def length(self):
        return self.Size
    
    def build(self, X):
        self.Arr = [i for i in X]
        self.Size = len(X)

    def itr(self):
        for i in range(self.Size):
            print(self.Arr[i], end=' ')
        print()

    def get_at(self, idx):
        if 0 <= idx < self.Size:
            return self.Arr[idx]
        else:
            return 'Index Out of Range'
    
    def set_at(self, idx, x):
        if 0 <= idx < self.Size:
            self.Arr[idx] = x
        else:
            print('Index Out of Range')

    def item_idx(self, k):
        for i in range(self.Size):
            if self.Arr[i] == k:
                return i
        return 'No Existance'
    
    def insert_first(self, x):
        self.Arr += [x]
        self.Size += 1
        for i in range(self.Size - 2, - 1, -1):
            self.Arr[i + 1] = self.Arr[i]
        self.Arr[0] = x

    def insert_last(self, x):
        self.Arr = self.Arr + [x]
        self.Size += 1

    def insert_at(self, idx, x):
        self.Arr += [None]
        self.Size += 1
        for i in range(self.Size - 2, idx - 1, -1):
            self.Arr[i + 1] = self.Arr[i]
        self.Arr[idx] = x

    def delete_last(self):
        self.Size -= 1
    
    def delete_first(self):
        for i in range(1, self.Size):
            self.Arr[i - 1] = self.Arr[i]
        self.Size -= 1
    
    def delete_at(self, idx):
        for i in range(idx + 1, self.Size):
            self.Arr[i - 1] = self.Arr[i]
        self.Size -= 1
    
if __name__ == '__main__':
    myArr = DynamicArr()

    myArr.build([1,2,3,4,5])
    print(myArr.length())
    myArr.itr()
    print(myArr.get_at(3))
    myArr.set_at(0, 10)
    myArr.itr()
    print(myArr.get_at(7))
    myArr.set_at(10, 10)
    myArr.itr()
    myArr.insert_last(100)
    myArr.itr()
    print(myArr.length())
    myArr.insert_first(200)
    myArr.itr()
    print(myArr.length())
    myArr.insert_at(2, 500)
    myArr.itr()
    print(myArr.length())
    myArr.delete_last()
    myArr.itr()
    print(myArr.length())
    myArr.delete_first()
    myArr.itr()
    print(myArr.length())
    myArr.delete_at(1)
    myArr.itr()
    print(myArr.length())
