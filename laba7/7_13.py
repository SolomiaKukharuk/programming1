#https://www.eolymp.com/uk/submissions/15098121
def check_unique(num):
    num = str(num)
    return len(num) == len(set(num))

def rangedif(k,n):
    lst = []
    for i in range(k,n):
        if check_unique(i) is True:
            lst.append(i)
    return lst

a, b = [int(d) for d in input().split()]
print(*rangedif(a,b))