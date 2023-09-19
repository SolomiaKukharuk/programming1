x = int(input())
a = x % 10
c = x // 100
if  a > c:
	print (a)
else: 
	if c > a:
		print(c)
	else:
		print("=") 