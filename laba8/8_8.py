#https://www.eolymp.com/uk/submissions/15383407
def qpow(n):
    if n <= 1: return ''

    if n & 0x01:
        return qpow(n-1) + 'X'
    else:
        return qpow(n//2) + 'S'

n = int(input())
print(qpow(n))
