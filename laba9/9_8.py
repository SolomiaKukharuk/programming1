#https://www.eolymp.com/uk/submissions/15408519
import math
n = int(input())
lst = map(int, input().split())
lst = set(lst)
dic = {}
for i in lst:
    if abs(i) not in dic:
          dic[abs(i)] = []
print(len(dic))