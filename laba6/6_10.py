#https://www.eolymp.com/uk/submissions/14963980
s = input()
alphabet = "abcdefghijklmnopqrstuvwxzy"
for letter in alphabet:
  s = s.replace(letter,letter*2)
print(s)