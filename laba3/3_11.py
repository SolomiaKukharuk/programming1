n = int(input())
i = 1
summ = 0
dig = 0
while 10 ** (i - 1) <= n:
    digit = (n % 10 ** i) // 10 ** (i - 1)
    i += 1
    if digit % 2 == 0:
        dig += 1
        summ += digit        
if dig == 0:
    print("-1")
else:
    print(summ)