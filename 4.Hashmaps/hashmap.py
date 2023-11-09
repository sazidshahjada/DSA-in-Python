class Hashmap:
    def __init__(self, A) -> None:
        self.size = len(A)
        self.h_table = [None] * self.size
        self.keys = [x for x in A]

    def h_function(self, key):
        return key % self.size
    
    def h_map(self):
        for key in self.keys:
            idx = self.h_function(key)
            self.h_table[idx] = key

        return self.h_table

if __name__ == '__main__':
    my_list = [9,3,5,2,1]
    
    hmap = Hashmap(my_list)

    print(hmap.h_map())
    