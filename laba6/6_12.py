#https://www.eolymp.com/uk/submissions/14964785
#код працює але еолімп видає тільки 74% , проблема не в тому що 
#у рядку можуть бути не тільки літери, він не виходить за межі вихідних данних
s1 = input()
s1 = s1.upper()
k = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet.upper()
for letter in s1:
    i = alphabet.index(letter)
    r = i - k
    lettr = alphabet[r]
    s1 = s1.replace(letter, lettr)
print(s1)