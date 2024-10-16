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
spisok = ["bread", "milk", "eggs"]
spisok[1] = "almond milk"
print(spisok)
print(spisok[0:2])
print([
    [spisok[0], "1,2$"],
    [spisok[1], "2,3$"],
    [spisok[2], "3,1$"]
])
print()

# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
# Измените имя второго студента на "Eve".
# Создайте срез, содержащий студентов: "Bob", "Charlie".
# Создайте вложенный список, где каждый студент имеет список своих оценок.

# Выведите список студентов, срез и вложенный список.
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат:
# [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]
stud_list = ["Alice", "Bob", "Charlie", "David"]
print(stud_list[1:3])
stud_list[1] = "Eve"
print([
    [stud_list[0], [5, 5, 4]],
    [stud_list[1], [4, 4, 5]],
    [stud_list[2], [3, 3, 4]],
    [stud_list[3], [3, 2, 2]]
])
print()

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
task_list = ["task1", "task2", "task3", "task4"]
last_tasks = task_list[2:4]
task_list[2] = "task3 updated"
detailed_tasks = [
    [task_list[0], True],
    [task_list[1], False],
    [task_list[2], True],
    [task_list[3], False]
]
print(task_list)
print(last_tasks)
print(detailed_tasks)
print()

# Тема: Методы списков

# Упражнение 1: Управление списком фильмов и их рейтингов
# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
films_list = ["Movie1", "Movie2", "Movie3"]
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
if "Movie4" in films_list:
    print("Данный фильм уже содержится в списке")
else:
    films_list.append("movie4")
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
films_list2 = ["movie5", "Movie6", "Movie7"]
film_qantity = int(len(films_list))
if film_qantity > 2:
    films_list[1] = "Updares Movie2"
# пробовал эту строку через elif, не работает почему то
if film_qantity < 5:
    films_list.extend(films_list2)
else:
    print()
# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
films_detals = [
    ["Movie1", 2010, 8.1],
    ["Updated Movie2", 2015, 7.5],
    ["Movie3", 2020, 8.6],
    ["Movie4", 2021, 7.9],
    ["Movie5", 2013, 8.5],
    ["Movie6", 2018, 8.6],
    ["Movie7", 2023, 7.0]
]
# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
films_detals.insert(0, ["Movie", 2002, 7.7])
# 1.6 Выведите список фильмов и вложенный список.
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
print(films_list)
print(films_detals)

# Упражнение 2: Анализ списка курсов и их продолжительности
# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
kurses = ["Python", "Java", "JavaScript"]
# 2.2 Добавьте в список курс "C++".
kurses.append("C++")
# 2.3 Измените название второго курса на "Kotlin".
kurses[1] = "Kotlin"
# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
if kurses[0:3] == (["Python", "Kotlin", "JavaScript"]):
    print(kurses[0:3])
# 2.5 Отсортируйте курсы по названиям.
kurses.sort()
print(kurses)
# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
kurses_details = [
    ["Python", 40],
    ["Kotlin", 30],
    ["JavaScript", 35],
    ["C++", 50]
]
print(kurses_details)
# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
print(kurses_details[0] [1] + kurses_details[1] [1] + kurses_details[2] [1] + kurses_details[3] [1])
# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155


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

tasks = []
while True:

# В решении используется цикл, чтобы программа работала пока вы ее принудительно не завершите через Ctr-C.
# Циклы вы еще не проходили. Для решения задачи эти знания не нужны. Просто пишите код с отступом, продолжая программу.

    print("\nСистема управления задачами")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    choice = input("Выберите действие, введя его номер: ")

    # Продолжите программу ниже. Код пишите с отсутпом, как принты выше.

    if choice == '1':
        task_description = input("Введите описание задачи: ")
        task_number = len(tasks) + 1
        tasks.append([task_number, task_description, False])
        print(f"Задача добавлена: {task_number}. {task_description}")

    elif choice == '2':
        if not tasks:
            print("Нет задач для отображения.")
        else:
            print("Список задач:")
            for task in tasks:
                status = "Выполнена" if task[2] else "Не выполнена"
                print(f"{task[0]}. {task[1]} - {status}")

    elif choice == '3':
        task_number = int(input("Введите номер задачи, чтобы отметить как выполненную: "))
        found = False
        for task in tasks:
            if task[0] == task_number:
                task[2] = True
                print(f"Задача {task_number} отмечена как выполненная.")
                found = True
                break
        if not found:
            print("Некорректный номер задачи.")

    elif choice == '4':
        task_number = int(input("Введите номер задачи, чтобы удалить ее: "))
        found = False
        for i in range(len(tasks)):
            if tasks[i][0] == task_number:
                tasks.pop(i)
                print(f"Задача {task_number} удалена.")
                found = True
                break
        if not found:
            print("Некорректный номер задачи.")

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 4.")