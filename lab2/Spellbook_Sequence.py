def longest_common_subsequence(no_of_rows, no_of_columns, first_num_array, second_num_array):
    twoD_array = [[0] * (no_of_columns+1) for _ in range(no_of_rows+1)]

    for i in range(no_of_columns+1):
        twoD_array[0][i] = 0

    for i in range(no_of_rows+1):
        twoD_array[i][0] = 0

    for i in range(1, no_of_rows+1):
        for j in range(1, no_of_columns+1):
            if first_num_array[j-1] == second_num_array[i-1]:
                twoD_array[i][j] = 1 + twoD_array[i-1][j-1]
            else:
                twoD_array[i][j] = max(twoD_array[i-1][j], twoD_array[i][j-1])

    i, j = no_of_rows, no_of_columns
    last_index = twoD_array[i][j]
    output_array = [0] * last_index  

    while i > 0 and j > 0:
        if first_num_array[j-1] == second_num_array[i-1]:
            output_array[last_index-1] = first_num_array[j-1]
            i -= 1
            j -= 1
            last_index -= 1
        elif twoD_array[i-1][j] > twoD_array[i][j-1]:
            i -= 1
        else:
            j -= 1

    print(*output_array)

no_of_columns, no_of_rows = map(int, input().split())
first_num_array = list(map(int, input().split()))
second_num_array = list(map(int, input().split()))

longest_common_subsequence(no_of_rows, no_of_columns, first_num_array, second_num_array)

