a, b, c = [int(d) for d in input().split()] 
n = b**2 - 4*a*c
y = 0 - b
if n > 0 :
	x1 = (y + n**0.5) / (2*a)
	x2 = (y - n**0.5) / (2*a)
	if x1 > x2:
		print("Two roots:", round(x2), round(x1))
	else:
		print("Two roots:", round(x1), round(x2))
if n == 0:
	x = y / (2*a)
	print("One root:", round(x)) 
else:
	pass 
if n < 0:
	print ("No roots")
else:
	pass 