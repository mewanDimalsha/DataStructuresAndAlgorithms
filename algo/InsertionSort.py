def Insertion_sort(Array):
    for i in range(1, len(Array)):
        j = i
        while j > 0 and Array[j] < Array[j-1]:
            Array[j], Array[j-1] = Array[j-1], Array[j]
            j -= 1
    return Array

print(Insertion_sort([10,9,8,7,6,5,4,3,2,1]))