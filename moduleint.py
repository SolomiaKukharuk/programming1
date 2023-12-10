
def inmatrix(m, n):
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            j = int(input("Enter Number in pocket[" + str(i) + "][" + str(j) + "]"))
            b.append(j)
        a.append(b)
    return a


def printmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end="  ")
