#https://www.eolymp.com/uk/submissions/15031497
def is_palindrome(s):
    return s == s[::-1]

n = int(input())


found_bases = []
for base in range(2, 37):
    num_in_base = ""
    temp_n = n
    while temp_n > 0:
        remainder = temp_n % base
        num_in_base += str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10)
        temp_n //= base

    if is_palindrome(num_in_base):
        found_bases.append(base)

if len(found_bases) == 0:
    print("none")
elif len(found_bases) == 1:
    print("unique")
    print(found_bases[0])
else:
    print("multiple")
    print(" ".join(map(str, found_bases)))