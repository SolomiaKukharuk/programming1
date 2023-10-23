n = int(input())
lst = [float(el) for el in input().split()]
summ = 0
count = 0
for el in lst:
	if el > 0:
		summ += el
		count += 1
if summ != 0:
	  print(format(summ/count, '.2f'))
else:
	print("Not Found")