def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = arr[i]

        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    my_list = [5,4,3,3,2,1,1]
    print("Original List:")
    print(my_list)

    selection_sort(my_list)

    print("Sorted List:")
    print(my_list)