runtime_error_count = 0
type_error_count = 0
value_error_count = 0

while True:
    user_input = input("Введіть число або 'досить' для завершення: ")

    if user_input.lower() == 'досить':
        break

    try:
        num = int(user_input)
        if num > 9:
            raise RuntimeError("Помилка: Введене число більше 9")
        elif num < 0:
            raise TypeError("Помилка: Введене число менше 0")
        elif 0 <= num <= 9:
            raise ValueError("Помилка: Введене число в діапазоні від 0 до 9")
    except RuntimeError as re:
        print(re)
        runtime_error_count += 1
    except TypeError as te:
        print(te)
        type_error_count += 1
    except ValueError as ve:
        print(ve)
        value_error_count += 1

print(f"\nЗвіт про виключення:")
print(f"RuntimeError: {runtime_error_count} випадків")
print(f"TypeError: {type_error_count} випадків")
print(f"ValueError: {value_error_count} випадків")