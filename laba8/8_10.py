#https://www.eolymp.com/uk/submissions/15383465
def perestanovky(arr):
    if len(arr) <= 1:
        return [arr]
    
    p = []
    for i in range(len(arr)):
        pr = perestanovky(arr[:i] + arr[i+1:])
        for j in pr:
            p.append([arr[i]] + j)
    return p

n = int(input())
for p in perestanovky(list(range(1, n + 1))):
    print(*p, sep=" ")
