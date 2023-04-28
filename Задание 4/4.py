import numpy as np

A1 = np.array([[1, -1, 1], [2, 1, 1], [1, 1, 1]])
B1 = np.array([3, 11, 8])

print("Матрица A")
print(A1,"\n")
print("Матрица B")
print(B1,"\n")

try:
    X1 = np.linalg.solve(A1, B1)
    print("Решение системы линейных уравнений 1:")
    print(X1)
except:
    print("Нет решения")

A2 = np.array([[1, 2, -1], [2, -3, 1], [4, 1, -1]])
B2 = np.array([7, 3, 16])

print("Матрица A")
print(A2,"\n")
print("Матрица B")
print(B2,"\n")

try:
    X2 = np.linalg.solve(A2, B2)
    print("Решение системы линейных уравнений 2:")
    print(X2)
except:
    print("Нет решения")
