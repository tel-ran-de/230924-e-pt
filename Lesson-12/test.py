# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
#
from os import remove

employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
}
print("----------------------")
print("1. Список сотрудников:")
for name in employees:
    print(f"{name}")
print("----------------------")
summa = sum(employee["salary"] for employee in employees.values())
print(f"2. Общая зарплата сотрудников: {summa}")
print("----------------------")
print("3. Добавляем нового сотрудника:")
employees["David"] = {"age": 28, "department": "IT", "salary": 6500}
for name in employees:
    print(f"{name}")
print("-----------------------")
print("4. Поднимаем зарплату Alice до 5500")
employees["Alice"] ["salary"] = 5500
print(employees)
print("_______________________")
print("Удаляем сотрудника Charlie")
del employees["Charlie"]
print(employees)
print("-----------------------")
print("Данные о каждом сотруднике")
for name, info in employees.items():
    print(f"Имя: {name}, Возоаст: {info["age"]}, Отдел: {info["department"]}, Зарплата: {info["salary"]}")
print("------------------------")

