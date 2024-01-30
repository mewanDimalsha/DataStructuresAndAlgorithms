def merge_sort(num_array):
    if len(num_array) <= 1:
        return num_array

    mid = len(num_array) // 2
    left_half = merge_sort(num_array[:mid])
    right_half = merge_sort(num_array[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

count = int(input())
for i in range(count):
    num_array = list(map(int,input().split()))
    sorted_array = merge_sort(num_array)
    print(' '.join(map(str, sorted_array)))
    
