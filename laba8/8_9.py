#https://www.eolymp.com/uk/submissions/15383436
def ch(c):
    if c < 10: return str(c)
    else: return chr(ord('A') + c - 10)

def s13(n):
    if not n:
        return ''
    return s13(n // 13) + ch(n % 13)     

n = int(input())

print(s13(n))
