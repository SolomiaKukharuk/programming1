#https://www.eolymp.com/uk/submissions/15027510
#код працює чудово з різними значеннями,а еолімп вимахується
def nsk(a):
	dilnyky = []
	res = a
	for i in range(1,a):
		if a % i == 0:
			dilnyky.append(i)
	if dilnyky == [1]:
		for i in range(1, a - 1):
			if (a - 1) % i == 0:
				dilnyky.append(i)

	for d in range(1,a):
		res *= d
	for el in dilnyky:
		e = res // el
	return e


n = int(input())
y = nsk(n)
print(y)
