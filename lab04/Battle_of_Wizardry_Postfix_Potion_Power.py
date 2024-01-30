count = int(input())

for i in range(count):
    expression = list(map(str,input().split()))
    stack = []
    for j in expression:  
        if j in ["+", "-", "*", "/"]:
            top_element = stack.pop()
            second_top_element = stack.pop()
            if j == "+":
                stack.append(second_top_element + top_element)
            elif j == "-":
                stack.append(second_top_element - top_element)
            elif j == "*":
                stack.append(second_top_element * top_element)
            elif j == "/":
                stack.append(second_top_element / top_element)    
        else:
            stack.append(float(j))
    print(int(stack.pop()))