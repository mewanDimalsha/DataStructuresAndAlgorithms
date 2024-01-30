def Fibonacci(n):
    first = 1
    second = 1
    temp = 0
    if n == 1 or n == 2:
        return 1
    else:
        for x in range(2, n):
            temp = first + second
            first = second
            second = temp

    return temp

count = int(input())
for _ in range(count):
    weight = int(input())
    print(Fibonacci(Fibonacci(weight)))