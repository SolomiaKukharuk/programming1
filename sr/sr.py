import moduleint
import multi 
import tasks

m = int(input("Enter the numder of Row"))
n = int(input("Enter Number of Coloumn"))
a = inmatrix(m,n)

rank = rank_of_matrix(a)
determinant = determinant_of_matrix(a)
upper_triangular_matrix = make_upper_triangular(a)
    



x = input("Chose the variant:")
if x == a:
	printmatrix("Ось нова матриця:"upper_triangular_matrix)
elif x == b:
	print("Ранг матриці:", rank)
elif x == c:
	print("Визначник матриці:", determinant)

