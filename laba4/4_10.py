res = 0
n = abs(int(input()))
if n == 1:
    for i in range(100, 1000):
        if i % 2 == 0:
            res += i
elif n == 2:
    for i in range(100, 1000):
        digs = [int(dig) for dig in str(i)]
        if digs[0] < digs[1] < digs[2]:
            res += 1
elif n == 3:
    for i in range(100, 1000):
        digs = [int(dig) for dig in str(i)]
        if digs[0] % 2 != 0 and digs[1] % 2 != 0 and digs[2] % 2 != 0:
            res += i
elif n == 4:
    for i in range(100, 1000):
        digs = [int(dig) for dig in str(i)]
        if digs[0] > digs[1] > digs[2]:
            res += 1
elif n == 5:
    for i in range(100, 1000):
        digs = [int(dig) for dig in str(i)]
        if i == sum([dig ** 3 for dig in digs]):
            res += i
elif n == 6:
    for i in range(100, 1000):
        digs = set([int(dig) for dig in str(i)])
        if len(digs) == 3:
            res += 1
print(res)