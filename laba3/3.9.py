n = int(input())
count = 0
i = 0
while count < n:
	i += 1
	if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
		print(i, end = " ")
		count += 1 