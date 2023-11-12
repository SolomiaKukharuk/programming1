#https://www.eolymp.com/uk/submissions/14848886
n = int(input())
lst1 = [int(el) for el in input().split()]
n1 = int(input())
lst2 = [int(el) for el in input().split()]
lst3 =[]
for el in lst1:
    if el not in lst2:
        lst3.append(el)
print(len(lst3))
print(*lst3)