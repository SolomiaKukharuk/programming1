coefa = int(input("Введіть коефіціент біля x^2 - "))
coefb = int(input("Введіть коефіціент біля x - "))
coefc = int(input("Введіть вільний член - "))
assert coefa != 0, "Коефіціент а не може бути рівним нулю, тоді це рівняння не буде квадратним"
print((coefb ** 2) - 4 * coefa * coefc)
x = 0
assert ((coefb ** 2) - 4 * coefa * coefc) >= 0, "Це рівняння не має розв'язків над полем дійсних чисел"
dis = (coefb ** 2) - 4 * coefa * coefc
if dis == 0:
    x = (coefb * -1) / (2 * coefa)
    print(f"Це рівняння має один корінь - {format(x, '.0f')}")
elif dis > 0:
    x_1 = ((coefb * -1) - dis ** 0.5) / (2 * coefa)
    x_2 = ((coefb * -1) + dis ** 0.5) / (2 * coefa)
    print(f"Це рівняння має два кореня - {format(x_1, '.0f')} {format(x_2, '.0f')}")