def scalar(lst1, lst2):
    if len(lst1) == len(lst2):
        summ = 0
        for el in lst1:
            for i in lst2:
                dob = lst1[el] * lst2[i]
                summ += dob
        return summ
    else:
        return ImportError


def rows(matrix):
    while True:
        for row in matrix:
            for i in range(len(matrix)):
                rowscalar = scalar(row, row[i])
                if rowscalar == 0:
                    return True
                else:
                    return False


def cols(matrix):
    n = len(matrix)
    m = len(matrix[0])
    while True:
        for j in range(m):
            for i in range(n):
                col = scalar(matrix[i][j], matrix[i][j])
                if col == 1:
                    return True
                else:
                    return False


def isortonormo(matrix):
    if len(matrix) == len(matrix[0]):
        if rows(matrix) is True and cols(matrix) is True:
            return "Matrix is ortonormous"
        else:
            return "Matrix is not ortonormous"
    else:
        return ImportError
