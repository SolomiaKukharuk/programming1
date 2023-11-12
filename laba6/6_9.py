#https://www.eolymp.com/uk/submissions/14965441
s = input()
n = 0
a = '*/-+%'
if '**' in s:
    n += s.count('**')
if '//' in s:
    n += s.count('//')
s = s.replace('**', '')
s = s.replace('//', '')
for ch in a:
    for i in s:
        if i == ch:
            n += 1
print(n)