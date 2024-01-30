def linear_search(Array,value):
    for i in range(len(Array)):
        if Array[i] == value:
            return i
    return -1
print(linear_search([10,9,8,7,6,5,4,3,2,1], 9))