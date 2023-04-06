import copy

def kramer_method(matrix, free_terms):
    """
    Вычисление решения системы линейных уравнений методом Крамера.

    :param matrix: матрица коэффициентов системы линейных уравнений
    :param free_terms: вектор свободных членов системы линейных уравнений
    :return: вектор решения системы линейных уравнений
    """

    # Размерность матрицы
    n = len(matrix)

    # Определитель матрицы
    determinant = det(matrix)

    # Решение системы линейных уравнений
    solution = []
    try:
        for i in range(n):
            # Копия матрицы коэффициентов
            matrix_copy = copy.deepcopy(matrix)

            # Замена i-го столбца на вектор свободных членов
            for j in range(n):
                matrix_copy[j][i] = free_terms[j]

            # Вычисление определителя новой матрицы
            determinant_i = det(matrix_copy)

            # Вычисление i-й неизвестной
            solution_i = determinant_i / determinant

            solution.append(solution_i)
        print(solution)
    except:
        print("Решения нет")

    return solution


def det(matrix):
    """
    Вычисление определителя матрицы.

    :param matrix: матрица
    :return: определитель матрицы
    """

    # Размерность матрицы
    n = len(matrix)

    # Базовый случай - матрица 1x1
    if n == 1:
        return matrix[0][0]

    # Базовый случай - матрица 2x2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Рекурсивное вычисление определителя матрицы
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
