def binary_search(array,target):
    low=0
    high=len(array)-1
    while low<=high:
        mid=low+(high-low)//2
        value = array[mid]
        if value<target:
            low=mid+1
        elif value>target:
            high=mid-1
        else:
            return mid
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10],8))