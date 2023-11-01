#https://www.eolymp.com/uk/submissions/14965501
n = input()
n = n.replace(' ', '')
if n == n[::-1]:
	print("YES")
else:
	print("NO")