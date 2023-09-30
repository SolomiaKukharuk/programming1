m = int(input())
pl = 0

while str(m) != str(m)[::-1]:
    rm = int(str(m)[::-1])
    m += rm
    pl += 1

print(pl)