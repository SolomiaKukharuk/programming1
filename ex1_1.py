from math import sqrt, pi


class Triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def perimeter(self):
		if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
			return (self.a + self.b + self.c)
		else:
			return 0

	def area(self) -> object:
		pivp = self.perimeter() / 2
		return sqrt(pivp * (pivp - self.a) * (pivp - self.b) * (pivp - self.c))


class Rectangle:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def perimeter(self):
		return (self.a + self.b)

	def area(self):
		return self.a * self.b


class Trapeze:
	def __init__(self, a, b, c, d):

		self.a = a
		self.b = b

		self.c = c
		self.d = d

	def perimeter(self):
		return (self.a + self.b + self.c + self.d)

	def area(self):
		pivp = self.perimeter() / 2
		srt = pivp * (pivp - self.a) * (pivp - self.b) * (pivp - self.a - self.c) * (pivp - self.a - self.c)

		if srt <= 0:
			return 0

		if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
			return 0
		if self.a - self.b == 0:
			return 0

		return ((self.a + self.b) / abs(self.a - self.b)) * sqrt(srt)


class Parallelogram:

	def __init__(self, a, b, h):
		self.a = a
		self.b = b
		self.h = h

	def perimeter(self):
		return (2 * self.a + 2 * self.b)

	def area(self):
		return self.b * self.h


class Circle:

	def __init__(self, r):
		self.r = r

	def perimeter(self):
		return 2 * pi * self.r

	def area(self):
		return pi * (self.r ** 2)


with open('input01.txt', 'r') as f1, open('input02.txt', 'r') as f2, open('input03.txt', 'r') as f3:
	max_area_t = 0  # triangle
	max_perimeter_t = 0

	max_area_r = 0  # rectangle
	max_perimeter_r = 0

	max_area_c = 0  # circle
	max_perimeter_c = 0

	max_area_tr = 0  # trapezia
	max_perimeter_tr = 0

	max_area_p = 0  # paralelogram
	max_perimeter_p = 0

	with open('input01.txt', 'r') as f1, open('input02.txt', 'r') as f2, open('input03.txt', 'r') as f3:
		lines = f1.readlines()
		lines2 = f2.readlines()
		lines3 = f3.readlines()
		lines.extend(lines2)
		lines.extend(lines3)

		for line in lines:
			data = line.strip().split()
			figure_name = data[0]
			parameters = [float(x) for x in data[1:]]

			if figure_name == 'Rectangle':
				a, b = parameters
				rectangle = Rectangle(a, b)
				area = rectangle.area()
				perimeter = rectangle.perimeter()
				if area > max_area_r:
					max_area_r = area
				if perimeter > max_perimeter_r:
					max_perimeter_r = perimeter

			elif figure_name == 'Circle':
				r = parameters[0]
				circle = Circle(r)
				area = circle.area()
				perimeter = circle.perimeter()
				if area > max_area_c:
					max_area_c = area
				if perimeter > max_perimeter_c:
					max_perimeter_c = perimeter

			elif figure_name == 'Parallelogram':
				a, b, h = parameters
				parallelogram = Parallelogram(a, b, h)
				area = parallelogram.area()
				perimeter = parallelogram.perimeter()
				if area > max_area_p:
					max_area_p = area
				if perimeter > max_perimeter_p:
					max_perimeter_p = perimeter

			elif figure_name == 'Triangle':
				a, b, c = parameters
				triangle = Triangle(a, b, c)
				area = triangle.area()
				perimeter = triangle.perimeter()
				if area > max_area_t:
					max_area_t = area
				if perimeter > max_perimeter_t:
					max_perimeter_t = perimeter

			elif figure_name == 'Trapeze':
				a, b, c, d = parameters
				trapeze = Trapeze(a, b, c, d)
				area = trapeze.area()
				perimeter = trapeze.perimeter()
				if area > max_area_tr:
					max_area_tr = area
				if perimeter > max_perimeter_tr:
					max_perimeter_tr = perimeter

	dict = { }
	dict['Triangle'] = max_perimeter_t, max_area_t
	dict['Paralllogram'] = max_perimeter_p, max_area_p
	dict['Trapeze'] = max_perimeter_tr, max_area_tr
	dict['Circle'] = max_perimeter_c, max_area_c
	dict['Rectangle'] = max_perimeter_r, max_area_r
	print('The biggest area and perimeter in:', max(dict))
