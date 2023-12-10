def len_of_lis(lis):
    if not lis:
        return 0
    return 1 + len_of_lis(lis[1:])


def sum_of_elem(lis):
    if not lis:
        return 0
    return lis[0] + sum_of_elem(lis[1:])


lis = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
print(f"Кількість елементів списку дорівнює - {len_of_lis(lis)}")
print(f"Сума елементів списку дорівнює - {sum_of_elem(lis)}")
print(f"Максимальне відношення списку - {max(lis) / min(lis)}")