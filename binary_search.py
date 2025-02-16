def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == item:
            return mid
        elif guess >  item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None


# Test cases
print(binary_search([1, 2, 3], 3))  # Should return 2
print(binary_search([1, 2, 3, 4, 5, 6], 4))  # Should return 3
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))  # Should return 3
print(binary_search([1, 2, 3], 5))  # Should return None
