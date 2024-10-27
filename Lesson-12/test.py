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
from token import tok_name

inventory = {
    "Apples": {"quantity": 50, "price": 2},
    "Bananas": {"quantity": 30, "price": 1},
    "Cherries": {"quantity": 20, "price": 3},
}
print("---------------------")
print("1. Название всех товаров")
for name in inventory:
    print(f"{name}")
print("----------------------")
print("2. Увеличить количество яблок на 10")
inventory["Apples"]["quantity"] = 60
print("----------------------")
print("3. Изменить цену бананов на 1,5")
inventory["Bananas"]["price"] = 1.5
print("----------------------")
print("4. Удалить товар Черри")
del inventory["Cherries"]
print("----------------------")
print("5. Добавить новый товар - финики количеством 15 и ценой 4")
inventory["Dates"] = {"quantity": 15, "price": 4}
print("----------------------")

total_cost = 0
for item, details in inventory.items():
    total_cost += details["quantity"] * details["price"]
print(f"Общая стоимость товаров: {total_cost}")