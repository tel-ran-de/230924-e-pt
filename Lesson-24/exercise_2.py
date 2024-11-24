# Тема: Модуль os


# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.
print("---------------------Задание 1-----------------------------")
import os


def create_and_remove_directory():
    dir_name = "test_directory"

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Директория '{dir_name}' создана.")
    else:
        print(f"Директория '{dir_name}' уже существует.")

    all_dirs = [d for d in os.listdir() if os.path.isdir(d)]
    print("Список всех директорий в текущем каталоге:")
    print(all_dirs)

    if os.path.exists(dir_name): # Удаление
        os.rmdir(dir_name)
        print(f"Директория '{dir_name}' удалена.")
    else:
        print(f"Директория '{dir_name}' не существует для удаления.")


# Вызов функции
create_and_remove_directory()

# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.
print("---------------------Задание 2-----------------------------")
def create_and_rename_file():
    original_file = "temp_file.txt"
    renamed_file = "renamed_file.txt"

    # Проверка существования файла перед созданием
    if not os.path.exists(original_file):
        with open(original_file, "w") as file:
            file.write("Temporary content")
        print(f"Файл '{original_file}' создан и содержимое записано.")

    # Переименование файла
    if os.path.exists(original_file):
        os.rename(original_file, renamed_file)
        print(f"Файл '{original_file}' переименован в '{renamed_file}'.")
    else:
        print(f"Файл '{original_file}' не существует для переименования.")

    # Список всех файлов
    all_files = [f for f in os.listdir() if os.path.isfile(f)]
    print("Список всех файлов в текущем каталоге:")
    print(all_files)

create_and_rename_file()



# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".
print("---------------------Задание 3-----------------------------")
def check_file_existence():
    file_name = "examples.py"

    if os.path.exists(file_name) and os.path.isfile(file_name):
        file_size = os.path.getsize(file_name)
        print(f"Файл '{file_name}' существует. Его размер: {file_size} байт.")
    else:
        print(f"Файл '{file_name}' не найден.")

check_file_existence()


# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".
print("---------------------Задание 4-----------------------------")
def compare_file_sizes(file1, file2):
    if not os.path.exists(file1):
        print(f"Файл '{file1}' не найден.")
        return
    if not os.path.exists(file2):
        print(f"Файл '{file2}' не найден.")
        return

    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    if size1 > size2:
        print(f"Файл '{file1}' больше, его размер: {size1} байт.")
    elif size1 < size2:
        print(f"Файл '{file2}' больше, его размер: {size2} байт.")
    else:
        print("Файлы имеют одинаковый размер.")

file_name1 = input("Введите имя первого файла: ")
file_name2 = input("Введите имя второго файла: ")
compare_file_sizes(file_name1, file_name2)
