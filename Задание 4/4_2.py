import numpy as np

A = np.array([[1, -1, 1], [2, 1, 1], [1, 1, 1]])
B = np.array([3, 11, 8])
X = np.linalg.solve(A, B)

print("Решение системы линейных уравнений 1:")
print(X)

A = np.array([[1, 2, -1], [2, -3, 1], [4, 1, -1]])
B = np.array([7, 3, 16])

try:
    X = np.linalg.solve(A, B)
    print("Решение системы линейных уравнений 2:")
    print(X)
except:
    print("Нет решения")
