# https://snakify.org/en/lessons/two_dimensional_lists_arrays/
# Time complexity: O(n^2)

def mat_modifier(size):
    n = size
    matrix = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i > j:
                matrix[i][j] = 2
            elif i < j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1

    for i in matrix:
        print(' '.join([str(j) for j in i]))


mat_modifier(4)
