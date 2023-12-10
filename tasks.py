import multi
def make_upper_triangular(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        if matrix[i][i] == 0:
            for j in range(i + 1, rows):
                if matrix[j][i] != 0:
                    multi.swap_rows(matrix, i, j)
                    break

        if matrix[i][i] == 0:
            continue

        for j in range(i + 1, rows):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, cols):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


def rank_of_matrix(matrix):
    x = make_upper_triangular(matrix)
    rank = 0
    if matrix[0][0] != 0:
        rank += 1

    return rank




def determinant_of_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise ValueError("Матриця не є квадратною")

    if rows == 1 and cols == 1:
        return matrix[0][0]

    if rows == 2 and cols == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(cols):
        minor = [[matrix[i][j] for j in range(cols) if j != col] for i in range(1, rows)]
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant_of_matrix(minor)

    return det



