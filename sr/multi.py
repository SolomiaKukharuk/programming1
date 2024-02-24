def matrix_multiplication(A, B):

	rows_A = len(A)

	cols_A = len(A[0])

	rows_B = len(B)

	cols_B = len(B[0])

	result = [[sum(a * b for a, b in zip(rows_a, cols_b)) for cols_b in zip(*B)] for rows_a in A]

	return result


def ryadok(a,b):
	b = input("Choose the row")
	return a[b]



def multyscal(a,b):
	colso_A = a[0]
	for el in colso_A:
		el * col 
	return colso_A



def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]
    return matrix 



def swap_columns(matrix1, i1, j1):
    for row in matrix1:
        row[i1], row[j1] = row[j1], row[i1]
    return matrix1




def subtract_vector_from_rows(matrix2, vector):
    if len(matrix2[0]) != len(vector):
        print("Неможливо відняти вектор. Розмірності не співпадають.")
        return

    for row in matrix2:
        for i in range(len(row)):
            row[i] -= vector[i]

    return matrix2