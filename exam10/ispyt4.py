from moduler import isortonormo
with open("file.txt", "r") as f:
    matrix1 = []
    for line in f:
        lst = ''.join(line)
        matrix1.append(lst)

print(isortonormo(matrix1))
