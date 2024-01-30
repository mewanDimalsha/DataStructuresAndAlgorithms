def BubbleSort(Array):
    n = len(Array)
    while n > 1:
        is_sorted = True  # Flag to check if the array is already sorted
        for i in range(n - 1):
            if Array[i] > Array[i + 1]:
                Array[i], Array[i + 1] = Array[i + 1], Array[i]
                is_sorted = False  # Set the flag to False if a swap is made
        if is_sorted:
            break  # Terminate the sorting process if the array is already sorted
        n -= 1
    
    return Array
print(BubbleSort([10,9,8,7,6,5,4,3,2,1]))