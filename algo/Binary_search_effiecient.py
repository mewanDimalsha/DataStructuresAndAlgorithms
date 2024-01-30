def binary_search(array, target, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if array[mid] < target:
        return binary_search(array, target, mid + 1, high)
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return mid

print(binary_search([1,2,3,4,5,6,7,8,9,10], 8))