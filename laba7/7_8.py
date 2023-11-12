#https://www.eolymp.com/uk/submissions/15096107
def nskd(c,d):
    lst = []
    for i in range(1,d + 1):
        if i % c == 0:
            lst.append(i)
            if d % i != 0:
                lst.remove(i)

    return len(lst) - 2

a, b = [int(d) for d in input().split()]
print(nskd(a,b))
