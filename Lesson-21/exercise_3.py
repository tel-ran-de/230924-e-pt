# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

def read_filter(file_path, x_word):
    with open(file_path, "r") as file:
        for line in file:
            if x_word.lower() in line.lower():
                yield line.strip()
fileExmpl = 'text_files/data.txt'
x_word = 'This'
try:
fltr_lines = read_filter(fileExmpl, x_word)
for string in fltr_lines:
    print(string)

# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt



# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
