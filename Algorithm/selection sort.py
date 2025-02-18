def selection_sort(arr):
    # প্রতিটি উপাদানের জন্য
    for i in range(len(arr)):
        # ধরে নিই যে i তম উপাদানটাই সবচেয়ে ছোট
        min_idx = i
        # i এর পরবর্তী সব উপাদানের জন্য
        for j in range(i + 1, len(arr)):
            # যদি j তম উপাদানটি min_idx তে থাকা উপাদানের চেয়ে ছোট হয়
            if arr[j] < arr[min_idx]:
                # তাহলে min_idx আপডেট করে দেই
                min_idx = j
        # সবচেয়ে ছোট উপাদানটিকে বর্তমান i তম স্থানে বসাই
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# উদাহরণ:
numbers = [5, 3, 8, 6, 7, 2]
selection_sort(numbers)
print("Sorted array:", numbers)
