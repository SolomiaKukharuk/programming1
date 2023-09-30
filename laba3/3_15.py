k = int(input())
n = int(input())
digi = 0
i = 1
while n > 0:
    bit = n % 10
    digidu = bit * (k ** (i - 1))
    i += 1
    digi += digidu
    n //= 10
print(digi)