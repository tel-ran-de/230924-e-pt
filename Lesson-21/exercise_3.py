# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

x_word = 'this'



# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt



def read_and_count_lines_in_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        remaining_data = ''

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            combined_data = remaining_data + chunk
            lines = combined_data.split('\n')

            # Все строки, кроме последней, являются полными строками
            line_count = len(lines) - 1

            # Последняя строка может быть неполной, сохраняем её для следующего чанка
            remaining_data = lines[-1]

            yield line_count

        # Добавляем последнюю строку, если она не пустая
        if remaining_data:
            yield 1

# Пример использования
file_path = 'text_files/data.txt'
chunk_size = 100

for line_count in read_and_count_lines_in_chunks(file_path, chunk_size):
    print(f"Lines in this chunk: {line_count}")



# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
