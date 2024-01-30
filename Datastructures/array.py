from array import *

num_array = array('i', [1, 2, 3, 4, 5])

num_array.append(6)
print(num_array)

num_array.insert(4, 45)
print(num_array)

for i in num_array:
    print(i)
    
print(num_array.index(4))

num_array.pop()
print(num_array)

num_array.remove(45)
print(num_array)