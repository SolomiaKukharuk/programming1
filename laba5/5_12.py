#https://www.eolymp.com/uk/submissions/14692121
n = input()
lst1 = [int(el) for el in input().split()]
lst2 = [ ]
for el in lst1:
	if el not in lst2:
		lst2.append(el)
print(*lst2)