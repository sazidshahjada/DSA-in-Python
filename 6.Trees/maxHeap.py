class PriorityQueue:
    def __init__(self) -> None:
        self.heap_array = []

    def heapify_up(self):
        index = len(self.heap_array) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap_array[index] > self.heap_array[parent_index]:
                self.heap_array[index], self.heap_array[parent_index] = (
                    self.heap_array[parent_index],
                    self.heap_array[index],
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (
            left_child_index < len(self.heap_array)
            and self.heap_array[left_child_index] > self.heap_array[largest]
        ):
            largest = left_child_index

        if (
            right_child_index < len(self.heap_array)
            and self.heap_array[right_child_index] > self.heap_array[largest]
        ):
            largest = right_child_index

        if largest != index:
            self.heap_array[index], self.heap_array[largest] = (
                self.heap_array[largest],
                self.heap_array[index],
            )
            self.heapify_down(largest)

    def insert_element(self, element):
        self.heap_array.append(element)
        self.heapify_up()
        print("Inserted element:", i)

    def delete_max_element(self):
        if not self.heap_array:
            return None

        max_element = self.heap_array[0]
        last_element = self.heap_array.pop()
        if self.heap_array:
            self.heap_array[0] = last_element
            self.heapify_down(0)

        print("Deleted max element:", max_element)

    def show_heap_array(self):
        print("The heap array: ")
        for i in self.heap_array:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    pq = PriorityQueue()

    elements = [3, 5, 7, 9, 10, 20, 2, 30, 15, 39, 50, 12, 6]

    for i in elements:
        pq.insert_element(i)
    pq.show_heap_array()

    max_element = pq.delete_max_element()
    pq.show_heap_array()

    max_element = pq.delete_max_element()
    pq.show_heap_array()

    max_element = pq.delete_max_element()
    pq.show_heap_array()