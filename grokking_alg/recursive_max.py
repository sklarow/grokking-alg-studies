def max (arr):
    if len(arr) < 2: # corner case
        return None
    if len(arr) == 2: # base case
        return arr[0] if arr[0] > arr[1] else arr[1]
    
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max # recursive case

print(max([1,2,4,7,30,2,10]))
print(max([]))
print(max([1]))
print(max([2,4]))
print(max([4,2]))
