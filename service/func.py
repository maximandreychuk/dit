from typing import List


def check_matrix_dimensions(matrix1: List[List[int]], matrix2: List[List[int]], operation: str):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if operation == "multiply":
        if cols1 != rows2:
            raise ValueError("Столбец 1 должен быть равен столбцу 2")
    elif operation in ["add", "subtract"]:
        if rows1 != rows2 or cols1 != cols2:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
    else:
        raise ValueError("Invalid operation type")


def apply_matrix_operation(matrix1: List[List[int]], matrix2: List[List[int]], operation: str):
    check_matrix_dimensions(matrix1, matrix2, operation)

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0]) if operation == "multiply" else cols1

    result_matrix = [[0.0] * cols2 for _ in range(rows1)]

    if operation == "multiply":
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    elif operation == "add":
        for i in range(rows1):
            for j in range(cols1):
                result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    elif operation == "subtract":
        for i in range(rows1):
            for j in range(cols1):
                result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
    return result_matrix