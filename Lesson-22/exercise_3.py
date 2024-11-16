# Тема: Дополнительная практика

# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]



def gen_far():
    for i in range(-10, 11):
        yield i

# (0 °C × 9/5) + 32 = 32 °F

#lamb_funk = map()
lambda_list = list(map(lambda x : x * 1.8 + 32, gen_far()))
print(lambda_list)







# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']




def len_string(words):
    return words.__len__() > 5

words = iter(["hello", "world", "python", "is", "awesome"])
lamb_string = filter(len_string, words)
print(list(lamb_string))






# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']




iter_1 = [i for i in range(1, 4)]
iter_2 = [i**3 for i in iter_1 ]

iter_zip = zip(iter_1, iter_2)
#print(list(iter_zip))

lambda_list = list(map(lambda pair: f"{pair[0]}: {pair[1]}", zip(iter_1, iter_2)))

print(lambda_list)



# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.
def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def contains_digit(line):
    for char in line:
        return char.isdigit()


# Создаем генератор для чтения строк из файла data.txt
file_path = 'text_files/data.txt'
lines = read_file_lines(file_path)

# Используем filter с функцией contains_digit для отбора строк, содержащих числа
filtered_lines = filter(contains_digit, lines)


# Применяем map с лямбда функцией для преобразования строк в целые числа
numbers = list(map(lambda line: int(''.join(filter(lambda char: char.isdigit(), line))), filtered_lines))

print(numbers)









# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".
