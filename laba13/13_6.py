def correct_text(line):
    length = 40
    mas_of_lines = []
    i = 1
    k = 0
    while True:
        mas_of_lines.append(line[length * k: length * i])
        i += 1
        k += 1
        if length * i > len(line):
            mas_of_lines.append(line[length * k: len(line)])
            break
    return mas_of_lines


some_text = input()
with open('text.txt', 'w') as file:
    for line in correct_text(some_text):
        print(line, file=file)