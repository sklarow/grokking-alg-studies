def sum(arr):
    if arr == []: # base case
        return 0
    
    return arr[0] + sum(arr[1:])  # recursive case


print(sum([1,2,4,7,2]))
