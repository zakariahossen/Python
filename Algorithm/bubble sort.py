def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - 1):
            if list[j] > list[j + 1]:
                # Swap the elements
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

# Example usage
nums = [5, 3, 8, 6, 7, 2]
result = bubble_sort(nums)
print(result)
