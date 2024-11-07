# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
file_r = open('text_files/data.txt', 'r')
content = file_r.read()
print(content)
print("------------------")
file_r.seek(0)
content = file_r.read(10)
print(content)
print("------------------")
file_r.seek(0)
content = file_r.readline()
print(content)
print("------------------")
file_r.seek(0)
content = file_r.readlines()
print(*content)
file_r.close()
# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
print("----------Задание 2.--------")
file_make_output = open('text_files/output.txt', 'w')
file_make_output.write('Hello, World!\n')
lines = ["This is line 1\n", "This is line 2\n"]
file_make_output.writelines(lines)
print(*lines)
file_make_output.close()

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
print("----------Задание 3.--------")
file_make_log = open('text_files/log.txt', 'w')
file_make_log.write("New log entry\n")
lines = ["Log entry 1\n", "Log entry 2\n"]
file_make_log.writelines(lines)
print(*lines)
file_make_log.close()
# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.

