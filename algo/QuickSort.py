def quick_sort(arr, start, end):
    if start >= end:
        return  # If the start index is greater than or equal to the end index, the array is already sorted

    pivot = arr[end]  # Choose the last element as the pivot
    left = start  # Initialize the left pointer
    right = end - 1  # Initialize the right pointer

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1  # Move the left pointer to the right until a value greater than the pivot is found
        while left <= right and arr[right] >= pivot:
            right -= 1  # Move the right pointer to the left until a value smaller than the pivot is found

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]  # Swap the values at the left and right pointers

    arr[end], arr[left] = arr[left], arr[end]  # Swap the pivot with the value at the left pointer

    quick_sort(arr, start, left - 1)  # Recursively sort the left subarray
    quick_sort(arr, left + 1, end)  # Recursively sort the right subarray

    return arr  # Return the sorted array

print(quick_sort([3, 2, 1, 5, 6, 4], 0, 5))
large_array = [9, 5, 2, 7, 1, 8, 3, 6, 4, 10, 15, 12, 11, 14, 13, 18, 16, 19, 17, 20, 25, 22, 21, 24, 23, 30, 27, 26, 29, 28, 35, 32, 31, 34, 33, 40, 37, 36, 39, 38, 45, 42, 41, 44, 43, 50, 47, 46, 49, 48, 55, 52, 51, 54, 53, 60, 57, 56, 59, 58, 65, 62, 61, 64, 63, 70, 67, 66, 69, 68, 75, 72, 71, 74, 73, 80, 77, 76, 79, 78, 85, 82, 81, 84, 83, 90, 87, 86, 89, 88, 95, 92, 91, 94, 93, 100]
print(quick_sort(large_array, 0, len(large_array) - 1))

