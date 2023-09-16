x = abs(int(input()))
a = x % 10
b = (x % 100) // 10
c = x // 100
if a > b and a > c:
	print (a)
else:
	pass 
if b > a and b > c:
	print(b)
else:
	pass 
if c > b and c > a:
	print(c)
else:
	pass 