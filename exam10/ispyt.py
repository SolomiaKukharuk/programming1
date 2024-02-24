lst = []
for i in range(10_000, 100_000):
    i = str(i)
    if i == i[::-1]:
        i = int(i)
        f = i ** 2
        f = str(f)
        if f == f[::-1]:
            lst.append(i)
print(sum(lst))
