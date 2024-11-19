# Тема: Модуль datetime
# Покажите в режиме live-coding и объясните как использовать модуль datetime:
# - получать дату и время,
# - производить с ними сложения и вычитания,
# - конвертировать в строку и обратно.
#
import datetime
#
# 1. Получение текущей даты и времени
# now = datetime.datetime.now()
# print(now)  # Вывод: текущие дата и время, например, 2024-05-21 15:26:53.123456
# print(type(now))
#
# 2. Получение текущей даты
# today = datetime.date.today()
# print(today)  # Вывод: текущая дата, например, 2024-05-21
# print(type(today))
#
# # 3. Создание объекта даты
# my_date = datetime.date(2023, 5, 21)
# # my_date = datetime.date(year=2023, month=5, day=21)
# print(my_date)  # Вывод: 2023-05-21
#
# # 4. Создание объекта времени
# my_time = datetime.time(15, 30, 0)
# print(my_time)  # Вывод: 15:30:00
#
# # 5. Создание объекта даты и времени
# my_datetime = datetime.datetime(2023, 5, 21, 15, 30, 0)
# print(my_datetime)  # Вывод: 2023-05-21 15:30:00
#
# # 6. Разбор строки в объект даты и времени (строка -> datetime)
# date_string = "2023-05-21 15:30:00"
# date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(date_object)  # Вывод: 2023-05-21 15:30:00
# print(type(date_object))
# print(type(date_string))
#
# # 7. Форматирование объекта даты и времени в строку (datetime -> строка)
# now = datetime.datetime.now()
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# formatted_date2 = now.strftime("%d.%m.%Y %H:%M:%S")
# formatted_date3 = now.strftime("%W week %d %B'%y %A")
# formatted_date4 = now.strftime("%W-ая неделя %Y-го года")
# print(formatted_date)  # Вывод: 2024-05-21 15:26:53
# print(formatted_date2)  # Вывод: 21.05.2024 15:26:53
# print(formatted_date3)  # Вывод: 19 week 21 May'24 Thursday
# print(formatted_date4)  # Вывод: Неделя 19 2024-го года
#
# # 8. Получение компонента даты или времени
# now = datetime.datetime.now()
# print(now.year)    # Вывод: текущий год, например, 2024
# print(now.month)   # Вывод: текущий месяц, например, 5
# print(now.day)     # Вывод: текущий день, например, 21
# print(now.hour)    # Вывод: текущий час, например, 15
# print(now.minute)  # Вывод: текущая минута, например, 26
# print(now.second)  # Вывод: текущая секунда, например, 53
#
# # 9. Вычисление разницы между двумя датами (timedelta)
# date1 = datetime.date(2023, 5, 21)
# date2 = datetime.date(2022, 5, 21)
# difference = date1 - date2
# print(difference)  # Вывод: timedelta(days=365)
# print(type(difference))
# print(difference.days)  # Вывод: 365
#
# # 10. Добавление или вычитание времени с использованием timedelta
# now = datetime.datetime.now()
# future = now + datetime.timedelta(days=42)
# print(future)  # Вывод: дата и время через 42 дня от текущей
# #
# past = now - datetime.timedelta(days=10, hours=2, minutes=30)
# print(past)  # Вывод: дата и время 10 дней назад от текущей
#
# # 11. Работа с часовыми поясами
# import pytz  # pip install pytz
#
# utc = pytz.UTC
# eastern = pytz.timezone('US/Eastern')
#
# now = datetime.datetime.now(utc)
# print(now)  # Вывод: текущие дата и время в UTC
#
# eastern_time = now.astimezone(eastern)
# print(eastern_time)  # Вывод: текущие дата и время в часовом поясе US/Eastern



# Тема: Модуль os
# Покажите в режиме live-coding и объясните:
# - Как работать с модулем os.
# - Основные команды: getcwd, listdir, mkdir, remove, rmdir, rename.
#
import os
#
# # 1. Получение текущей рабочей директории
# current_directory = os.getcwd()
# print(current_directory)  # Вывод: текущая рабочая директория

# # 2. Изменение текущей рабочей директории
# os.chdir('../../QA422')
# print(os.getcwd())  # Вывод: новая рабочая директория C:\Users\maks\PycharmProjects\QA422
#
# # 3. Список файлов и директорий в указанной директории
# '.' - текущая директория
# '..' - родительская директория
# files_and_directories = os.listdir('..')
# print(files_and_directories)  # Вывод: ['.gitignore', '.idea', '.venv', 'Lesson-10', 'Lesson-11', 'Lesson-12', 'Lesson-13', 'Lesson-14', 'Lesson-15', 'Lesson-16', 'Lesson-17', 'Lesson-18', 'Lesson-19', 'Lesson-2', 'Lesson-20', 'Lesson-21', 'Lesson-22', 'Lesson-23', 'Lesson-24', 'Lesson-3', 'Lesson-4', 'Lesson-5', 'Lesson-6', 'Lesson-7', 'Lesson-8', 'Lesson-9', 'manuals']
# files_and_directories = os.listdir('.')
# print(files_and_directories)  # ['examples.py', 'exercise_1.py', 'exercise_2.py', 'exercise_3.py', 'homework.py', 'live-coding.py', 'Урок 19. Модули  datetime и os.pptx']
#
# # 4. Создание новой директории
# os.mkdir('new_directory')  # Создает директорию с именем 'new_directory'
#
# # 5. Удаление директории
# os.rmdir('new_directory')  # Удаляет директорию с именем 'new_directory'
#
# # 6. Удаление файла
# os.remove('file1.txt')  # Удаляет файл с именем 'file1.txt'
#
# # 7. Переименование файла или директории
# os.rename('old_name.txt', 'new_name.txt')  # Переименовывает 'old_name.txt' в 'new_name.txt'
#
# # 8. Проверка существования файла или директории
# exists = os.path.exists('new_name.txt')  # True
# exists2 = os.path.exists('old_name.txt')  # False
# print(exists)  # Вывод: True, если файл существует, иначе False
# print(exists2)  # Вывод: True, если файл существует, иначе False
#
# # 9. Получение информации о файле или директории
# info = os.stat('live-coding.py')
# print(info)  # Вывод: os.stat_result(st_mode=33206, st_ino=5066549580835969, st_dev=1826509369, st_nlink=1, st_uid=0, st_gid=0, st_size=8169, st_atime=1731666364, st_mtime=1731666364, st_ctime=1731658323)
# print(info.st_mode)  # Вывод: 33206
# print(info.st_size)  # Вывод: 8169
# print(info.st_mtime)  # Вывод: 1731666364
#
# # 10. Создание вложенных директорий
# os.makedirs('parent_directory/child_directory')  # Создает директорию 'parent_directory' и вложенную 'child_directory'
#
# # 11. Удаление вложенных директорий
# os.removedirs('parent_directory/child_directory')  # Удаляет директорию 'child_directory' и пустую 'parent_directory'
#
# # 12. Выполнение системных команд
# print(os.getcwd())
# os.system('echo hello > file.txt')  # Выполняет команду echo в системной оболочке
#
# # 13. Получение значений переменных окружения
# path = os.environ.get('PATH')
# print(path)  # Вывод: значение переменной окружения PATH
# #
# # # 14. Установка значений переменных окружения
# os.environ['NEW_VAR'] = 'value'
# print(os.environ['NEW_VAR'])  # Вывод: значение новой переменной окружения NEW_VAR
#
# # 15. Разделение пути на директорию и файл
# directory, filename = os.path.split(r'C:\Users\maks\PycharmProjects\141024-m-pt\Lesson-24\examples.py')
# print(directory)  # Вывод: C:\Users\maks\PycharmProjects\141024-m-pt\Lesson-24
# print(filename)  # Вывод: examples.py
#
# # 16. Получение абсолютного пути
# absolute_path = os.path.abspath('examples.py')
# print(absolute_path)  # Вывод: C:\Users\maks\PycharmProjects\141024-m-pt\Lesson-24\examples.py
#
# # 17. Проверка, является ли путь файлом
# print(os.path.isfile('../Lesson-24/examples.py'))  # Вывод: True
# print(os.path.isfile('../Lesson-24'))  # Вывод: False
#
# # 18. Проверка, является ли путь директорией
# print(os.path.isdir('../Lesson-24/examples.py'))  # Вывод: False
# print(os.path.isdir('../Lesson-24'))  # Вывод: True
