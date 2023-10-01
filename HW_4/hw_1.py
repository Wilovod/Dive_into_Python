# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    n = len(matrix)
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return transposed

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)