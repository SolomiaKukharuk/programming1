#https://www.eolymp.com/uk/submissions/14965659
s = input()
c = 0
c1 = 0
c2 = 0
c4 = 0
c3 = 0
c5 = 0
for i in s:
    if i.islower():
        c1 = 1
    elif i.isupper():
        c2 = 1
    elif i.isdigit():
        c3 = 1
    elif not i.islower() and not i.isupper() and not i.isdigit():
        c4 = 1
if len(s) >= 8:
    c5 = 1
c = c1 + c2 + c3 + c4 + c5
print(c)