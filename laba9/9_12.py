#https://www.eolymp.com/uk/submissions/15409024
a = input()
b = input()
a1 = set(a)
b1 = set(b)
if a1.issuperset(b1) is True:
	print("Ok")
else:
	print("No")