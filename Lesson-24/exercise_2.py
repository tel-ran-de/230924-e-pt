# Тема: Модуль os
import os

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.

# os.mkdir('test_dir')
# print ('Directory /"test_dir/" has been created !')
# curr_dir = os.listdir('.')
# dir_list = [item for item in curr_dir if os.path.isdir(item)]
# print(dir_list)
# os.rmdir('test_dir')
# print ('New directory has been deleted !')



# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.


with open ("temp_file.txt" , "w") as file:
    file.write("Temporary content")
    os.rename("temp_file.txt" , "renamed_file.txt")

curr_dir2 = os.listdir('.')
dir_list2 = [item for item in curr_dir2]
print(f"List of all files in current directory :{dir_list2}")


# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".


# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".

