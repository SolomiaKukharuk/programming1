x1, x2, x3 = [int(d) for d in input().split()]
if x1 <= 100 and x2 <= 100 and x3 <= 100:
	if x1 == x2 and x1 == x3 and x2 == x3:
		print ("1")
	elif (x1 == x2)^(x1 == x3)^(x2 == x3):
		print ("2")
	elif x1 != x2 and x1 != x3 and x2 != x3:
		print ("3")
	else:
		pass
else:
	pass