def a(line):
	ress = 0
	for el in line:
		if el % 2 == 0
			ress += 1
	return ress


def b(line):
	ress1 = 0
	for el in line:
		if el % 2 != 0
			ress1 += 1
	return ress1


def c(line):
	odd = []
	noodd = []
	for el in line:
		if el % 2 == 0:
			noodd.append(el)
		else:
			odd.append(el)
	maxi = max(noodd)
	mini = min(odd)
	e = maxi - mini
	return e


def d(line):
	 mas_len = []
    length = 1
    for i in range(len(line) - 1):
        if i + 1 == len(line) - 1 and line[i] < line[i + 1]:
            length += 1
            mas_len.append(length)
            break
        if line[i] < line[i + 1]:
            length += 1
        elif line[i] > line[i + 1]:
            mas_len.append(length)
            length = 1
    if not mas_len:
        return "error"
    return max(mas_len)


with open('file.txt') as file:
	 mas_of_lines = []
    for line in file:
        line = [int(el) for el in line.split()]
        mas_of_lines += line
    print(f"a): {ex_a(mas_of_lines)}")
    print(f"b): {ex_b(mas_of_lines)}")
    print(f"c): {ex_c(mas_of_lines)}")
    print(f"d): {ex_d(mas_of_lines)}")