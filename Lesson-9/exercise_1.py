# Упражнение 1: Управление списком покупок
# Создайте список покупок, содержащий элементы "bread", "milk", "eggs".
# Измените элемент "milk" на "almond milk".
# Создайте срез, содержащий первые два элемента списка.
# Создайте вложенный список, где каждый элемент списка покупок будет содержать его цену.
<<<<<<< HEAD
pay = ["bread", "milk", "eggs"]
print(pay)
pay[1] = "almond milk"
print(pay)
pay_1 = pay[0:2]
print(pay_1)
price = [["bread ", 10], ["milk", 2], ["eggs", 3]]
print(price)
=======
>>>>>>> 8278559ef7c6b735e9f4813deb85c5c95b2f3a32

# Выведите список покупок, срез и вложенный список.
# print(shopping_list)  # Ожидаемый результат: ["bread", "almond milk", "eggs"]
# print(slice_shopping_list)  # Ожидаемый результат: ["bread", "almond milk"]
# print(detailed_shopping_list)  # Ожидаемый результат: [["bread", 1.5], ["almond milk", 3.0], ["eggs", 2.0]]



# Упражнение 2: Управление списком студентов и их оценок
# Создайте список студентов, содержащий элементы "Alice", "Bob", "Charlie", "David".
# Измените имя второго студента на "Eve".
# Создайте срез, содержащий студентов: "Bob", "Charlie".
# Создайте вложенный список, где каждый студент имеет список своих оценок.

<<<<<<< HEAD
students = ["Alice", "Bob", "Charlie", "David"]
print(students)
students[1] = "Eve"
print(students)
top_students = students[1:3]
students_grades = [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]
print(students_grades)
=======
>>>>>>> 8278559ef7c6b735e9f4813deb85c5c95b2f3a32
# Выведите список студентов, срез и вложенный список.
# print(students)  # Ожидаемый результат: ["Alice", "Eve", "Charlie", "David"]
# print(top_students)  # Ожидаемый результат: ["Bob", "Charlie"]
# print(student_grades)  # Ожидаемый результат: [["Alice", [90, 85, 88]], ["Eve", [75, 80, 82]], ["Charlie", [95, 92, 93]], ["David", [78, 85, 84]]]



# Упражнение 3: Управление списком задач
# Создайте список задач, содержащий элементы "task1", "task2", "task3", "task4.
# Измените третью задачу на "task3 updated".
# Создайте срез, содержащий последние две задачи.
# Создайте вложенный список, где каждая задача имеет свой статус (True - выполнено, False - не выполнено).

# Выведите список задач, срез и вложенный список.
# print(tasks)  # Ожидаемый результат: ["task1", "task2", "task3 updated", "task4"]
# print(last_tasks)  # Ожидаемый результат: ["task3", "task4"]
# print(detailed_tasks)  # Ожидаемый результат: [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
<<<<<<< HEAD

tasks = ["task1", "task2", "task3", "task4"]
print(tasks)
tasks[2] = "task3 updated"
last_tasks = tasks[2:]
print(last_tasks)
detailed_tasks = [["task1", True], ["task2 updated", False], ["task3", True], ["task4", False]]
print(detailed_tasks)
=======
>>>>>>> 8278559ef7c6b735e9f4813deb85c5c95b2f3a32
