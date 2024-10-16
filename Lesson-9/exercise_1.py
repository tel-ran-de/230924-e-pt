# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
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
# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]



# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
# Измените имя второго студента на "Eve".
# Создайте срез, содержащий студентов: "Bob", "Charlie".
# Создайте вложенный список, где каждый студент имеет список своих оценок.
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
# Выведите список студентов, срез и вложенный список.
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат: [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]



# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
# Измените третью задачу на "task3 updated".
# Создайте срез, содержащий последние две задачи.
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).
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

# Выведите список задач, срез и вложенный список.
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат: [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
