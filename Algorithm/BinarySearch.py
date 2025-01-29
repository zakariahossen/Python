def binary_search(list, find_value):      # Define the binary search function
    low = 0                              # Initialize the low index
    high = len(list) - 1                 # Initialize the high index

    while low <= high:                   # Loop until low index is less than or equal to high index
        mid = (low + high) // 2          # Calculate the middle index
        if list[mid] < find_value:       # If the middle element is less than the target value
            low = mid + 1                # Move the low index to mid + 1
        elif list[mid] > find_value:     # If the middle element is greater than the target value
            high = mid - 1               # Move the high index to mid - 1
        else:                            # If the middle element is equal to the target value
            return mid                   # Return the middle index
    print("element not found")           # Print message if element is not found

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]       # List of numbers to search
index = binary_search(nums, 90)          # Call the binary search function with a target value
print(index)                             # Print the result index
