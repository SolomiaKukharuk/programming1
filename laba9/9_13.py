#https://www.eolymp.com/uk/submissions/15409038
n = int(input())
dick = {}
new_dick = {}
for i in range(n):
    a = input()
    a = a.replace(',', '').replace('-', '').split()
    dick[a[0]] = []
    for j in range(1, len(a)):
        dick[a[0]].append(a[j])

for key, value in dick.items():
    for el in value:
        if el not in new_dick:
            new_dick[el] = []
            new_dick[el].append(key)
        else:
            new_dick[el].append(key)

sorted_dick = sorted(new_dick)
print(len(new_dick))
for key in sorted_dick:
    print(key, '-', end=' ')
    print(*new_dick[key], sep=', ')