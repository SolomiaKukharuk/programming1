#https://www.eolymp.com/uk/submissions/15408566
num = int(input())
for i in range(num):
    mn = {}
    lst_max = []
    a = int(input())
    for j in range(a):
        n = int(input())
        if n not in mn:
            mn[n] = [1]
        else:
            mn[n][0] += 1
    for key in mn:
        if mn[key] == max(mn.values()) and key not in lst_max:
            lst_max.append(key)
    if  len(lst_max) == 1:
        print(max(lst_max))
    elif len(lst_max) >= 2:
        print(min(lst_max))