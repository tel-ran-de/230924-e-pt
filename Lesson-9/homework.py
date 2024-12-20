# FIXED

# Тема: Список, срезы списков.

# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
shopping_list = ["bread", "milk", "eggs"]


# Измените элемент "milk" на "almond milk".
shopping_list[1] = "almond milk"

print(shopping_list)


# Создайте срез, содержащий первые два элемента списка.
slice_shopping_list = shopping_list[:2]

# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
detailed_shopping_list = [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]

# Выведите список покупок, срез и вложенный список.
print(shopping_list)  # ["bread", "almond milk", "eggs"]
print(slice_shopping_list)  # ["bread", "almond milk"]
print(detailed_shopping_list)  # [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]

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

# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
students = ["Alice", "Bob", "Charlie", "David"]
# Создайте срез, содержащий студентов: "Bob", "Charlie".
top_students = students[1:3]
# Измените имя второго студента на "Eve".
students[1] = "Eve"
# Создайте вложенный список, где каждый студент имеет список своих оценок.
student_grades = []
subjects = ['math', 'algorithm', 'design']
for student in students:
    marks = []
    for subject in subjects:
        marks.append(int(input(f'Please input mark by {subject} for {student}: ')))
    student_grades.append([student, marks])

# Выведите список студентов, срез и вложенный список.
print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]

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

# Измените третью задачу на "task3 updated".
tasks[2] = "task3 updated"
# Создайте срез, содержащий последние две задачи.
last_tasks = tasks[-2:]
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
detailed_tasks = []
for task in tasks:
    status = bool(int(input(f"Please input 1 if {task} completed, or 0 if didn't: ")))
    detailed_tasks.append([task, status])
# Выведите список задач, срез и вложенный список.
print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]

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
if len(movie_list) < 5:
    movie_list.extend(["Movie5", "Movie6", "Movie7"])

# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
movie_details = [
    ["Movie1", 2010, 8.1],
    ["Updated Movie2", 2015, 7.5],
    ["Movie3", 2020, 8.6],
    ["Movie4", 2021, 7.9],
    ["Movie5", 2013, 8.5],
    ["Movie6", 2018, 8.6],
    ["Movie7", 2023, 7.0]]

# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
movie_details.insert(0, ["Movie", 2002, 7.7])

# 1.6 Выведите список фильмов и вложенный список.
print()
print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]

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
subjects = ["Python", "Java", "JavaScript"]
print(subjects)
# 2.2 Добавьте в список курс "C++".
subjects.append("C++")
print(subjects)
# 2.3 Измените название второго курса на "Kotlin".
subjects[1] = "Kotlin"
print(subjects)
# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
subjects_slice = []
if ["Python", "Kotlin", "JavaScript"] == subjects[:3]:
    subjects_slice = subjects[:3]
print(subjects_slice)
# 2.5 Отсортируйте курсы по названиям.
subjects_sorted = sorted(subjects)
print(subjects_sorted)

# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
subjects_extended = []
for subject in subjects:
    duration = int(input(f"введите продолжительность курса {subject} в часах: "))
    subjects_extended.append([subject, duration])

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
total_duration_1 = 0
for items in subjects_extended:
    total_duration_1 += items[1]

total_duration_2 = sum([item[1] for item in subjects_extended])
# 2.8 Выведите в консоль:
print(subjects_sorted, subjects_slice, subjects_extended, total_duration_1, total_duration_2, sep='\n')
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


# в процессе создания, задаче будет присваивается id
# id будет генерироваться в виде последовательности начиная с 1
id = 1
while True:
#     # В решении используется цикл, чтобы программа работала пока вы ее принудительно не завершите через Ctr-C.
#     # Циклы вы еще не проходили и для решения задачи эти знания не нужны. Просто пишите код с отступом, продолжая программу.
     print("\nСистема управления задачами")
     print("1. Добавить задачу")
     print("2. Показать задачи")
     print("3. Отметить задачу как выполненную")
     print("4. Удалить задачу")
     choice = int(input("Выберите действие, введя его номер: "))

     if choice not in [1, 2, 3, 4]:
         print('Ваш выбор неверен. Ведите число согласно установленного выбора!')
     # Продолжите программу ниже. Код пишите с отсутпом, как принты выше.
     else:
         if choice == 1:
             text = input('Введите текст задачи: ')
             status = False
            # Задача добавляется в список.
             tasks.append([id, text, status])
             print(f'Ваша задача: {text.upper()} добавлена в список под номером {id} со статусом {status} ')
             id = id + 1
            # Если мы не дополняем список, то в начале распечатывается список задач в виде таблицы
         elif choice > 1:
             print(50 * '-')
             print(f'| id |           задача               |  status  |')
             print(50 * '-')
             for task in tasks:
                 # такое нагромождение связано с выравниванием столбцов в таблице
                 print(f'|{(3-len(str(task[0])))*" "}{task[0]} |{(31-len(str(task[1])))*" "}{task[1]} |'
                       f'{(9-len(str(task[2])))*" "}{task[2]} |')
                 print(50 * '-')
             if choice == 3:
                 executed_task = int(input('выбирете номер выполненной задачи: '))
                 # проверяем есть ли в списке задача с введенным номером
                 if executed_task not in [item[0] for item in tasks]:
                     print('Вы ввели неверный номер задачи')
                 else:
                     for task in tasks:
                         if task[0] == executed_task:
                             task[2] = True
                             print(f'статус задачи {task[1].upper()} под номером {task[0]} изменен на ВЫПОЛНЕНО ')
             elif choice == 4:
                 task_to_delete = int(input('выбирете номер удаляемой задачи: '))
                 # проверяем есть ли в списке задача с введенным номером
                 if task_to_delete not in [item[0] for item in tasks]:
                     print('Вы ввели неверный номер задачи')
                 else:
                    for task in tasks:
                        if task[0] == task_to_delete:
                            # Просим подтвердить удаление.
                            check = input(f'подтвердите удаление заачи {task[1].upper()} введя "y"')
                            #  у берется в литинице и в русской раскладке
                            if check.lower() in ['y', 'у']:
                                name = task[1]
                                tasks.pop(tasks.index(task))
                                print(f'задача {name.upper()} удалена!')

