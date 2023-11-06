def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

if __name__ == '__main__':
    my_list = [7,6,5,4,3,2,1]
    print("Original List:")
    print(my_list)

    insertion_sort(my_list)

    print("Sorted List:")
    print(my_list)