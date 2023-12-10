#матриця є симетричною якщо дорівнює транспонованій
import moduleint
m = int(input("Enter the numder of Row"))
n = int(input("Enter Number of Coloumn"))
a = inmatrix(m,n)
def is_qudratic(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return False 


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] == matrix[j][i]
    return matrix1


def isSymmetric(mat, N):
    tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True
 
if (isSymmetric(a, 3)):
    print ("This matrix is symmetric")
else:
    print ("This matrix is not symmetric")
