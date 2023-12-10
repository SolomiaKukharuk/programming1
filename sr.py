import moduleint
import multi
import tasks

m = int(input("Enter the numder of Row"))
n = int(input("Enter Number of Coloumn"))
a = moduleint.inmatrix(m,n)

rank = tasks.rank_of_matrix(a)
determinant = tasks.determinant_of_matrix(a)
upper_triangular_matrix = tasks.make_upper_triangular(a)
    



x = input("Chose the variant:")
if x == 'a':
	moduleint.printmatrix(upper_triangular_matrix)
elif x == 'b':
	print("Ранг матриці:", rank)
elif x == 'c':
	print("Визначник матриці:", determinant)

