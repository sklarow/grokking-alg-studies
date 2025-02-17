def count(arr):
    if arr == []: # base case
        return 0
    
    return 1 + count(arr[1:]) # recursive case


print(count([1,2,4,7,2]))
