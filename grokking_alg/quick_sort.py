def quicksort (arr):
    if len(arr) < 2: # base case (arrays with 0 or 1 elements are already sorted)
        return arr
    
    pivot = arr[0] # get the first element as pivot
    print("-----")
    print("Quick Sort call:")
    print(f"Array: {arr}")
    print(f"Pivot: {pivot}")
    
    # initialize empty arrays
    less = []
    greater = []
    
    # compare the array minus the first element (pivot)
    # and make the less and greater than arrays
    for i in arr[1:]:
        if i <= pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
            
    print(f"Less than {pivot} arr: {less}")
    print(f"Greater than {pivot} arr: {greater}")
    
    return quicksort(less) + [pivot] + quicksort(greater)

test_arr = [0, 2, 3, 6, 1, 5, 9, 12, 15, 1]
print(quicksort(test_arr))
