def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# উদাহরণ:
arr = [3, 8, 7, 5, 9, 4]
insertion_sort(arr)
print(arr)
