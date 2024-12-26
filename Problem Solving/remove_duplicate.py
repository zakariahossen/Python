# it will remove duplicate numbers from the given list
def remove_duplicate(arr):
    # create a new empty list
    unique_list = []
    for num in arr:
        # check that the number is in the new list or not.
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


our_list = [2, 3, 4, 4, 5, 5]
result = remove_duplicate(our_list)
print(result)
