x = int(input())
a = x // 100
b = x % 10
if a > b:
    print(a)
else:
    if a < b:
        print(b)
    else:
        print("=")
