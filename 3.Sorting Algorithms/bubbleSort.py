def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        
        if not swap:
            break

if __name__ == '__main__':
    my_list = [1,2,3,4]
    print('Original List:')
    print(my_list)
    bubble_sort(my_list)
    print('Sorted List:')
    print(my_list)