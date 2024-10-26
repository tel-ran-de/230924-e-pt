# Тема: Список, срезы списков.

# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
shopping_list = ["bread", "milk", "eggs"]


# Измените элемент "milk" на "almond milk".
el_to_change = shopping_list.index('milk')
shopping_list[el_to_change] = "almond milk"
# Создайте срез, содержащий первые два элемента списка.
slice_shopping_list = shopping_list[:2]
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
detailed_shopping_list = []
for element in shopping_list:
    price = float(input(f'Please input price for {element}: '))
    detailed_shopping_list.append([element, price])
# Выведите список покупок, срез и вложенный список.
print(5*'#', 'RESULT', 5*'#')
print(f'shopping_list: {shopping_list}', f'slice_shopping_list: {slice_shopping_list}',
      f'detailed_shopping_list: {detailed_shopping_list}', sep='\n' )

# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]


# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
students = ["Alice", "Bob", "Charlie", "David"]

# Измените имя второго студента на "Eve".
students[1] = "Eve"

# Создайте срез, содержащий студентов: "Bob", "Charlie".
top_students = students[1:3]

# Создайте вложенный список, где каждый студент имеет список своих оценок.
student_grades = [
    ["Alice", [90, 85, 88]],
    ["Eve", [75, 80, 82]],
    ["Charlie", [95, 92, 93]],
    ["David", [78, 85, 84]]]

# Выведите список студентов, срез и вложенный список.
print()
print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
print(top_students)  # Ожидаемый результат: ["Eve", "Charlie"]

print(student_grades)  # Ожидаемый результат:
# [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]


# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
tasks = ["task1", "task2", "task3", "task4"]


# Измените третью задачу на "task3 updated".
tasks[2] = "task3 updated"

# Создайте срез, содержащий последние две задачи.
last_tasks = tasks[2:]

# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
detailed_tasks = [
    ["task1", True],
    ["task2", False],
    ["task3 updated", True],
    ["task4", False]]

# Выведите список задач, срез и вложенный список.
print()
print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
print(last_tasks)  # Ожидаемый результат: ["task3", "task3 updated"]

print(detailed_tasks)  # Ожидаемый результат:
# [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]


# Тема: Методы списков

# Упражнение 1: Управление списком фильмов и их рейтингов
# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
movie_list = ["Movie1", "Movie2", "Movie3"]

# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
if "Movie4" not in movie_list:
    movie_list.append("Movie4")
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
if len(movie_list) > 2:
    movie_list[1] = "Updated Movie2"
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
if len(movie_list) <5 :
    movie_list.extend(["Movie5", "Movie6", "Movie7"])
# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
details = [['year', 'int'], ['rating', 'float']]
movie_details =[]
for movie in movie_list:
    element = [movie]
    for detail in details:
        detail_value = eval(f'{detail[1]}(input(f"pleas input value of {detail[0]} for {movie}: "))')
        element.append(detail_value)
    movie_details.append(element)
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
movie_details.insert(0, ["Movie", 2002, 7.7])
# 1.6 Выведите список фильмов и вложенный список.
print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
#["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]


# Упражнение 2: Анализ списка курсов и их продолжительности
# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".

courses = ["Python", "Java", "JavaScript"]

# 2.2 Добавьте в список курс "C++".
courses.append("C++")

# 2.3 Измените название второго курса на "Kotlin".
courses[1] = "Kotlin"

# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
if courses[:3] == ["Python", "Kotlin", "JavaScript"]:
    slice_courses = courses[:3]

# 2.5 Отсортируйте курсы по названиям.
courses_sorted = sorted(courses)

# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
course_details = [
    ["Python", 40],
    ["Kotlin", 30],
    ["JavaScript", 35],
    ["C++", 50]]

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
total_duration = sum(course[1] for course in course_details)

# 2.8 Выведите в консоль:
print()
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
print(courses_sorted)
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
print(slice_courses)
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
print(course_details)
# - общую продолжительность всех курсов. # Ожидаемый результат: 155
print(total_duration)

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

task_counter = 1
#
while True:

    # В решении используется цикл, чтобы программа работала пока вы ее принудительно не завершите через Ctr-C.
    # Циклы вы еще не проходили и для решения задачи эти знания не нужны. Просто пишите код с отступом, продолжая программу.
    print("\nСистема управления задачами")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    choice = input("Выберите действие, введя его номер: ")

    # Продолжите программу ниже. Код пишите с отсутпом, как принты выше.

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append([task_counter, task, False])
        task_counter += 1
        print(f"Задача '{task}' добавлена.")

    elif choice == "2":
        if not tasks:
            print("Задач нет.")
        else:
            for task in tasks:
                status = "Выполнено" if task[2] else "Не выполнено"
                print(f"{task[0]}. {task[1]} - {status}")

    elif choice == "3":
        task_num = int(input("Введите номер задачи для отметки как выполненной: "))
        for task in tasks:
            if task[0] == task_num:
                task[2] = True
                print(f"Задача '{task[1]}' отмечена как выполненная.")
                break
        else:
            print("Некорректный номер задачи.")

    elif choice == "4":
        task_num = int(input("Введите номер задачи для удаления: "))
        for task in tasks:
            if task[0] == task_num:
                tasks.remove(task)
                print(f"Задача '{task[1]}' удалена.")
                break
        else:
            print("Некорректный номер задачи.")

    elif choice == 'exit':
        exit()


