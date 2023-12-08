def ex_a(filename):
    with open(filename) as file:
          word_lis = {}
        for line in file:
            for el in line.split():
                if el not in word_lis:
                    word_lis[el] = len(el)
        max_key, max_value = max(word_lis.items(), key=lambda x: x[1])
    return f"Максимальне слово з довжиною {max_value} - {max_key}"

def ex_b(filename):
    with open(filename) as file:
        res = 0
        for line in file:
            res += len(line.split())
    return res

def ex_c(filename):
    new_lines = []
    with open(filename) as file:
        for el in file.split():
             if len(el) != 1:
                    new_line += el
                    new_line += ' '
            new_lines.append(new_line.split())

    with open(files, 'w') as file2:
        for line in new_lines:
            for el in line:
                file2.write(el)
                file2.write(' ')
            file2.write('\n')


files = input('Введіть розташування файлу')
ex_c(files)