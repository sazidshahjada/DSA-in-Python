def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    my_list = [1, 5, 9, 5, 4, 2]

    print("Original List:")
    print(my_list)

    my_list = quick_sort(my_list)

    print("Sorted List:")
    print(my_list)