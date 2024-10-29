# Задача 1: Анализ данных о сотрудниках
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
employees = {
    "Alice": {"age": 30, "department": "HR", "salary": 5000},
    "Bob": {"age": 25, "department": "IT", "salary": 6000},
    "Charlie": {"age": 35, "department": "Finance", "salary": 7000}}

for name in employees.keys():
    print(name)

total_salary = sum(employee["salary"] for employee in employees.values())
print(f"\nОбщая сумма зарплат всех сотрудников: {total_salary}")

employees["David"] = {"age": 28, "department": "IT", "salary": 6500}

employees["Alice"]["salary"] = 5500

del employees["Charlie"]

for name, details in employees.items():
    print(f"Имя: {name}, Возраст: {details['age']}, Отдел: {details['department']}, Зарплата: {details['salary']}")

     "Alice": {"age": 30, "department": "HR", "salary": 5000},
     "Bob": {"age": 25, "department": "IT", "salary": 6000},
     "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
 }
for name in employees.keys():
    print(name)
salary = sum([ x['salary'] for x in employees.values()])
print(salary)

employees['David'] = {'age':28, 'department': 'IT', 'Salary': 6500}
print(employees['David']['Salary'])

# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
#

inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}

for product in inventory.keys():
    print(product)

inventory["Apples"]["quantity"] += 10

inventory["Bananas"]["price"] = 1.5

del inventory["Cherries"]

inventory["Dates"] = {"quantity": 15, "price": 4}

total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"\nОбщая стоимость всех товаров: {total_value}")
# inventory = {
#     "Apples": {"quantity": 50, "price": 2},
#     "Bananas": {"quantity": 30, "price": 1},
#     "Cherries": {"quantity": 20, "price": 3},
# }

