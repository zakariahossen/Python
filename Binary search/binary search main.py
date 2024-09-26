def binary_search(list,find_value):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] < find_value:
            low = mid + 1
        elif list[mid] > find_value:
            high = mid -1
        else:
            return mid
    print("element not found")

nums = [1,2,3,4,5,6,7,8,9]
index = binary_search(nums, 90)
print(index)