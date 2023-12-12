a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    P = a + b + c
    S = (P / 2 * (P / a) * (P / b) * (P / c)) ** 0.5
    h1 = (2 * S) / a
    h2 = (2 * S) / b
    h3 = (2 * S) / c
    print("Perimeter:", P, "\n" "Area:", S, "\n" "Heights:", h1, h2, h3)
else:
    print("This triangle cant't be formed!")