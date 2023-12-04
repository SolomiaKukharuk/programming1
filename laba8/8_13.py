#https://www.eolymp.com/uk/submissions/15383502
from math import gcd
import sys

mod = 10**8

def fib(n):
    f0, f1 = 1, 1
    for _ in range(n-2):
        f0, f1 = f1 % mod, (f0 + f1) % mod
    return f1

def mul_mat(m1, m2):
    mm = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(mm)):
        for j in range(len(mm[0])):
            res = 0
            for k in range(len(m1)):
                res += m1[i][k] * m2[k][j]
            mm[i][j] = res % mod 
    return mm
    
def pow_mat(m, p):
    res = [[1,0], 
           [0,1]]
    
    while p:
        if p & 0x01: 
            res = mul_mat(res, m) 
        m = mul_mat(m, m)
        p >>= 1
    
    return res

def mat_fib(n):
    q = [[1, 1],
         [1, 0]]

    q = pow_mat(q, n)
    return q[0][1]

for line in sys.stdin:
    n, m = map(int, line.split())
    print(mat_fib(gcd(n, m)))
