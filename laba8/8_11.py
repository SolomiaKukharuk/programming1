#https://www.eolymp.com/uk/submissions/15383492
def Summ(n):
    s = 0
    while True:
        o = n % 10
        s += 45*(n//10) + o*(o+1)//2
        
        if n < 10: break
        n //= 10
    return s

p, q = map(int, input().split())
while p > -1 and q > -1:
    print(Summ(q) - Summ(p-1))
    p, q = map(int, input().split())
