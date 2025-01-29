def LinearSearch(list,target):
    for elements in list:
        if elements == target:
            print('I have got ',target,' and its index is ',list.index(target))
        else:
            print("Not found!")

arr = [34,65,89,23,534,56,78,35]
LinearSearch(arr,23)
