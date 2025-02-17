def findSmallest (arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in (range(1, len(arr))):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selectionSort (arr):
    newArr = []
    copiedArr = list(arr)
    print("Initial array:")
    print(copiedArr)
    for i in range(len(copiedArr)):
        print(f"Interaction #{i}")
        smallestIndex = findSmallest(copiedArr)
        print(f"Smallest Index: {smallestIndex}")
        print(f"Smallest Number: {copiedArr[smallestIndex]}")
        newArr.append(copiedArr.pop(smallestIndex))
        print(f"Array after pop:")
        print(copiedArr)
    return newArr


print(selectionSort([3, 4, 7, 1, 2, 9, 5]))
