import copy

def kramer_method(matrix, free_terms):

    n = len(matrix)
    determinant = det(matrix)
    solution = []
    try:
        for i in range(n):
            matrix_copy = copy.deepcopy(matrix)
            for j in range(n):
                matrix_copy[j][i] = free_terms[j]

            determinant_i = det(matrix_copy)
            solution_i = determinant_i / determinant
            solution.append(solution_i)
        print(solution)
    except:
        print("Решения нет")
    return solution

def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    sign = 1

    for i in range(n):
        matrix_copy = copy.deepcopy(matrix)
        matrix_copy.pop(0)

        for j in range(n - 1):
            matrix_copy[j].pop(i)

        determinant += sign * matrix[0][i] * det(matrix_copy)
        sign = -sign
    return determinant

matrix = [[1, -1, 1], [2, 1, 1], [1, 1, 2]]
free_terms = [3, 11, 8]

kramer_method(matrix, free_terms)

matrix = [[1, 2, -1], [2, -3, 1], [4, 1, -1]]
free_terms = [7, 3, 16]

kramer_method(matrix, free_terms)
