#https://www.eolymp.com/uk/submissions/15096228
from math import sqrt
def lucky(a):
    lst = []
    while len(lst) <= a:
        for i in range(11, 100):
            for el in range(2, int(sqrt(i))):
                if i % el == 0:
                    pass
                elif i % 5 == 0:
                    pass
                elif i % 3 == 0:
                    pass
                elif i % 2 == 0:
                    pass
                else:
                    lst.append(i)
    for el in lst:
        el = str(el)
        if el == el[:: -1]:
            el = int(el)
            lst.remove(el)
        else:
            el = int(el)
    return lst[a - 1]

k = int(input())
if k > 10**6:
    print("-1")
else:
    print(lucky(k))