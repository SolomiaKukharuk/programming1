from cmath import pi
s1, r1 = [float(d) for d in input().split()]
s = r1 ** 2 * pi
s2 = s - s1
r2 = (s2 / pi) ** 0.5
print("%0.2f" % r2)
