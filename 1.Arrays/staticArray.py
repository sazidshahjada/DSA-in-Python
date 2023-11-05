
class StaticArr:
    def __init__(self) -> None:
        self.Arr = []
        self.Size = 0

    def __len__(self):
        return self.Size
    
    def build(self, X):
        self.Arr = [i for i in X]
        self.Size = len(X)

    def itr(self):
        for item in self.Arr:
            print(item, end=' ')
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
    
if __name__ == '__main__':
    myArr = StaticArr()

    myArr.build([1,2,3,4,5])
    print(len(myArr))
    myArr.itr()
    print(myArr.get_at(3))
    myArr.set_at(0, 10)
    myArr.itr()
    print(myArr.get_at(7))
    myArr.set_at(10, 10)
    myArr.itr()