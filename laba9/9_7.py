#https://www.eolymp.com/uk/submissions/15408303
n = int(input())
lett = input()
if n % 2 == 0:
    print('Ok')
    exit()
for i in lett:
    if lett.count(i) % 2:
        print(i)
        break