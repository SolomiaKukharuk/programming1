#https://www.eolymp.com/uk/submissions/14848794
n = int(input())
lst = [int(el) for el in input().split()]
if n == 1:
    print(lst[0])
else:
    minl = min(lst)
    for el in lst:
        if el < minl:
            minl = el
    print(minl)