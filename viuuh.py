x1 , y1 = [int(d) for d in input().split()]
x2 , y2 = [int(d) for d in input().split()]
x3 , y3 = [int(d) for d in input().split()]
x4 , y4 = [int(d) for d in input().split()]
if x1 == x2 and y2 == y3 and x3 == x4 and y1 == y4:	
	print("yes")
	s = abs(x2-x1) * abs(y1-y4)


if abs(x2-x1) == abs(x3 - x4)  and abs(y2 - y3) == abs(y4 - y1) :
	print(s)
else: 
	pass 

	print("no")
