import modeuleint
import multi 


m = int(input("Enter the numder of Row"))
n = int(input("Enter Number of Coloumn"))
a = inmatrix(m,n)

def rank_of_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    rank = cols
    for row in range(min(rows, cols)):
        if matrix[row][row] != 0:
            for col in range(rows):
                if col != row:
                    multiplier = matrix[col][row] / matrix[row][row]
                    for i in range(rank):
                        matrix[col][i] -=  multiplier * matrix[row][i] #у задачі було лише про множення вектора на скаляр

        else:
            reduce_rank = True
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    matrix[row], matrix[i] = matrix[i], matrix[row]
                    reduce_rank = False
                    break

            if reduce_rank:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][rank]

    return rank

rank = rank_of_matrix(a)


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


determinant = determinant_of_matrix(example_matrix)

def make_upper_triangular(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        if matrix[i][i] == 0:
            for j in range(i + 1, rows):
                if matrix[j][i] != 0:
                    swaprows(i,j)
                    break

        if matrix[i][i] == 0:
            continue

        for j in range(i + 1, rows):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, cols):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


upper_triangular_matrix = make_upper_triangular(example_matrix)
    



x = input("Chose the variant:")
if x == a:
	printmatrix("Ось нова матриця:"upper_triangular_matrix)
elif x == b:
	print("Ранг матриці:", rank)
elif x == c:
	print("Визначник матриці:", determinant)

