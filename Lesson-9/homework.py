# Тема: Список, срезы списков.

# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".

# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.

# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]
# РЕШЕНИЕ:
# shoping_list = ["bread", "milk", "eggs"]
# shoping_list[1] = "almond milk"
# print(shoping_list)
# slice_shoping_list = shoping_list[0:2]
# print(slice_shoping_list)
# detailed_shopping_list = [[shoping_list[0], 1.5], [shoping_list[1], 3.0], [shoping_list[2], 2.0]]
# print(detailed_shopping_list)


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
# Измените имя второго студента на "Eve".
# Создайте срез, содержащий студентов: "Bob", "Charlie".
# Создайте вложенный список, где каждый студент имеет список своих оценок.
#

# Выведите список студентов, срез и вложенный список.
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат:
# [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]
#
# students = ["Alice", "Bob", "Charlie", "David"]
# print(students)
# slice_students = students[1:3]
# print(slice_students)
# students[1] = "Eve"
# students_grades = [[students[0], [90, 85, 88]], [students[1], [75, 80, 82]], [students[2], [95, 92, 93]], [students[3], [78, 85, 84]]]
# print(students_grades)


# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
# Измените третью задачу на "task3 updated".
# Создайте срез, содержащий последние две задачи.
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).

# Выведите список задач, срез и вложенный список.
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат:
# [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]

# tasks = ["task1", "task2", "task3", "task4"]
# old_tasks = tasks[:]
# tasks[2] = "task3 updated"
# print(tasks)
# last_tasks = old_tasks[2:]
# print(last_tasks)
# old_tasks[1] = "task2 updated"
# print([[old_tasks[0], True], [old_tasks[1], False], [old_tasks[2], True], [old_tasks[3], False]])


# Тема: Методы списков

# Упражнение 1: Управление списком фильмов и их рейтингов
# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
# 1.6 Выведите список фильмов и вложенный список.
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
# movie_list = ["Movie1", "Movie2", "Movie3"]
#
# if "Movie4" not in movie_list:
#     movie_list.append("Movie4")
# if len(movie_list) > 2:
#     movie_list[1] = "Updated Movie2"
# if len(movie_list) < 5:
#     new_list = movie_list + ["Movie5", "Movie6", "Movie7"]
# new_big_list = [["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
# new_big_list.insert(0, ["Movie", 2002, 7.7])
# print(new_big_list)

# Упражнение 2: Анализ списка курсов и их продолжительности
# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
# 2.2 Добавьте в список курс "C++".
# 2.3 Измените название второго курса на "Kotlin".
# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
# 2.5 Отсортируйте курсы по названиям.
# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
# 2.8 Выведите в консоль:
# - отсортированный список курсов, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155

# main_list = ["Python", "Java", "JavaScript"]
# new_list = main_list + ["C++"]
# new_list[1] = "Kotlin"
# slice_list = new_list[0:3]
# print(slice_list)
# new_list.sort()
# print(new_list)
# v_list = [["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]]
# print(v_list)
# print(sum([v_list[0][1], v_list[1][1], v_list[2][1], v_list[3][1]]))




# Мини-проект: Система управления задачами (To-Do List)

# Описание проекта:
# Создайте простую систему управления задачами, которая позволяет пользователям
# добавлять, удалять, и отмечать задачи как выполненные.
#
# Требования:
# 1. Программа должна запрашивать у пользователя ввод задачи. Программа должна преобразовывать введенную пользователем
# задачу в список, где первым элементом идет номер задачи, вторым задача, а третьим статус ее выполнения.
# При создании задачи статус всегда False. Список с задачей добавляется во вложенный список со всеми задачами tasks.

# 2. Программа должна выводить список задач.

# 3. Пользователь должен иметь возможность отметить задачу как выполненную. Для этого программа должна запросить у него
# номер задачи. Если такого номера нет, то вывести сообщение "Некорректный номер задачи.".
# Если номер корректный, то поменять статус задачи на True.

# 4. Пользователь должен иметь возможность удалить задачу. Чтобы удалить задачу, запросите ее номер.
# Если номер корректный, то удалите ее.
#
# tasks = []
# #
# while True:
# # #     # В решении используется цикл, чтобы программа работала пока вы ее принудительно не завершите через Ctr-C.
# # #     # Циклы вы еще не проходили и для решения задачи эти знания не нужны. Просто пишите код с отступом, продолжая программу.
#     print("\nСистема управления задачами")
#     print("1. Добавить задачу")
#     print("2. Показать задачи")
#     print("3. Отметить задачу как выполненную")
#     print("4. Удалить задачу")
#     choice = int(input("Выберите действие, введя его номер: "))
#
#     if choice == 1:
#         task = input("Добавьте задачу: ")
#         num_task = len(tasks) + 1
#         status_task = False
#         tasks.append([num_task, task, status_task])
#         print(f"Задача {task} Добавлено!")
#     elif choice == 2:
#         print(*tasks, sep="\n")
#     elif choice == 3:
#         num = input("Введите номер задачи, как выполненную: ")
#         for task in tasks:
#             if task[0] == num:
#                 task[2] = True
#                 print(f"Статус задачи номер {num} изменен на выполненную!")
















#
#     # Продолжите программу ниже. Код пишите с отсутпом, как принты выше.

