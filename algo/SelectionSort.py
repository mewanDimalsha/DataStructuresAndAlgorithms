def Selection_sort(Array):
    for i in range(len(Array)):
        min_index = i  # Initialize min_index to i
        for j in range(i+1, len(Array)):
            if Array[j] < Array[min_index]:
                min_index = j
        if min_index != i:
            Array[i], Array[min_index] = Array[min_index], Array[i]
    return Array

print(Selection_sort([10,9,8,7,6,5,4,3,2,1]))
